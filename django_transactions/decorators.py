from typing import Callable, Union

from django.db import IntegrityError
from django.utils.timezone import now

from django_transactions.models import ExclusiveTransaction
from django_transactions.exceptions import ExclusiveTransactionException


def exclusive(slug: Union[None, str, Callable] = None):
    """
    Example of use:

    @exclusive('my_func')
    def func(self, *args):
        ...
    ________________________________________________________________
    def _exclusive_slug() -> str:
        ...

    @exclusive(_exclusive_slug)
    def func(self, *args):
        ...
    ________________________________________________________________
    result = exclusive(f'my_func_{obj.id}')(obj.func)(*args)

    """
    def inner(func):
        def wrapper(*args, **kwargs):
            if slug is None:
                slug_string = func.__name__
            elif isinstance(slug, Callable):
                slug_string = slug()
            elif isinstance(slug, str):
                slug_string = slug
            else:
                raise TypeError('Slug must be string or callable')
            try:
                transaction: ExclusiveTransaction = ExclusiveTransaction.objects.create(slug=slug_string)
            except IntegrityError:
                # Database unique constraint validation
                raise ExclusiveTransactionException('Previous transaction has not been ended')
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                transaction.error = str(e)
                raise e
            finally:
                transaction.ended = now()
                transaction.save(update_fields=('ended', 'error'))
            return result
        return wrapper
    return inner

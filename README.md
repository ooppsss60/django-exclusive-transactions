# django-exclusive-transactions

Allows to execute only one function with the same slug at the same time using DB constraints

Examples of use:

```
@exclusive()
def func(self, *args):
    ...
```
```
@exclusive('my_method')
def func(self, *args):
    ...
```
```
def _exclusive_slug() -> str:
    ...

@exclusive(_exclusive_slug)
def func(self, *args):
    ...
```
```
result = exclusive(f'my_func_{obj.id}')(obj.func)(*args)
```

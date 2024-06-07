from django.db import models
from django.db.models import Q


class ExclusiveTransaction(models.Model):
    slug = models.CharField(max_length=256)
    started = models.DateTimeField(auto_now_add=True)
    ended = models.DateTimeField(null=True, blank=True)
    error = models.TextField(null=True)

    class Meta:
        # Only one null in unique columns
        # https://wladimirguerra.medium.com/only-one-null-in-unique-columns-234672fefc08
        constraints = [
            models.UniqueConstraint(
                name='%(app_label)s_%(class)s_slug_ended_uniq',
                fields=('slug',),
                condition=Q(ended__isnull=True)
            )
        ]

    def __str__(self):
        started = self.started.strftime("%Y/%m/%d %H:%M:%S")
        ended = f'- {self.ended.strftime("%Y/%m/%d %H:%M:%S")}' if self.ended else ''
        return f'Transaction: {self.slug}: {started} {ended}'

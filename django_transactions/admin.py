from django.contrib import admin
from django.utils.timezone import now

from django_transactions.models import ExclusiveTransaction


@admin.action
def close_transactions(model_admin, request, queryset):
    queryset.filter(ended__isnull=True).update(ended=now())


@admin.register(ExclusiveTransaction)
class ExclusiveTransactionAdmin(admin.ModelAdmin):
    readonly_fields = ('slug', 'started', 'ended', 'error')
    list_display = ('slug', 'started', 'ended', 'success')
    list_filter = (
        ('ended', admin.EmptyFieldListFilter),
        ('error', admin.EmptyFieldListFilter),
    )
    actions = (close_transactions,)

    @admin.display(boolean=True)
    def success(self, obj: ExclusiveTransaction) -> bool:
        return obj.error is None

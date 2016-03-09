from django.contrib import admin
from .models import YadTransactions


class YadTransactionAdmin(admin.ModelAdmin):
    pass


admin.site.register(YadTransactions, YadTransactionAdmin)

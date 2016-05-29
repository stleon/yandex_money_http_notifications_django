from django.contrib import admin
from .models import YadTransaction


class YadTransactionAdmin(admin.ModelAdmin):
    pass


admin.site.register(YadTransaction, YadTransactionAdmin)

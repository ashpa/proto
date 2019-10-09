from django.contrib import admin
from .models import TrialBalance


# Register your models here.
class TrialBalanceAdmin(admin.ModelAdmin):
    fields = ['accountNumber',
              'accountAssetType',
              'accountSubType',
              'accountClass',
              'accountSubClass',
              'beginningBalance',
              'endingBalance']


admin.site.register(TrialBalance, TrialBalanceAdmin)

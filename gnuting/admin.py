from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from account.models import Account
from .models import Campus_Date, Date

# Register your models here.
class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'account'

class UserAdmin(BaseUserAdmin):
    inlines = (AccountInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Account)
admin.site.register(Date)
admin.site.register(Campus_Date)
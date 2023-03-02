from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import AccountCreateForm, AccountUpdateForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = AccountCreateForm
    form = AccountUpdateForm
    model = CustomUser
    list_display = ['email', 'userrealname', 'phone_number']

admin.site.register(CustomUser, CustomUserAdmin)
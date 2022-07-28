from django.contrib import admin
from .models import Users
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth import admin as auth_admin

@admin.register(Users)
class UserAdmin(auth_admin.UserAdmin):
    form=UserChangeForm
    add_form=UserCreationForm
    model=Users

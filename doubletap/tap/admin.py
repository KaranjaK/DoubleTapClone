from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from authen.forms import UserForm, CustomUserChangeForm
from .models import Person
# Register your models here.
Person = get_user_model()


# ModelAdmin
class CustomUserAdmin(UserAdmin):
    add_form = UserForm
    form = CustomUserChangeForm
    model = Person

    add_fieldsets = (
        ('Personal Details', {"fields": ('email','names','username','picture','password1','password2')}),
        ('Permissions',{"fields":('is_staff','is_active')}),
        ('Optional',{"fields":('bio','website')})
    )


    fieldsets = (
        ('Personal Details', {
            "fields": ('email',
            'names','username','picture')}),
        ('Permissions',{
            "fields":('is_staff','is_active')}),
        ('Optional',{"fields":('bio','website')})
    )
    

# admin.site.register(User, CustomUserAdmin)
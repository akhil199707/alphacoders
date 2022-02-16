from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea
# Register your models here.
class UserAdminConfig(UserAdmin):
    search_fields = ('email','first_name','last_name','phone','university','branch','specitalization')
    ordering = ('email',)
    list_display = ('first_name','last_name','is_active')
    fieldsets=(
    ('User',{'fields':('first_name','last_name','user_name')}),
    ('Permissions',{'fields':('is_staff','is_active')}),
    ('Education',{'fields':('university','branch','specitalization','status','endyear')}),
    ('Personal',{'fields':('email','DOB','bio','point')}),
    )
    formfield_overrides= {
    Profile.bio:{'widget':Textarea(attrs={'rows':10,'cols':40})},
    }
    add_fieldsets=(
    (None,{
    'classes':('wide',),
    'fields':('first_name','last_name','email','phone','user_name','password1','password2','is_staff','is_active','university','branch','specitalization','status','endyear','DOB','bio')
    }),
    )


admin.site.register(Profile, UserAdminConfig)

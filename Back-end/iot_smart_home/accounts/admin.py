from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from accounts.models import User, Customer, Contractor
from home_cntrl.models import House
from device_cntrl.models import Device


admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Contractor)
admin.site.register(House)
admin.site.register(Device)
# class UserAdmin(DefaultUserAdmin):
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Personal info', {'fields': (
#             'first_name', 'last_name', 'email', 'gender', 'age', 'role',
#         )}),
#         ('Contact info', {'fields': (
#             'phone', 'address',
#         )}),
#         ('Permissions', {
#             'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
#         }),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )
#     list_filter = ('gender', 'is_staff', 'is_superuser', 'is_active', 'groups')
#     list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
#     list_editable = ('is_staff', 'is_active')
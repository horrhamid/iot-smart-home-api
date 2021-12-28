
from django.contrib import admin
from accounts.models import User, Customer, Contractor
from home_cntrl.models import House
from device_cntrl.models import Device, DeviceInUsed, Reports


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    pass


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    pass


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    pass


@admin.register(DeviceInUsed)
class DeviceInUsedAdmin(admin.ModelAdmin):
    pass


@admin.register(Reports)
class ReportAdmin(admin.ModelAdmin):
    pass



# admin.site.register(User, UserAdmin)
# admin.site.register(Customer, CustomerAdmin)
# admin.site.register(Contractor, ContractorAdmin)
# admin.site.register(House, HouseAdmin)
# admin.site.register(Device, DeviceAdmin)
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
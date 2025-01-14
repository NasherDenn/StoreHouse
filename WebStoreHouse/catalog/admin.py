from django.contrib import admin

from .models import MethodNdt, Status, Location, Unit

admin.site.register(MethodNdt)
# admin.site.register(Type)
# admin.site.register(Manufacturer)
admin.site.register(Status)
admin.site.register(Location)


class UnitAdmin(admin.ModelAdmin):
    list_display = ('equipment_name', 'type', 'equipment_serial_number', 'total', 'location')
    list_filter = ('method', 'location', 'status')


admin.site.register(Unit, UnitAdmin)

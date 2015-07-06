from django.contrib import admin
from .models import Brand, Equipment, BackupConf
from .actions import export_as_excel

# Register your models here.
admin.site.register(Brand)
admin.site.register(BackupConf)

class BackupConfInline(admin.TabularInline):
    model = BackupConf
    extra = 1

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):

	list_display = ('brand', 'model', 'ip_conf', 'mask_conf', 'ip_swi', 'mask_swi', 'image_img')
	#readonly_fields = ('image_img',)
	list_filter = ('is_active',)
	search_fields = ('model', 'ip_conf')
	ordering = ('model',)
	fieldsets = (
			('Equipo Info',{'fields': ('brand', 'model', )}),
		)
	fieldsets = (
			('Informacion del equipo',{'fields': 
				(('brand', 'model', 'image'), ('ip_conf', 'mask_conf'),
				 ('ip_swi','mask_swi'))}),
		)

	actions = [export_as_excel]
	inlines = [BackupConfInline]


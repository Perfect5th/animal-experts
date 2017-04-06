from django.contrib import admin
from .models import Expert, FieldCategory


admin.AdminSite.site_header = "Animal Experts Admin"

# Register your models here.
class ExpertAdmin(admin.ModelAdmin):
    pass
admin.site.register(Expert, ExpertAdmin)

class FieldCategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(FieldCategory, FieldCategoryAdmin)

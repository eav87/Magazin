from django.contrib import admin
from .models import *
# admin.site.register(Auto,AutoAdmin)

# Register your models here.
# class AutoAdmin(admin.ModelAdmin):
#     list_display = ('title','model','harakteristika','data')
#     list_display_links = ('id','title')
#     search_fields = ('title','data')


admin.site.register(Auto)
admin.site.register(Part)
admin.site.register(ZapisTo)
admin.site.register(CartItem)
admin.site.register(Wheels)




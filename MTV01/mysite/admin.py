from django.contrib import admin
from mysite.models import NewTable, Product

# Register your models here.
class NewTableAdmin(admin.ModelAdmin):
    list_display=('models_f', 'datetime_f')


class ProductAdmin(admin.ModelAdmin):
    list_display=('name', 'price','qty')

admin.site.register(NewTable, NewTableAdmin)
admin.site.register(Product, ProductAdmin)

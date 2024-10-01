from django.contrib import admin

from gallerydept.models import Section, Product, Discount, Order, OrderLine

admin.site.register(Section)



class ProductAdmin(admin.ModelAdmin):
    #вид отображения админки
    list_display = ('title', 'slug', 'section', 'image', 'price', 'date')
    list_filter = ('section', )
    actions_on_bottom = True


admin.site.register(Product, ProductAdmin) #регистрация


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('code', 'value')

    def save_model(self, request, obj, form, change):
        print('Request', request)
        print('Obj', obj)
        print('Form', form)
        print('Change', change)
        super(DiscountAdmin, self).save_model(request, obj, form, change)
        print('Request', request)
        print('Obj', obj)
        print('Form', form)
        print('Change', change)


admin.site.register(Discount, DiscountAdmin)


class OrderLineAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'price', 'count')
    list_filter = ('order',)


admin.site.register(OrderLine, OrderLineAdmin)


@admin.register(Order) #вариант регистрации модели
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'display_products', 'name', 'discount',
        'phone', 'email', 'address',
        'notice', 'date_order', 'date_send',
        'status', 'display_amount'
    )
    list_filter = ('status', 'date_order')
    date_hierarchy = 'date_order'

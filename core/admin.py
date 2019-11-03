from django.contrib import admin
from .models import Prod, Service, Price, Work, CartItem, Cart

admin.site.register(Prod)
admin.site.register(Service)
admin.site.register(Price)
admin.site.register(Work)
admin.site.register(Cart)
admin.site.register(CartItem)
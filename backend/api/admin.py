from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(Delivery)

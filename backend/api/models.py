from django.db import models

# USER
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name


# RESTAURANT
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


# MENU ITEM
class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.item_name


# ORDER
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=50, default="Pending")
    order_date = models.DateTimeField(auto_now_add=True)


# ORDER ITEMS
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)


# PAYMENT
class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)


# DELIVERY
class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    delivery_status = models.CharField(max_length=50)
    delivery_time = models.CharField(max_length=50)
    address = models.TextField()


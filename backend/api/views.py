from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Restaurant, MenuItem, User, Order, OrderItem, Payment, Delivery


# ===============================
# GET ALL RESTAURANTS
# ===============================
@api_view(['GET'])
def get_restaurants(request):
    restaurants = Restaurant.objects.all().values()
    return Response(list(restaurants))


# ===============================
# GET MENU OF ONE RESTAURANT
# ===============================
@api_view(['GET'])
def get_menu(request, rid):
    items = MenuItem.objects.filter(restaurant_id=rid).values()
    return Response(list(items))


# ===============================
# PLACE ORDER (MAIN FEATURE)
# ===============================
@csrf_exempt
@api_view(['POST'])
def place_order(request):
    data = request.data
    cart = data.get("cart", [])

    # 🔴 Ensure a user exists
    user = User.objects.first()
    if not user:
        user = User.objects.create(
            name="Demo User",
            email="demo@test.com",
            password="123",
            phone="9999999999",
            address="Demo address"
        )

    # calculate total
    total = sum(float(item["price"]) for item in cart)

    # create main order
    order = Order.objects.create(
        user=user,
        total_amount=total,
        order_status="Placed"
    )

    # create order items (multiple restaurants supported)
    for item in cart:
        OrderItem.objects.create(
            order=order,
            item_id=item["id"],
            restaurant_id=item["restaurant_id"],
            quantity=1,
            price=item["price"]
        )

    # create payment record
    Payment.objects.create(
        order=order,
        payment_method="Online",
        payment_status="Paid",
        amount=total
    )

    # create delivery record
    Delivery.objects.create(
        order=order,
        delivery_status="Preparing",
        delivery_time="30 mins",
        address=user.address
    )

    return Response({"message": "Order placed successfully"})

@api_view(['GET'])
def get_orders(request):
    orders = Order.objects.all().values()
    return Response(list(orders))

@api_view(['GET'])
def get_order_items(request, oid):
    items = OrderItem.objects.filter(order_id=oid).values()
    return Response(list(items))



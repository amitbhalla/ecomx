from django.urls import path, include

from .views import all_products

app_name = "store"

urlpatterns = [
    path("", all_products, name="all_products"),
]

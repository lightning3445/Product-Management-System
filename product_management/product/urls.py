from django.contrib import admin
from django.urls import path
from product import views

urlpatterns = [
    path("add_product/",views.add_product,name="add_product"),
    path("product/",views.product_list,name="product_list"),
    path("product/<int:proid>/",views.product_detail,name="product_detail"),
    path("product/<int:proid>/edit/",views.edit_product,name="edit_product"),
    path("",views.login_view,name="login"),
    path("logout/",views.logout_view,name="logout"),
    path("delete/<int:proid>/",views.delete_product,name="delete")

]
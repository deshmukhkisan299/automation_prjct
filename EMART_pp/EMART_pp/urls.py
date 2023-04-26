"""EMART_BEZ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home import views
# from Login import views as V2
from signup import views as V1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/<int:id>/', views.User_view),
    path('seller/', views.Seller_view),
    path('product/', views.Product_view),
    path('productshow/', views.product_show),
    path('sign_up/',V1.sign_up),
    path('sign_up1/',views.SignUp1),
    # path('profile/',V2.update_profile),
    path('',views.Home_view),
    path('view/',views.view),
    path('login/',views.login),
    path('detail/<int:id>/',views.detail),
    path('add_to_cart/',views.Cartview),
    path("update/<id>/", views.update),
    path("delete/<id>/", views.delete),
    path("remove_cart/<id>/", views.remove_cart),
    path("login/", views.login),
    path("logout/", views.logout),
    path("show_cart/", views.show_add_to_cart),
    path("success/", views.success)
]


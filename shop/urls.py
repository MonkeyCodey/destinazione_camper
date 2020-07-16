from django.urls import path, include
from . import views


from django.conf.urls.static import static
from django.conf import settings




app_name = 'shop'

urlpatterns = [
    path('', views.shop, name="shop"),
    path('<int:camper_id>/', views.detail, name="detail"),
]

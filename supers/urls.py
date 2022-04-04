from django.urls import path
from . import views

urlpatterns = [
    path('', views.SuperList.as_view()),
    path('<int:pk>/', views.SuperDetail.as_view()),
    path('<int:pk>/<str:power_name>/', views.UpdatePowers.as_view())
]
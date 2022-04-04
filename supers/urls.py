from django import path
from . import views

urlpatterns = [
    path('', views.SuperList.as_view()),
    path('<int:pk>/', views.SuperDetail.as_view())
]
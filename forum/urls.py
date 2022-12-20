from django.urls import path
from . import views

urlpatterns = [
    # 주소 작성
    path('', views.index),
]
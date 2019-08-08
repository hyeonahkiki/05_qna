from django.urls import path
from . import views

urlpatterns = [
    #Create(질문을 올리는 페이지)
    path('new/', views.new),
    path('create/', views.create),
]

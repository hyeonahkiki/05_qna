from django.urls import path
from . import views

urlpatterns = [
    #Create(질문을 올리는 페이지)
    path('new/', views.new),
    path('create/', views.create),
    #Read
    path('', views.index),
    path('<int:question_id>/answers/create/', views.answer_create),
]

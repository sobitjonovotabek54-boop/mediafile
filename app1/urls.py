from django.urls import path
from . import views
urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('users/<slug:slug>/', views.user_view, name='user_view'),
]



from django.urls import path
from . import views
urlpatterns = [
    path('', views.user_list, name='user_list'),

    path('users/create/', views.user_create, name='user_create'),
    path('users/<slug:slug>/', views.user_view, name='user_view'),
    path('users/<slug:slug>/update/', views.user_update, name='user_update'),
    path('delete/<slug:slug>/', views.user_delete, name='user_delete'),
]



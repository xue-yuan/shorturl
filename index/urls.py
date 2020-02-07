from django.urls import path

from . import views

urlpatterns = [
	path('', views.index),
	path('ajax/', views.ajax),
    path('<str:hash_value>/', views.redirect_url),
]

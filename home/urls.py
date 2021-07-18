from django.urls import path
from . import views

urlpatterns = [
    # Set of empty path to indicate this is the route URL, and its going to render views.index with the name Home.

    path('', views.index, name='home'),
    path('privacy/', views.privacy, name='privacy'),
    path('tandc/', views.tandc, name='tandc'),
    path('refunds/', views.refunds, name='refunds'),
]

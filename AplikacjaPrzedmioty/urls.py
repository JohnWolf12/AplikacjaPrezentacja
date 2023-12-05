from django.urls import path

from AplikacjaPrzedmioty import views

urlpatterns = [
    path('', views.index, name='index')
]

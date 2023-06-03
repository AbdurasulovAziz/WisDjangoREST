from django.urls import path, include
from cinema import views



urlpatterns = [
    path('', views.FilmPage.as_view(), name='cinema'),
]

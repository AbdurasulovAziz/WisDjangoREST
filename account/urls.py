from django.urls import path
from account import views


urlpatterns = [
    path('register/', views.UserView.as_view(), name='user'),
    path('profile/<str:username>', views.UserDetailView.as_view(), name='user-detail'),
]

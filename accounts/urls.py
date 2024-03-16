from django.urls import path
from . import views


urlpatterns = [
    # registration
    path('register_user/', views.register_user, name='register_user'),
    
    # authentication
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('my_account/', views.my_account, name='my_account'),
    path('accounts_dashboard/', views.accounts_dashboard, name='accounts_dashboard'),
]
from django.urls import path

from . import views

app_name = 'my_login' # namespacing: https://docs.djangoproject.com/en/2.0/intro/tutorial03/#namespacing-url-names 
urlpatterns = [
    path('', views.LoginFormView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('userstable/', views.UsersView.as_view(), name='users-table')
]
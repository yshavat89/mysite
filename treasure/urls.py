from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'treasure' # namespacing: https://docs.djangoproject.com/en/2.0/intro/tutorial03/#namespacing-url-names 
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('create-treasure/', views.TreasureFormView.as_view(), name='create-treasure'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

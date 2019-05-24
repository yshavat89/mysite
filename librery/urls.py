from django.urls import path
from .views import RecordInterest,AuthorDetailView,PublisherDetail,AuthorDetail

app_name = 'librery'

urlpatterns = [
    #...
    path('author/<int:pk>/interest/', RecordInterest.as_view(), name='author-interest'),
    #path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('publisher/<int:pk>/', PublisherDetail.as_view(), name='publisher-detail'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
]
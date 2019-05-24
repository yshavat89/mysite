from django.urls import path

from . import views

app_name = 'polls' # namespacing: https://docs.djangoproject.com/en/2.0/intro/tutorial03/#namespacing-url-names 
urlpatterns = [
    #---url pattern without using "generi views"
    # ex: /polls/
    #path('', views.index, name='index'),
    # ex: /polls/5/
    #path('specifics/<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    #path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    #path('<int:question_id>/vote/', views.vote, name='vote'),
    #URL for bootsrap testing
    #path('bootstrap', views.bt4, name='bt4'),

    #---this code Use "generic views"
    path('jinja/', views.Jinja2TestsView.as_view(), name='jinja'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),  
    path('base/',views.BaseView.as_view(),name='base'),
    path('register/', views.UserFormView.as_view(), name='register'),
    path('question/add', views.QuestionCreate.as_view(), name='question_add'),
    path('choice/add', views.ChoiceCreate.as_view(), name='choice_add'),
    path('author/add', views.AuthorCreate.as_view(), name='author-create'),

]
from django.urls import path
#from .views import ArticleCreateView
from . import views

urlpatterns = [
    # path('edit/<int:pk>/', ArticleUpdateView.as_view(), name='article_update'),
    # path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    #path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete'),
    path('',views.articlelistview, name='article_list'),
    # path('new/', ArticleCreateView.as_view(), name='article_create'),
    path('<int:pk>/edit/',views.article_update, name='article_update'),
    path('<int:pk>/delete/',views.article_delete, name='article_delete'),
    path('<int:pk>/', views.articledetailview, name='article_detail'),
    path('new/', views.article_create, name='article_create'),
]

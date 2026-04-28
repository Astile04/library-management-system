from django.urls import path
from . import views,api_views


urlpatterns = [
    path('',views.book_list,name='book_list'),
    path('authors/',views.author_list,name='author_list'),
    path('members/',views.member_list,name='member_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    
    path('api/books/', api_views.book_list_api, name='book_list_api'),
    path('api/authors/',api_views.author_list_api,name='author_list_api'),
    path('api/members/', api_views.member_list_api, name='member_list_api'),
    path('api/books/<int:pk>/',api_views.book_detail_api,name='book_detail_api'),
    path('api/authors/<int:pk>/',api_views.author_detail_api,name='author_detail_api'),
    path('api/members/<int:pk>/',api_views.member_detail_api,name='member_detail_api')

    
]
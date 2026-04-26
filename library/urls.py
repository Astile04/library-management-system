from django.urls import path
from . import views


urlpatterns = [
    path('',views.book_list,name='book_list'),
    path('authors/',views.author_list,name='author_list'),
    path('members/',views.member_list,name='member_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
]
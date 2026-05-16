from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
    path('category/<str:category>/', views.category_view, name='category'),
    path('search/', views.search, name='search'),
]
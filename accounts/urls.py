from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('upload/', views.upload, name='upload_tt'),
    path('books/', views.book_list, name='book_list'),
    path('books/upload/', views.upload_book, name='upload'),
    path('books/<int:pk>/', views.delete_book, name='delete_book'),
    path('books_manager/<int:pk>/', views.update_status, name='update_status'),
    path('books_manager/', views.book_list_manager, name='book_list_manager'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
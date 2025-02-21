from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('issue/',views.issue_book),
    path('return/',views.return_book),
    path('addbook/',views.add_book),
    path('adduser/',views.add_user),
    path('bookinfo/',views.book_info),
    path('userinfo/',views.user_info),
]
from django.urls import path
from . import views

app_name = 'quotes_app'

urlpatterns = [
    path('', views.main, name='main'),
    path('page/<int:page>/', views.main, name='main'),
    path('tag/<str:tag>', views.tag_page, name='tag'),
    path('tag/<str:tag>/page/<int:page>', views.tag_page, name='tag'),
    path('author/<str:fullname>/', views.author_page, name='author'),
    path('<int:author_id>', views.delete_author, name='delete_author'),
    path('<int:quote_id>', views.delete_quote, name='delete_quote'),
]

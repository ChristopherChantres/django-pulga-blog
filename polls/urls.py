from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('create', views.create, name='create'),
  path('edit', views.edit, name='edit'),
  path('post/<int:post_id>', views.post_detail, name='post_detail'),
]

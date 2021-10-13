#creating URLs
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'), #button for adding new post for authorized user
    path('drafts/', views.post_draft_list, name='post_draft_list'), #for opportunity to review post later (posts = drafts) for authorized user
    path('post/<pk>/publish/', views.post_publish, name='post_publish'), #for adding "Publish" button if there is no published date for authorized user
    path('post/<pk>/remove/', views.post_remove, name='post_remove'), #for adding a "Delete" button for authorized user
]


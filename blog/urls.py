from django.urls import path,include
from . import views


urlpatterns = [
    path("", views.post_list,name="post_list"),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('media/images/', views.Image.as_view(), name='image'),
    path('./<int:pk>/', views.ImageDisplay.as_view(), name='image_display'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    #path('', views.index, name='index'), - zawsze kiedy dodajemy nowe widoki
]


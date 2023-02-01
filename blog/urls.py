from django.urls import path,include
from . import views


urlpatterns = [
    path("", views.post_list,name="post_list"),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('', views.Image.as_view(), name='image'),
    path('', views.ImageDisplay.as_view(), name='image_display'),
    #path('', views.index, name='index'), - zawsze kiedy dodajemy nowe widoki
]


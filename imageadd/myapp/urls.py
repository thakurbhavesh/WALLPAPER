from django.urls import path
from.import views
from .views import category

urlpatterns = [

    path('about',views.about,name="about"),
    path('',views.home,name="home"),
    path('category/<int:cid>/',category),

]

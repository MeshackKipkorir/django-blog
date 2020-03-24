from . import views
from django.urls import path 

urlpatterns = [
    path('',views.PostDetail.as_view(),name="jome"),
    path('<slug:slug>/',views.PostDetail.as_view(),name="post_detail"),
]
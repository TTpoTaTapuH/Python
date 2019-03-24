from django.urls import path
from welcome import views
app_name = 'welcome'
urlpatterns = [
    path('', views.index),
    path('registration/', views.registration),
]

#text-align: center;    position	: absolute;	top		: 0;	bottom		: 0;	left		: 0;	right		: 0;	margin		: auto;    width: 400px;    height: 280px;    background-color: rgb(226, 255, 237);    border-radius: 10px;

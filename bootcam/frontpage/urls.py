from django.urls import path
from frontpage import views

app_name = 'frontpage'

urlpatterns = [

    path('', views.index, name="index"),

]

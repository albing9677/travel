from . import views
from django.urls import path

urlpatterns = (

    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    #    path('view1/',views.view1,name='view1'),
    #    path('view2/',views.view2,name='view2')

)

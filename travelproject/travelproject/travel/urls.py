from . import views
from django.urls import path

urlpatterns = [

    path('', views.intro, name='intro'),
    #    path('view1/',views.view1,name='view1'),
    #    path('view2/',views.view2,name='view2')

]

from django.contrib import admin
from django.urls import path
#from .views import index, perros, gatos , scooby , patan, coraje, doraemon, tom, garfield
from webAyudaPeludo import views
urlpatterns = [
    path('',views.index,name='INDEX'),
    ## perros seccion
    path('perros/',views.perros,name="PERROS"),
    path('scooby/',views.scooby,name='SCOOBY'),
    path('patan/',views.patan,name='PATAN'),
    path('coraje/',views.coraje,name='CORAJE'),
    # gatos seccion
    path('gatos/',views.gatos,name='GATOS'),
    path('doraemon/',views.doraemon,name='DORAEMON'),
    path('tom/',views.tom,name='TOM'),
    path('garfield/',views.garfield,name='GARFIELD'),

    
]
# {% url '<nombre>' %} ---> lenguaje DJANGO TEMPLATE
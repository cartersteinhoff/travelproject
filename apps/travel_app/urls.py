from django.conf.urls import url
from . import views  

      
urlpatterns = [
    url(r'^$', views.index),
    url(r'^registration$', views.registration),
    url(r'^processreg$',views.processreg),
    url(r'^processlog$', views.processlog),
    url(r'^success$',views.success),
    url(r'^logout$', views.logout),
    url(r'^home$', views.home),
    url(r'^add$',views.add),
    url(r'^add_travel_plan$', views.add_travel_plan),
    url(r'^details/(?P<trip_id>\d+)$', views.details),
    url(r'^join/(?P<trip_id>\d+)$', views.join),

]
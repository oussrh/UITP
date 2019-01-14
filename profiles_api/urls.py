from django.conf.urls import url, include

from rest_framework.authtoken import views as auth_views
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('index', views.IndexViewSet, base_name='index')
router.register('profile', views.UserProfileViewSet)
router.register('incidents', views.IncidentsViewSet)
router.register('detail', views.DetailViewSet)
router.register('rapports', views.RapportsViewSet) 
router.register('Transports', views.TransportsViewSet)
router.register('TypeIncidents', views.TypeIncidentsViewSet)


# urlpatterns = [
#     url(r'^', include(router.urls)),
#     url(r'^token/', auth_views.obtain_auth_token),
# ]
urlpatterns = [
    url(r'^api/',views.Index.as_view()),
    url(r'^', include(router.urls)),

]
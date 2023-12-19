from django.urls import path, re_path

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import DefaultRouter

from . import views
from .views import UserViewSet, DoctorViewSet, SpecializationViewSet, PublicationViewSet

schema_view = get_swagger_view(title='API')

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'doctors', DoctorViewSet, basename='user')
router.register(r'specializations', SpecializationViewSet, basename='user')
router.register(r'publications', PublicationViewSet, basename='user')


urlpatterns = router.urls



# urlpatterns = [
#     path('s', schema_view),
#     path('users/', views.UserList.as_view()),
#     path('users/<int:pk>/', views.UserDetail.as_view()),
#     path('doctors/', views.AllDoctorsList.as_view()),
#     path('doctors/<int:pk>/', views.DoctorDetail.as_view()),
#     path('specializations/', views.AllSpecializationsList.as_view()),
#     path('specializations/<int:pk>/', views.SpecializationDetail.as_view()),
#     path('publications/', views.AllPublicationsList.as_view()),
#     path('publications/<int:pk>/', views.PublicationDetail.as_view()),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)
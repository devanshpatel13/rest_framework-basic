from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from app import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

# from rest_framework import routers
#
# router = routers.DefaultRouter()
# router.register("student",views.StudentViewSet)

urlpatterns = [
    # path('',include(router.urls))
    path('student/', views.SnippetList.as_view(),name = "student"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),

    # path('auth/',include('rest_framework.urls',namespace="rest_framework")),
    # path('gettoken',obtain_auth_token)



]

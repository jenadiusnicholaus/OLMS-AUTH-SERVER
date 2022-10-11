from . import views
from .Api.Views.EmployerViews import EmployerLoginView
from .views import MyTokenObtainPairView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('get-employers-by-tin/', EmployerLoginView.as_view(), name='get-employers-by-tin')
]

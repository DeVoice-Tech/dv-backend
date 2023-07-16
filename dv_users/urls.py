from django.urls import path
from django.urls import path
from .views import DVUserTokenObtainPairView

urlpatterns = [
    path('dv-user/token/', DVUserTokenObtainPairView.as_view(), name='dvuser-token-obtain-pair'),
]

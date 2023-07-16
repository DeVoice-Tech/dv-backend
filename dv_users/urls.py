from django.urls import path
from django.urls import path
from .views import DVUserTokenObtainPairView, DVUserListCreateView

urlpatterns = [
    path('dv_users/token/', DVUserTokenObtainPairView.as_view(), name='dvuser-token-obtain-pair'),
    path('dv_users/', DVUserListCreateView.as_view(), name='dvuser-list-create'),
]

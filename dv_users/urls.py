from django.urls import path
from django.urls import path
from .views import DVUserTokenObtainPairView, DVUserListCreateView

urlpatterns = [
    path('token/', DVUserTokenObtainPairView.as_view(), name='dvuser-token-obtain-pair'),
    path('', DVUserListCreateView.as_view(), name='dvuser-list-create'),
]

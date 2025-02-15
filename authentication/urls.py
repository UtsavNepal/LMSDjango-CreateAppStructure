from django.urls import path
from .views import UserSignupView, LoginView, AdminUserListView, AdminUserDetailView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', AdminUserListView.as_view(), name='admin_user_list'),
    path('users/<int:user_id>/', AdminUserDetailView.as_view(), name='admin_user_detail'),
]

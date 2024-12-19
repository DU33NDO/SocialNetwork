from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("posts/", views.PostCRUD.as_view(), name="post_list"),
    path("post/<int:pk>", views.PostCRUD.as_view(), name="post_detail"),
    path("comments/", views.CommentCRUD.as_view(), name="comments_list"),
    path("comment/<int:pk>", views.CommentCRUD.as_view(), name="comment_detail"),
    path("users/", views.UserProfileCRUD.as_view(), name="user_list"),
    path("user/<int:pk>", views.UserProfileCRUD.as_view(), name="user_detail"),
    path("auth/register/", views.UserRegisterView.as_view(), name="register_user"),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/login/', views.LoginView.as_view(), name='login'),
    path('auth/me/', views.MeView.as_view(), name='me')
]

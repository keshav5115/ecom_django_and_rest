from django.urls import path
from . import views as user_views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path("register/", user_views.register, name="user-register"),
    path("profile/", user_views.profile, name="user-profile"),
    path("profile/update/", user_views.profile_update, name="user-profile-update"),
    path(
        "",
        auth_view.LoginView.as_view(template_name="login.html"),
        name="user-login",
    ),
    path(
        "logout/",
        auth_view.LogoutView.as_view(template_name="logout.html"),
        name="user-logout",
    ),
]

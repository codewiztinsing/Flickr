from django.urls import path
from .views import user_login,dashboard,register
import django.contrib.auth.views  as auth_views

app_name = 'account'


urlpatterns = [
 # path('login/',user_login,name = 'login')
 path('login/',auth_views.LoginView.as_view(template_name = 'account/login.html'),name = 'login'),
 path('register/',register,name = 'register'),
 path('logout/',auth_views.LogoutView.as_view(template_name = 'account/logout.html'),name = 'logout'),

# password change view
 path('password-change/',auth_views.PasswordChangeView.as_view(
    template_name = 'account/password_change_form.html'),
    name = 'password_change'),
 path('password-change/done/',auth_views.PasswordChangeDoneView.as_view(
        template_name = 'account/password_change_done.html'),
        name = 'password_change_done'
        ),
 # reset password urls
path('password-reset/',
auth_views.PasswordResetView.as_view(),
name='password_reset'),
path('password-reset/done/',
auth_views.PasswordResetDoneView.as_view(),
name='password_reset_done'),
path('password-reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(),
name='password_reset_confirm'),
path('password-reset/complete/',
auth_views.PasswordResetCompleteView.as_view(),
name='password_reset_complete'),


 path('dashboard/',dashboard,name = 'dashboard'),
 
 ]
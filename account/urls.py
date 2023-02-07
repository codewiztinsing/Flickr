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
 path('password-change/',auth_views.PasswordChangeView.as_view(),name = 'password-change'),
 path('password-change/done/',auth_views.PasswordChangeDoneView.as_view(),name = 'password-change-done'),


 path('dashboard/',dashboard,name = 'dashboard'),
 
 ]
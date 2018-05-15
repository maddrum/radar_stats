from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from accounts import views

app_name = 'accounts'

urlpatterns = [
    url(r'login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'register/', views.UserRegisterView.as_view(), name='register'),
    url(r'logout/', LogoutView.as_view(next_page='../thank-you'), name='logout'),
    url(r'thank-you/', views.ThankYouView.as_view(), name='thank_you'),
    url(r'profile/', views.UserProfileMainView.as_view(), name='profile'),

]

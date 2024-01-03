from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from . forms import LogInFormClient

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='core/log_client.html', authentication_form=LogInFormClient), name='login'),
    path('signup/', views.client_signup, name='c_signup'),
    path('signup/cleaner_signup/', views.cleaner_signup, name='cleaner_signup'),
    path('signup/cleaner_signup1/', views.cleaner_signup1, name='cleaner_signup1'),
    path('logout/', views.logout_view, name='logout'),
    path('', include('client.urls'))
]

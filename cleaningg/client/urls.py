from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_redirect, name='home'),
    path('client-home/', views.client_home, name='client-home'),
    path('cleaner-home/', views.cleaner_home, name='cleaner-home'),
    path('order_creation/', views.order_creation, name='order_creation'),
    path('make-proposal/<int:pk>/', views.make_proposal, name='make-proposal'),
    path('execution-page/<int:pk>/', views.execution_page, name='execution-page'),
    path('waiting-response/<int:pk>', views.waiting_response, name='waiting-response'),
    path('show-proposals/<int:pk>', views.show_proposals, name='show-proposals'),
    path('make-review/<int:pk>', views.make_review, name='make-review'),
    path('client-settings/', views.settings, name='client-settings'),
    path('password-change/', views.password_change, name='password_change'),
    path('<int:pk>', views.details, name='details'),
    path('<int:pk>/edit/', views.edit_order, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete')
]

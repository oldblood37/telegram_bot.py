from django.urls import path
from . import views

urlpatterns = [
    path('set_webhook/', views.set_webhook, name='set_webhook'),
    path('telegram-webhook/', views.telegram_webhook, name='telegram_webhook'),
    path('login/', views.login_by_token, name='login-by-token'),
    path('logout/', views.logout_view, name='logout'),
    path('update_parser_settings/', views.update_parser_settings, name='update-parser-settings'),

]

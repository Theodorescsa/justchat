from django.urls import path

from . import views
app_name = "authenticating"

urlpatterns = [
    path("", views.register, name="register"),
    path("login/",views.signin,name = 'signin'),
    path("logout/",views.logout2,name = 'logout'),
    
    
    
]
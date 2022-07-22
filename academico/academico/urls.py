from django.contrib import admin
from django.urls import path, include
 
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
 
urlpatterns = [
    path('admin/', admin.site.urls),
    # localhost:8000/Docente/.....
    path('docente/', include('Docente.urls')),
    
     # Login and Logout
    path('login/', LoginView.as_view(redirect_authenticated_user=True,template_name='Usuario/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='Usuario/logout.html'), name='logout'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]

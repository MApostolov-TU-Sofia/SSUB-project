from django.urls import path, include
from django.conf import settings
from user import views as user_view
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
 
urlpatterns = [
    path('', user_view.index, name ='index'),
    path('login/', user_view.loginU, name ='login'),
    path('logout/', LogoutView.as_view(template_name ='user/index.html'), name ='logout'),
    path('register/', user_view.register, name ='register')
]
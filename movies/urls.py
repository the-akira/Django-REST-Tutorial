from django.contrib import admin
from django.urls import path
from resources import views as resources_views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('filmes/', resources_views.FilmeList.as_view()),
    path('filmes/<int:pk>/', resources_views.FilmeDetail.as_view()),
    path('usuarios/', resources_views.UserList.as_view()),
    path('usuarios/<int:pk>/', resources_views.UserDetail.as_view()),
    path('login/', obtain_auth_token, name='api_token_auth'),
]
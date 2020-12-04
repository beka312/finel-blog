from django.urls import path, include

from rest_project.main.views import ActivationView, RegisterView, LoginView, LogoutView, TokenRefresh

urlpatterns = [

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('activate/<str:activation_code>/', ActivationView.as_view()),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('login/refresh/', TokenRefresh.as_view()),

]
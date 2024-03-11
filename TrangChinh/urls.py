from django.urls import path
from . import views

urlpatterns = [
    path("", views.list),
    path("<int:id>/", views.post),
    
    # path("<int:id>/", views.post),
    path('register/', views.register, name="register"),
    path('login/', views.login, name='login'),
    # path('login/',auth_views.LoginView.as_view(template_name="pages/login.html"),name="login"),
    # path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]


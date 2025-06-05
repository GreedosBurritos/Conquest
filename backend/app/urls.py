from django.urls import path
from app.views import RegisterView, LoginView, GamePieceListView, home, login_page

urlpatterns = [
    path('', home, name='home'),
    path('login-page/', login_page, name='login_page'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('gamepieces/', GamePieceListView.as_view(), name='gamepieces'),
]

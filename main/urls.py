from django.urls import path
from .views import current_user_view, UserListView

app_name = 'main'

urlpatterns = [
    path('current_user/', current_user_view),
    path('users/', UserListView.as_view()),
]

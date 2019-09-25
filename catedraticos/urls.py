from django.urls import path
from catedraticos import views

app_name = 'catedraticos'

urlpatterns = [
    path('catedraticos/', views.catedratico_list_view),
    path('catedraticos/<int:pk>', views.catedratico_detail_view),
]

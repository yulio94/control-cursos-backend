from django.urls import path
from cursos import views

app_name = 'cursos'

urlpatterns = [
    path('carrera/', views.carrera_list_view),
    path('carrera/<int:pk>', views.carrera_detail_view),
    path('curso/', views.horario_list_view),
    path('curso/<int:pk>', views.horario_detail_view),
    path('horario/', views.horario_list_view),
    path('horario/<int:pk>', views.horario_detail_view),
]

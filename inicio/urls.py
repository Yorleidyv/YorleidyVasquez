from django.urls import path
from .views import (
    inicio,
    tratamiento,
    sobremi,
    TratamientoListView,
    TratamientoCreateView,
    TratamientoUpdateView,
    TratamientoDetailView,
    TratamientoDeleteView,
)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('tratamiento/', tratamiento, name='tratamiento'),
    path('tratamiento/lista/', TratamientoListView.as_view(), name='tratamiento-list'),
    path('tratamiento/nuevo/', TratamientoCreateView.as_view(), name='tratamiento-create'),
    path('tratamiento/<int:pk>/', TratamientoDetailView.as_view(), name='tratamiento-detail'),
    path('tratamiento/<int:pk>/editar/', TratamientoUpdateView.as_view(), name='tratamiento-update'),
    path('tratamiento/<int:pk>/eliminar/', TratamientoDeleteView.as_view(), name='tratamiento-delete'),
    path('sobremi/', sobremi, name='sobremi'),
]
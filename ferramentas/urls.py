from django.urls import path
from .views import list_ferramentas, create_ferramenta, update_ferramenta, delete_ferramenta

urlpatterns = [
    path('', list_ferramentas, name='list_ferramentas'),
    path('new', create_ferramenta, name='create_ferramentas'),
    path('update/<int:id>/', update_ferramenta, name='update_ferramenta'),
    path('delete/<int:id>/', delete_ferramenta, name='delete_ferramenta'),
]

# CRUD - CREATE, READ, UPDATE, DELETE
from django.urls import path
from main.views import main_view

app_name = 'main'

urlpatterns = [
    path('', main_view, name='main'),
    path('create/', main_view, name='create'),
    path('delete/', main_view),
    path('edit/', main_view),
]

from django.urls import path
from main.views import main_view

app_name = 'main'

urlpatterns = [
    path('', main_view),
    path('create/', main_view),
    path('delete/', main_view),
    path('edit/', main_view),
]

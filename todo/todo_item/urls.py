from django.urls import path
from todo_item.views import item_view, create_view

app_name = 'item'

urlpatterns = [
    path('<int:pk>', item_view, name='item'),
    path('create/<int:pk>', create_view, name='create'),
    path('delete/', item_view),
    path('edit/<int:pk>', item_view),
]

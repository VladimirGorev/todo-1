from django.shortcuts import render

data = {
    'lists': [
        {'id': 1,
         'user': 1,
         'name': 'Работа',
         'is_done': True,
         'created': '01.12.2019'
         },
        {'name': 'Дом', 'is_done': False},
        {'name': 'Учеба', 'is_done': True},
    ],
    'user_name': 'Admin',
}


def main_view(request):
    context = data
    return render(request, 'index.html', context)

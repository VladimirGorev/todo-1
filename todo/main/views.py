from django.shortcuts import render
from main.models import ListModel


def main_view(request):
    lists = ListModel.objects.filter(
        user=request.user,
    )

    # new_list = [
    #     ListModel.objects.create(
    #         name=f'Новый список{i}',
    #         user=request.user
    #     )
    #     for i in [5, 6, 7]
    # ]

    context = {
        'lists': lists,
        'user_name': request.user.username
    }
    return render(request, 'index.html', context)

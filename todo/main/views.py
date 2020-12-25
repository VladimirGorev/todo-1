from django.shortcuts import render, reverse, redirect
from main.models import ListModel
from main.forms import ListForm

def login_decorator(url='registration/'):
    #TODO Пишем код декоратора ТУТ
    pass


# @login_decorator(url='registration/')
def main_view(request):
    lists = ListModel.objects.filter(
        user=request.user,
    )

    context = {
        'lists': lists,
        'user_name': request.user.username
    }
    return render(request, 'index.html', context)


def create_view(request):
    form = ListForm()
    if request.method == 'POST':
        form = ListForm({
            'user': request.user,
            'name': request.POST.get('name')
        })
        if form.is_valid():
            success_url = reverse('main:main')
            form.save()
            return redirect(success_url)

    return render(request, 'new_list.html', {'form': form})


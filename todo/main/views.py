from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from main.models import ListModel
from main.forms import ListForm
from django.contrib.auth.decorators import login_required
from django.views import generic
from copy import copy


@login_required(login_url=reverse_lazy('registration:login'))
def main_view(request):
    lists = ListModel.objects.filter(
        user=request.user,
    )
    context = {
        'lists': lists,
        'user_name': request.user.username
    }
    return render(request, 'index.html', context)


class MainView(generic.ListView):

    model = ListModel
    template_name = 'index.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user).order_by('created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_name'] = self.request.user.username
        return context


@login_required(login_url=reverse_lazy('registration:login'))
def create_view(request):

    if request.method == 'POST':
        form = ListForm({
            'user': request.user,
            'name': request.POST.get('name')
        })
        if form.is_valid():
            success_url = reverse('main:main')
            form.save()
            return redirect(success_url)
    else:
        form = ListForm()

    return render(request, 'new_list.html', {'form': form})


class CreateView(generic.CreateView):
    model = ListModel
    template_name = 'new_list.html'
    form_class = ListForm
    success_url = reverse_lazy('main:main')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        query_dict = kwargs.get('data')
        if query_dict:
            query_dict = copy(query_dict)
            query_dict['user'] = self.request.user
            kwargs['data'] = query_dict
        return kwargs


@login_required(login_url=reverse_lazy('registration:login'))
def edit_view(request, pk):
    list_ = ListModel.objects.get(id=pk)

    if request.method == 'POST':
        form = ListForm({
            'user': request.user,
            'name': request.POST.get('name')
        }, instance=list_)

        if form.is_valid():
            success_url = reverse('main:main')
            form.save()
            return redirect(success_url)
    else:
        form = ListForm(instance=list_)

    context = {
        'form': form,
        'pk': pk
    }
    return render(request, 'edit_list.html', context)


@login_required(login_url=reverse_lazy('registration:login'))
def delete_view(request, pk):
    ListModel.objects.get(id=pk).delete()
    success_url = reverse('main:main')
    return redirect(success_url)

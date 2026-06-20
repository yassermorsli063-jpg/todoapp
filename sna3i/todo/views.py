from django.shortcuts import get_object_or_404, render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def home(request):
    if request.user.is_authenticated:
        return redirect('task_list')
    else:
        return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'todo/register/register.html', {'form': form})


@login_required(login_url='login')
def task_list(request):
    tasks = Task.objects.all()
    search_query = request.GET.get('search', '')
    if search_query:
        tasks = tasks.filter(title__icontains=search_query)

    context = {
        'tasks': tasks,
        'search_query': search_query,
    }
    return render(request, 'todo/index.html', context)


@login_required(login_url='login')
def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            task = Task(title=title)
            task.save()
    return redirect('task_list')


@login_required(login_url='login')
def task_update(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.completed = request.POST.get('completed') == 'on'
        task.save()
        return redirect('task_list')
    context = {'task': task}
    return render(request, 'todo/update_task.html', context)


@login_required(login_url='login')
def task_delete(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('task_list')
 
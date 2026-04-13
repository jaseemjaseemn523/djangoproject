from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'list.html', {'tasks': tasks})



def add_task(request):
    form = TaskForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('task_list')

    return render(request, 'add.html', {'form': form})


def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')



def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')
from django.shortcuts import render, redirect
from tasklist_app.models import Tasklist
from tasklist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def index(request):
    context = {
        'welcome_text': "Welcome to Home page",
    }
    return render(request, 'index.html', context)


@login_required
def tasklist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.person = request.user 
            instance.save()
        messages.success(request, ("New Task Added !!"))
        return redirect('tasklist')
    else:
        all_tasks = Tasklist.objects.filter(person=request.user)
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        return render(request, 'tasklist.html', {'all_tasks':all_tasks})


@login_required
def delete_task(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    if task.person == request.user:
        task.delete()
    else:
        messages.error(request, ("Access Restricted !!"))
    return redirect('tasklist')


@login_required
def edit_task(request, task_id):
    if request.method == "POST":
        task = Tasklist.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        messages.success(request, ("Task is Updated Successfully !!"))
        return redirect('tasklist')
    else:
        task_obj = Tasklist.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj': task_obj})


@login_required
def complete_task(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    if task.person == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request, ("Access Restricted !!"))
    return redirect('tasklist')


@login_required
def pending_task(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    if task.person == request.user:
        task.done = False
        task.save()
    else:
        messages.error(request, ("Access Restricted !!"))
    return redirect('tasklist')

def contact(request):
    context = {
        'contact_text':"Welcome to contact page",
    }
    return render(request, 'contact.html', context)

def about(request):
    context = {
        'about_text':"Welcome to about page.",
    }
    return render(request, 'about.html', context)

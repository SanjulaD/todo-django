from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import TodoList
from .forn import TodoListForms

# Create your views here.
def index(request):
    todo_items = TodoList.objects.order_by('id')
    form = TodoListForms()
    context = {'todo_items': todo_items, 'form': form}
    return render(request, 'todolist/index.html', context)

@require_POST
def addTodoItem(request):
    form = TodoListForms(request.POST)
    if(form.is_valid()):
        new_todo = TodoList(text=request.POST['text'])
        new_todo.save()
    return redirect('index')

def updateCompleted(request, todo_id):
    todo = TodoList.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')

def deleteCompleted(request):
    delete_todo_completed = TodoList.objects.filter(completed=True)
    delete_todo_completed.delete()
    return redirect('index')

def deleteAll(request):
    TodoList.objects.all().delete()
    return redirect('index')
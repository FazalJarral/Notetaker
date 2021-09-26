from django.shortcuts import render,redirect,get_object_or_404

from django.http import HttpResponse
from .models import Item,Category
import datetime
# Create your views here.
def index(request):

    tasks = Item.objects.all()
    categories = Category.objects.all()
    context = {"task_list" : tasks,
                "category_list":categories}



    return render(request,"index.html" , context)

def add_task(request):
    # time = datetime.now()
    title = request.POST["task"]
    iscompleted = False
    category = request.POST["category_select"]
    print(category)

    todo = Item()
    todo.title= title
    todo.iscompleted = iscompleted
    todo.category = Category.objects.get(title = category)
    todo.save()

    return redirect('/')

def complete_task(request,task_id):
    todo = Item.objects.get(id=task_id)
    todo.iscompleted = True
    todo.save()
    return redirect('/')

def delete_task(request,task_id):
    Item.objects.get(id=task_id).delete()

    return redirect('/')

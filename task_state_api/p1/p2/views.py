from django.shortcuts import render , HttpResponseRedirect , HttpResponse

from .forms import *
# Create your views here.


def add(request):
    print("hey")
    er_message = None
    su_message = None
    form = AddTaskForm(request.POST)

    if request.POST:
        if form.is_valid():
            form.save()
            task_object = Task.objects.get(pk=form.instance.pk)
            task_object.state = "draft"
            task_object.save()
            return HttpResponseRedirect('/list/')
        else:
            print(form.errors)

    context = {
        'form': form,
        'er_message': er_message,
        'su_message': su_message,

    }
    return render(request, "home.html", context)


def listall(request):
    print("hey")
    er_message = None
    su_message = None
    tasks = Task.objects.all()

    context = {
        'tasks': tasks,
    }
    return render(request, "update.html", context)


def change_state(request):
    print("hey in change state")

    state = request.GET.get("state")
    id = request.GET.get("id")
    print(state)
    t = Task.objects.get(id=id)
    t.state = state
    t.save()
    return HttpResponseRedirect("/list/")

def delete(request, id):
    tasks = Task.objects.get(id=id)
    tasks.delete()
    return HttpResponseRedirect("/list/")
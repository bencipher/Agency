from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import TodoApp
from django.utils.timezone import datetime
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def todoapp(request):
    # return HttpResponse("To do app worked.")
    if request.method == 'POST':
        # while alarm_time != '' and subject != '' and message != '':
        subject = request.POST['subject']
        alarm_time = request.POST['alarm_time']
        message = request.POST['reason']
        TodoApp.objects.create(reminder=subject, alarm_time=alarm_time, reason=message, start_time=datetime.now())
        return redirect('todoapp')
    else:
        return render(request, 'todoapp.html', {'todoitems': TodoApp.objects.all().order_by("-start_time")})

@csrf_exempt
def deleteitem(request, id):
    TodoApp.objects.get(id=id).delete()
    return redirect('todoapp')

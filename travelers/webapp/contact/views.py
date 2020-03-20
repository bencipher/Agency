from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

# Create your views here.


def contact(request):
    message = Contact()
    message.message = 'I am only testing to see how it works!'
    messages = [message]
    if request.method == 'POST':
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        if email != '' and subject != '' and firstname != '' and message != '':
            new_message = Contact.objects.create(firstname=firstname, lastname=lastname, email=email, subject=subject, message=message)
            new_message.save();
            return redirect('/')
        else:
            messages.info(request, 'please fill make sure all fields are filled appropriately')
            return redirect('contact')
    else:
        return render(request, 'contact.html', {'message': message})


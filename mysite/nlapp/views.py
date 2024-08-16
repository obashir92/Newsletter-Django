from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import SubscriberForm
from .models import Subscriber
from django.contrib import messages

# Each function(def) represents a html page

def subscribe(request):
    if request.method == 'POST':  # This statement is used to submit data/form to the server
        form = SubscriberForm(request.POST)  # This statement specifies the data type which is being submitted
        if form.is_valid():
            email = form.cleaned_data['email']
            if Subscriber.objects.filter(email=email).exists():
                messages.warning(request, 'This email address is already subscribed.')
            else:
                form.save()
                messages.success(request, 'Thank you for subscribing!')
                return redirect('thankyou')  # If the form is successfully saved we will be redirected to thankyou page
    else:
        form = SubscriberForm()
    
    return render(request, 'nlapp/subscribe.html', {'form': form})

def thankyou(request):
    return render(request, 'nlapp/thankyou.html')

def send_newsletter(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        from_email = 'o.bashir92@gmail.com'

        # Retrieve all subscribers
        subscribers = Subscriber.objects.all()

        for subscriber in subscribers:
            send_mail(
                subject,
                message,
                from_email,
                [subscriber.email],
            )

        # Display a success message
        messages.success(request, 'Newsletter sent to all subscribers!')
        return redirect('send_newsletter')  # Redirect after sending email

    return render(request, 'nlapp/send_newsletter.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BusinessCustomerForm, SwiftApplicationForm ,BussinessCustomerLoginForm
from .models import BussinessCustomer, SwiftApplication
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.core.exceptions import ObjectDoesNotExist
from .models import ChatMessage, ChatSession
import json

@csrf_exempt
def chat_view(request, chat_session_id):
    chat_messages = ChatMessage.objects.filter(chat_session_id=chat_session_id)
    return render(request, 'chat.html', {'chat_messages': chat_messages, 'chat_session_id': chat_session_id})

@csrf_exempt
def poll_messages_api(request, chat_session_id):

    last_message_timestamp = request.GET.get('last_timestamp', None)

    if last_message_timestamp:
        messages = ChatMessage.objects.filter(chat_session_id=chat_session_id, timestamp__gt=last_message_timestamp)
    else:
        messages = ChatMessage.objects.filter(chat_session_id=chat_session_id)

    serialized_messages = [
        {'user': message.user.username if message.user else 'Anonymous User', 'content': message.content, 'timestamp': str(message.timestamp)}
        for message in messages
    ]

    return JsonResponse(serialized_messages, safe=False)

@require_POST
@csrf_exempt
def send_message_api(request, chat_session_id):
   
    user = request.user if request.user.is_authenticated else None
    content = request.POST.get('content', '')
    data = json.loads(request.body.decode('utf-8'))
   
    if data['content']:
        chat_session = ChatSession.objects.get(id=chat_session_id)

        ChatMessage.objects.create(user=user, chat_session=chat_session, content=data['content'])
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Content cannot be empty'})

def initiate_chat(request):
    admin_user = User.objects.filter(is_staff=True).first()

    if request.user.is_authenticated:
        user = request.user
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.save()
            session_key = request.session.session_key

        try:
            session = Session.objects.get(session_key=session_key)
            user_id = session.get_decoded().get('_auth_user_id')
            user = User.objects.get(pk=user_id)
        except ObjectDoesNotExist:
            user = None

    chat_session = ChatSession.objects.create(user=user, admin=admin_user)

 
    return JsonResponse({'status': 'success', 'chat_session_id': chat_session.id})


def create_business_customer(request):
    try:
        if request.method == 'POST':
            form = BusinessCustomerForm(request.POST)
            if form.is_valid():
                
                print("===== in form valid =====")
                business_customer = form.save()

                request.session['business_customer_id'] = business_customer.id

                return redirect('create_swift_application')
            else:
                print("===== not valid =====")
                print(form.errors)
                return render(request,"create_business_customer.html",{'form':form,'message':form.errors})
        else:
            form = BusinessCustomerForm()
        return render(request, 'create_business_customer.html', {'form': form})
    except Exception as e:
        print(e)

def create_swift_application(request):
    business_customer_id = request.session.get('business_customer_id')
    business_customer = get_object_or_404(BussinessCustomer, id=business_customer_id)

    if request.method == 'POST':
        form = SwiftApplicationForm(request.POST)
        if form.is_valid():
            swift_application = form.save(commit=False)
            swift_application.owner = business_customer
            swift_application.save()

            messages.success(request, 'Swift Application created successfully!')
            return redirect('success')
        else:
            print(form.errors)
            return render(request, 'create_swift_application.html',{'form':form,'message':form.errors})
    else:
        form = SwiftApplicationForm()
    return render(request, 'create_swift_application.html', {'form': form})

def success(request):
    business_customer_id = request.session.get('business_customer_id')
    try:
        swift_information = SwiftApplication.objects.get(owner_id=business_customer_id)
        status = swift_information.status  
    except SwiftInformation.DoesNotExist:
        status = 'N/A' 
    messages = {
        'A': 'Congragulations !! Your process has been successfully completed.',
        'R': 'Your applications has been rejected.',
        'P': 'Your application has been submitted and is currently pending approval.',
        'N/A': 'Status not available.',
    }
    message = messages.get(status, 'Invalid status.')
    return render(request, 'success.html', {'status': status,'message':message})



def login(request):
    if request.method == 'POST':
        form = BussinessCustomerLoginForm(request.POST)
        if form.is_valid():
            
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            try:
                business_customer = BussinessCustomer.objects.get(email=email, password=password)
                request.session['business_customer_id'] = business_customer.id
                return redirect('success')
            except BussinessCustomer.DoesNotExist:
                return render(request, 'login.html', {'form': form,'message':'Invalid email or password. Please try again.'})  
    else:
        form = BussinessCustomerLoginForm()

    return render(request, 'login.html', {'form': form})   

def landing(request):
    return render(request,'landing.html')
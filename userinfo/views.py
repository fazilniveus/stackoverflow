from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_text  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .token import account_activation_token  
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage 
from .forms import ProfileUpdateForm, UserUpdateForm

# Create your views here.
username=''
#@login_required
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            """user= form.save()
            global username"""
            username = form.cleaned_data.get('username')
            """user.is_active = False  
            user.save()
            current_site = get_current_site(request)  
            mail_subject = 'Activation link has been sent to your email id'  
            message = render_to_string('userinfo/acc_active_email.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            })
            to_email = form.cleaned_data.get('email')  
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )  
            email.send()
            messages.success(request,f'Please confirm your email address to complete the registration')
        
            #return HttpResponse('Please confirm your email address to complete the registration'),x"""

            messages.success(request, f'Account Successfully created for {username}! Login In Now')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'userinfo/register.html',{'form':form})

"""def activate(request, uidb64, token): 
    User = get_user_model()  
    try:  
        uid = force_text(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()
        #messages.success(request, f'Account Successfully created for {username}! Login In Now')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
    else:  
        return HttpResponse('Activation link is invalid!')  """

@login_required
def profile(request):
    return render (request, 'userinfo/profile.html')

def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account updated successfully')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

    context ={
        'u_form' : u_form,
        'p_form' : p_form}
    return render (request, 'userinfo/profile_update.html',context)
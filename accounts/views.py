from django.shortcuts import render, redirect, get_object_or_404
from .forms import (
    NewUserForm,   
)
from .tasks import (
    welcome_user, send_welcome_sms
)
from django.contrib.auth.views import (
    LoginView
)
from accounts.models import (
     Admin,  
)
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.views.generic.edit import (
    UpdateView, DeleteView
)
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
User = get_user_model()


def register(request, utype=None):
    new_user = None
    form = None
    if request.method == 'POST':
        form = NewUserForm(request.POST, request.FILES)
        if form.is_valid():
            new_user = form.save(commit=False)
            if utype == 'admin':
                new_user.is_superuser = True
                new_user.is_staff = True

            elif utype == 'moderator':
                new_user.is_staff = True
                new_user.is_moderator = True
            elif utype == 'premium_member':
                new_user.is_premium = True
            elif utype == 'designer':
                new_user.is_designer = True
            elif utype == 'student':
                new_user.is_student = True
            else:
                new_user.is_member = True
            new_user.save()
            welcome_user(new_user.id)
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('accounts:profile')
    else:
        form = NewUserForm()
    return render(request, 'accounts/forms/registration_form.html', {
        'form': form,
        'utype': utype
    })


class SignInView(LoginView):
    template_name = 'accounts/forms/signin_form.html'


@login_required
def profile(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('dashboard:index')
        else:
            return redirect('home:index')
    else:
        return redirect('home:index')



def user_profile(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    return render(request, 'accounts/user_profile.html', {
        'user': user,
        'user_profile': user.profile,
        'user_id': str(user.id)

    })


class UpdateUserView(UpdateView):
    model = User
    fields = ['username', 'email', 'tel_no', ]
    template_name = 'accounts/forms/update_form.html'
    success_url = '/accounts/profile/'


# def new_moderator(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     if request.method == 'POST':
#         form = ModeratorRequestForm(request.POST, request.FILES)
#         if form.is_valid():
#             applicant = form.save()
#             return redirect('accounts:profile')
#     else:
#         form = ModeratorRequestForm()
#     return render(request, 'accounts/forms/moderator_request_form.html', {
#         'form': form,
#         'user': user,
#         'form_title': 'Request To Moderate'
#     })



def connect_with_user(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    current_user = request.user
    current_user.connected_users.add(user)
    current_user.save()
    return redirect('accounts:user_profile', user.pk)


def activate_user(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    user.activated = True
    user.save()
    return redirect('accounts:user_profile', user.pk)


def deactivate_user(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    user.activated = False
    user.save()
    return redirect('accounts:user_profile', user.pk)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return render('accounts/change_password_done.html')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'accounts/registration/password_change_form.html', {
        'form': form,
        'form_title': "Change Your Password"
    })

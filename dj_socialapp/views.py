from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.db import transaction
from django.http import HttpResponse
from dj_socialapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

@transaction.atomic
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        repeat_password = request.POST.get("r_password")
        
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error_message': 'Username is already taken'})
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error_message': 'There is already an account with this email'})
        if password == repeat_password:
            # Create the Django User
            user = User.objects.create_user(username=username, email=email, password=password)

            # Create the additional user_info
            user_info_data = user_info(
                user_email=email,
                user_name=username,
                user_id=user.id,
            )
            user_info_data.save()

            return redirect('signup_success', id=user.id)
        else:
            return render(request, 'register.html', {'error_message': 'Passwords do not match'})

def signup_success(request, id):
    last_registered_user = User.objects.latest('id')
    return render(request, 'signup_success.html', {'last_registered_user': last_registered_user})

@login_required
def profile(request, username):
    user_data = User.objects.filter(username=username).first()
    user_info_data = user_info.objects.filter(user_id=user_data.id)
    return render(request, 'profile.html', {'user_data': user_data, 'user_info_data': user_info_data})

def users_list(request):
    all_user_data = user_info.objects.all().values()
    print(all_user_data)
    return render(request, 'users_list.html', {'users_list' : list(all_user_data)})

def edit_profile(request):
    if request.method == "GET":
        return render(request, 'edit_profile.html')
    
    if request.method == "POST":
        full_name = request.POST.get("fullname", None)
        user_file = request.FILES.get('userprofile', None)
        user_banner = request.FILES.get('userbanner', None)

        # Retrieve existing user_info_data instance
        user_info_data = user_info.objects.filter(user_id=request.user.id).first()

        if user_info_data:
            # Update the existing instance if it exists
            if full_name:
                user_info_data.full_name = full_name
            if user_file:
                user_info_data.user_profileimage = user_file.name
            if user_banner:
                user_info_data.user_banner = user_banner.name

            user_info_data.save()

            # Save the uploaded file
            if user_file:
                destination_folder = r"/Users/rihanna/Documents/Canadian_Business_College/Project/08-Django/django_social/dj_socialapp/static/images/"
                destination_path = destination_folder + user_file.name
                with open(destination_path, 'wb+') as destination_file:
                    for chunk in user_file.chunks():
                        destination_file.write(chunk)

            if user_banner:
                destination_folder = r"/Users/rihanna/Documents/Canadian_Business_College/Project/08-Django/django_social/dj_socialapp/static/images/"
                destination_path = destination_folder + user_banner.name
                with open(destination_path, 'wb+') as destination_file:
                    for chunk in user_banner.chunks():
                        destination_file.write(chunk)


        return redirect('profile', username=request.user.username)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from . forms import SignUpFormClient, SignUpFormCleaner, CleanerProfileForm


def client_signup(request):
    if request.method == 'POST':
        form = SignUpFormClient(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    
    else:
        form = SignUpFormClient()

    return render(request, 'core/reg_client.html', {
        'form': form
    })


def cleaner_signup(request):
    if request.method == 'POST':
        form = SignUpFormCleaner(request.POST)
        if form.is_valid():
            user = form.save()
            user.profile.is_cleaner = True
            user.profile.save()
            user.profile.is_cleaner = True
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            if user is not None:
                login(request, user)

            return redirect('cleaner_signup1')
    else:
        form = SignUpFormCleaner()

    return render(request, 'core/reg_cleaner.html', {'form': form})


def cleaner_signup1(request):
    if request.method == 'POST':
        form = CleanerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            cleaner_profile = form.save(commit=False)
            cleaner_profile.user = user
            cleaner_profile.save()
            form.save()
            return redirect('home')

    else:
        form = CleanerProfileForm()

    return render(request, 'core/reg_cleaner1.html', {
        'form': form
    })


def logout_view(request):
    logout(request)
    return redirect('client-home')
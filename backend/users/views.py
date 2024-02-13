from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib import messages
from music.models import Music
from users.forms import CustomUserCreationForm

User = get_user_model()


def registerUser(request):
    '''Register user view'''
    new_song_for_player = Music.objects.filter(
        published=True).order_by('-created').first()
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.email = user.email.lower()

                user.save()
                messages.success(request, 'User account was created!')
                login(request, user)
                return redirect('home')
            except Exception:
                messages.error(request, 'An error has occurred during'
                               ' registration')

        else:
            messages.error(request, 'An error has occurred during '
                           'registration')

    context = {'form': form, 'player': new_song_for_player}
    return render(request, 'registration/signup.html', context)


def loginUser(request):
    '''Login user view'''
    if request.user.is_authenticated:
        return redirect('home')

    new_song_for_player = Music.objects.filter(
        published=True).order_by('-created').first()

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'User does not exist !')
            return render(request, 'registration/login.html',
                          {'player': new_song_for_player})

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next', 'home'))
        else:
            messages.error(request, 'User or password is incorrect !')

    context = {'player': new_song_for_player}
    return render(request, 'registration/login.html', context)


def logoutUser(request):
    '''Logout user viwe'''
    logout(request)
    messages.success(request, 'Successfully Logged out !')
    return redirect('home')

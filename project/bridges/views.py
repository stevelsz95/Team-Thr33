from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Profile
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    """
    View function for home page of site.
    """
        # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
    )

from .models import Survey
from .forms import SurveyForm
from django.contrib.auth import logout
@login_required
def form(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            current_user = request.user
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            form = SurveyForm()
            logout(request)
            return redirect('thankyou/')
    else:
        form = SurveyForm()
    return render(request, 'form.html', {'form': form})


#----------------------------------------------------------------------
#                        Signup View
#----------------------------------------------------------------------

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import SignUpForm
from .forms import EditProfileForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.year = form.cleaned_data.get('year')
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.school = form.cleaned_data.get('school')
            user.profile.major = form.cleaned_data.get('major')
            user.profile.poc = form.cleaned_data.get('poc')
            user.profile.gender = form.cleaned_data.get('gender')
            user.profile.firstgen = form.cleaned_data.get('firstgen')
            user.profile.trans = form.cleaned_data.get('trans')
            user.profile.pronoun = form.cleaned_data.get('pronoun')
            user.profile.info = form.cleaned_data.get('info')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/survey/thankyou')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def editprofile(request):
    user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request=request)
        if form.is_valid():
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.year = form.cleaned_data.get('year')
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.school = form.cleaned_data.get('school')
            user.profile.major = form.cleaned_data.get('major')
            user.profile.poc = form.cleaned_data.get('poc')
            user.profile.gender = form.cleaned_data.get('gender')
            user.profile.firstgen = form.cleaned_data.get('firstgen')
            user.profile.trans = form.cleaned_data.get('trans')
            user.profile.pronoun = form.cleaned_data.get('pronoun')
            user.profile.info = form.cleaned_data.get('info')
            user.save()
            return redirect('/survey/thankyou')
    else:
        form = EditProfileForm(request=request)
        #use same html template
    return render(request, 'signup.html', {'form': form, 'user': user})

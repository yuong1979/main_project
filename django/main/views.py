from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from .models import UserProfile, Topic, Tag, Podcast, Episode, Listener, EpisodeTimestamps, User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from django.contrib.auth import authenticate, login, logout


from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import render
from .forms import SearchForm, UserForm, MyUserCreationForm, UserProfileForm, PodcastForm, EpisodeForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from wsgiref.util import FileWrapper as WSGIFileWrapper
import os
import requests
import ssl

# from django.http import FileResponse, Http404, HttpResponse
# from django.views.decorators.http import range
# import os

# from .forms import CombinedForm

# Create your views here.


#################################
############ pages ##############
#################################

# login
# registration

# Browse Topics - scrolling page

# search podcast creator/audio - scrolling page
#    -Trending searches

# followed podcast creator - scrolling page
#    -function to unfollow
#    -function to sort

# favorite podcast audio - scrolling page (playlist)
#    -function to unfollow
#    -function to sort

# episode play - single page

# user profile / settings
#    -function decide skip timing
#    -function to autoplay next
#    -toggle notifications
#    -bio


# integrate the play audio page so that favorite episodes and episodes browser can lead to playing directly
# delete the z from my html and unwanted from templates
# add css
# check how to do subtitles on the podcast player
# when user logging in, give referral code - so when user purchases compute credits, some will be donated to the referrer




########################################################################
#################### Home page ######################################### 
########################################################################

def make_flask_api_call(request):
    operation=10
    host_address = '127.0.0.1:5000'
    url = f'http://{host_address}/process/'
    headers = {'X-API-Key': 'your_api_key'}
    payload = {'operation': operation}

    response = requests.post(url, headers=headers, json=payload, verify=False)

    if response.status_code == 200:
        result = response.json()['result']
        return JsonResponse({'result': result})
    else:
        # Handle the error case
        return JsonResponse({'error': 'Failed to make Flask API call'}, status=500)




from django.http import JsonResponse

def process_operation(request):
    operation = request.POST.get('operation')
    result = make_flask_api_call(operation)

    if result is not None:
        return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': 'Failed to process operation'}, status=500)










########################################################################
#################### Login Register ####################################
########################################################################

def loginPage(request):
    page = 'login'

    # print ('test login page')

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        # username = request.POST.get('username').lower()
        username = request.POST.get('name').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exist')

    context = {'page': page}
    return render(request, 'login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'login_register.html', {'form': form})










########################################################################
#################### Home page ######################################### 
########################################################################

def home(request):

    return redirect('browse')

    user = request.user
    if not user.is_authenticated:
        return redirect('search')

    # Get the listener
    listener = Listener.objects.get(user=request.user.userprofile)

    followed_podcasts = listener.followed_podcasts.filter()
    favorited_episodes = listener.favorited_episodes.filter()

    # q = request.GET.get('q') if request.GET.get('q') != None else ''

    # rooms = Room.objects.filter(
    #     Q(topic__name__icontains=q) |
    #     Q(name__icontains=q) |
    #     Q(description__icontains=q)
    # )
    
    data = "Home pagesssssssssss"
    context = {'home_page' : data}

    return render(request, 'home.html', context)







########################################################################
#################### User lists ######################################## INCLUDE SCROLL PAGE FOR PODCASTS?
########################################################################


def favorite_episodes(request):
    try:
        listener = Listener.objects.get(user=request.user.userprofile)
        episodes = listener.favorited_episodes.order_by('-created')
    except:
        episodes = []  # or any other appropriate default value

    context = {'episodes': episodes}
    return render(request, 'favorite_episodes.html', context)




def followed_podcasts(request):
    try:
        listener = Listener.objects.get(user=request.user.userprofile)
        podcasts = listener.followed_podcasts.order_by('-created')
    except:
        podcasts = []  # or any other appropriate default value

    context = {'podcasts': podcasts}
    return render(request, 'followed_podcasts.html', context)















########################################################################
#################### User profile ###################################### INCLUDE SCROLL PAGE FOR PODCASTS?
########################################################################
def user_profile(request, pk):
    user = User.objects.get(pk=pk)
    try:
        user_profile = user.userprofile
        bio = user_profile.bio
        avatar = user_profile.avatar
        audio_skip_time = user_profile.audio_skip_time
        audio_speed = user_profile.audio_speed
        token = user_profile.token
        notification = user_profile.notification
    except:
        bio = ""
        avatar = ""
        audio_skip_time = ""
        audio_speed = ""
        token = ""
        notification = ""

    try:
        podcast = Podcast.objects.filter(Q(owner=user_profile) | Q(operator=user_profile))
        podcast_count = podcast.count()
    except:
        podcast = ""
        podcast_count = 0

    context = {
        'name': request.user,
        'bio': bio,
        'avatar': avatar,
        'audio_skip_time': audio_skip_time,
        'audio_speed': audio_speed,
        'token': token,
        'notification': notification,
        'podcast': podcast, 
        'podcast_count': podcast_count
        }
        
    return render(request, 'user_profile.html', context)



# http://127.0.0.1:8000/user_profile/1/


# http://127.0.0.1:8000/user_profile_update/1/


@login_required(login_url='login')
def user_profile_update(request, pk):

    user = User.objects.get(pk=pk)

    #if the userprofile exists - than proceed to with extracting data from existing profile, if not to create a new profile
    try:
        profile = user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=user)
        profile.save()

    form = UserProfileForm(instance=profile)

    audio_skip_time_options = [10, 5, 10, 15, 20]
    audio_speed_options = [1, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0]

    # Check if the user has permission to make changes to the podcast
    if request.user != user:
        messages.error(request, "You are not authorised to view this page!")  # Add an error message
        return redirect('home')  # Redirect to the homepage


    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user  # Assign the current user
            user_profile.save()
            form.save()
            messages.info(request, 'User Profile has been updated.')
            return redirect('home')
        else:
            print (form.errors)

    context = {
        'form': form,
        'audio_skip_time_options': audio_skip_time_options,
        'audio_speed_options': audio_speed_options
    }


    return render(request, 'user_profile_update.html', context)












########################################################################
#################### podcast profile ################################### INCLUDE SCROLL PAGE FOR EPISODES
########################################################################
# @login_required(login_url='login')
def podcast_profile(request, pk):
    podcast_profile = Podcast.objects.get(pk=pk)

    # episode = Episode.objects.filter(Q(owner=user_profile) | Q(operator=user_profile))
    episode = Episode.objects.filter(podcast=podcast_profile)
    episode_count = episode.count()

    owner = False  # Default value
    is_followed_status = False  # Default value

    if request.user.is_authenticated:
        # Check if the user is the owner or operator of the podcast
        if request.user == podcast_profile.owner.user or request.user == podcast_profile.operator.user:
            # User has access to the podcast
            owner = True

        # get the status of the listner following podcast or not and if listener does not exist start one
        try:
            listener = Listener.objects.get(user=request.user.userprofile)
        except Listener.DoesNotExist:
            listener = Listener.objects.create(user=request.user.userprofile)
            listener.save()

        is_followed_status = listener.followed_podcasts.filter(id=pk).exists()

    context = {
        'title': podcast_profile.title,
        'podcast_owner': podcast_profile.owner,
        'operator': podcast_profile.operator,
        'podcast_image': podcast_profile.podcast_image,
        'topic': podcast_profile.topic,
        'is_active': podcast_profile.is_active,
        'description': podcast_profile.description,
        'pk': pk,
        'episode': episode, 
        'episode_count': episode_count,
        'is_followed': is_followed_status,
        'owner': owner,
        }
    
    return render(request, 'podcast_profile.html', context)

@login_required(login_url='login')
def podcast_profile_update(request, pk):
    podcast = Podcast.objects.get(pk=pk)

    # Check if the user has permission to make changes to the podcast
    if request.user.userprofile != podcast.owner and request.user.userprofile != podcast.operator:
        messages.error(request, "You are not authorised to view this page!")  # Add an error message
        return redirect('home')  # Redirect to the homepage

    form = PodcastForm(instance=podcast)

    #check if the user has permission to make changes to the podcast if not redirect

    if request.method == 'POST':
        form = PodcastForm(request.POST, request.FILES, instance=podcast)

        if form.is_valid():
            # # if the user who updates needs to be saved into the database
            # user_profile = form.save(commit=False)
            # user_profile.user = request.user  # Assign the current user
            # user_profile.save()
            print (form.cleaned_data)
            form.save()
            #change to redirect to the podcast_profile page
            return redirect('home')
        
    context = {
        'form': form,
    }
    return render(request, 'podcast_profile_update.html', context)

@login_required(login_url='login')
def podcast_profile_create(request):

    if request.method == 'POST':
        form = PodcastForm(request.POST, request.FILES)
        if form.is_valid():
            podcast = form.save(commit=False)
            podcast.owner = request.user.userprofile
            podcast.save()
            return redirect('home')
    else:
        form = PodcastForm()

    context = {'form': form}
    return render(request, 'podcast_profile_create.html', context)














########################################################################
#################### episode profile ################################### 
########################################################################

def episode_profile(request, pk):

    episode_profile = Episode.objects.get(pk=pk)
    podcast = episode_profile.podcast

    owner = False  # Default value
    is_favorited_status = False # Default value

    if request.user.is_authenticated:
        # Check if the user is the owner or operator of the podcast
        if request.user == podcast.owner.user or request.user == podcast.operator.user:
            owner = True 

        #check if the episode is existing inside the the listener favorited
        listener = Listener.objects.get(user=request.user.userprofile)
        is_favorited_status = listener.favorited_episodes.filter(id=episode_profile.id).exists()

    # Get the tags associated with the episode as a list
    tags = list(episode_profile.tags.all())

    context = {
        'title': episode_profile.title,
        'description': episode_profile.description,
        'podcast': episode_profile.podcast,
        'tags': tags,
        'media_file': episode_profile.media_file,
        'timestamp': episode_profile.timestamp,
        'is_active': episode_profile.is_active,
        'pk': pk,
        'is_favorited': is_favorited_status,
        'owner': owner,
        }
    # context = {}
    return render(request, 'episode_profile.html', context)



@login_required(login_url='login')
def episode_profile_update(request, pk):

    print (pk, "episode_profile_update baby")

    episode = Episode.objects.get(pk=pk)
    podcast = episode.podcast

    # Check if the user is the owner or operator of the podcast
    if request.user.userprofile != podcast.owner and request.user.userprofile != podcast.operator:
        messages.error(request, "You are not authorised to view this page!")  # Add an error message
        return redirect('home')  # Redirect to the homepage



    form = EpisodeForm(instance=episode)

    if request.method == 'POST':
        form = EpisodeForm(request.POST, request.FILES, instance=episode)

        if form.is_valid():
            # # if the user who updates needs to be saved into the database
            # user_profile = form.save(commit=False)
            # user_profile.user = request.user  # Assign the current user
            # user_profile.save()
            print (form.cleaned_data)
            form.save()
            return redirect('home')
        
    context = {
        'form': form,
    }
    return render(request, 'episode_profile_update.html', context)

@login_required(login_url='login')
def episode_profile_create(request, pk):

    form = EpisodeForm()
    podcast = Podcast.objects.get(pk=pk)

    # Check if the user has permission to make changes to the podcast
    if request.user.userprofile != podcast.owner and request.user.userprofile != podcast.operator:
        messages.error(request, "You are not authorised to view this page!")  # Add an error message
        return redirect('home')  # Redirect to the homepage


    if request.method == 'POST':

        form = EpisodeForm(request.POST, request.FILES)
        if form.is_valid():
            episode = form.save(commit=False)
            episode.podcast = podcast
            episode.save()
            return redirect('home')

    else:
        form = EpisodeForm()

    context = {'form': form, 'podcast': podcast}
    return render(request, 'episode_profile_create.html', context)



def episode_delete(request, pk):
    episode = Episode.objects.get(pk=pk)
    podcast = episode.podcast

    # Check if the user is the owner or operator of the podcast
    if request.user.userprofile != podcast.owner and request.user.userprofile != podcast.operator:
        messages.error(request, "You are not authorised to view this page!")  # Add an error message
        return redirect('home')  # Redirect to the homepage

    if request.method == 'POST':
        episode.delete()
        # Optionally, redirect to a success page or perform any additional actions
        return redirect('home')
    
    context = {
        'title': episode.title,
        'description': episode.description,
        'podcast': episode.podcast,
        'tags': episode.tags.all(),
        'media_file': episode.media_file,
        'timestamp': episode.timestamp,
        'is_active': episode.is_active,
        'pk': pk
    }
    return render(request, 'episode_delete.html', context)


















########################################################################
#################### searchpage ######################################## 
########################################################################

def search(request):
    query = request.GET.get('query')  # Get the search query from the request
    search_type = request.GET.get('search_type')  # Get the selected search type (podcasts or episodes)

    if not query:  # If no query is provided, return all podcasts or episodes based on the selected search type
        if search_type == 'podcasts':
            results = Podcast.objects.all()
        elif search_type == 'episodes':
            results = Episode.objects.all()
        else:
            results = []
    else:  # Perform the search based on the search query and search type
        if search_type == 'podcasts':
            results = Podcast.objects.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(topic__name__icontains=query))
        elif search_type == 'episodes':
            results = Episode.objects.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(tags__name__icontains=query))
        else:
            results = []

    # Add additional logic to display all podcasts or episodes by default when no query is provided
    if not query:
        if search_type == 'podcasts':
            results = Podcast.objects.all()
        elif search_type == 'episodes':
            results = Episode.objects.all()
        else:
            results = []

    context = {
        'query': query,
        'search_type': search_type,
        'results': results,
    }
    return render(request, 'search.html', context)






########################################################################
#################### browsepage ######################################## 
########################################################################

def browse(request):
    
    topic_counts = {}
    try:
        topics = Topic.objects.annotate(podcast_count=Count('podcasts')).order_by('-podcast_count')
        for topic in topics:
            podcast_count = Podcast.objects.filter(topic=topic).count()
            topic_counts[topic] = podcast_count
    except:
        topics = ""

    tag_counts = {}
    try:
        tags = Tag.objects.annotate(episode_count=Count('episodes')).order_by('-episode_count')
        for tag in tags:
            episode_count = Episode.objects.filter(tags=tag).count()
            tag_counts[tag] = episode_count
    except:
        tags = ""

    context = {
        'topics': topics,
        'tags': tags,
        'topic_counts': topic_counts,
        'tag_counts': tag_counts,
    }
    return render(request, 'browse.html', context)


















########################################################################
#################### toggle follow in podcast ########################## 
########################################################################
@login_required
@csrf_exempt
def toggle_follow(request, pk):

    if request.method == 'POST':
        podcast = Podcast.objects.get(id=pk)
        listener = Listener.objects.get(user=request.user.userprofile)
        #check if the podcast is existing inside the the listener followed
        podcast_exists = listener.followed_podcasts.filter(id=podcast.id).exists()
        # print ('testing ')
        if podcast_exists:
            listener.followed_podcasts.remove(podcast)
            is_followed = False
        else:
            listener.followed_podcasts.add(podcast)
            is_followed = True

        return JsonResponse({'is_followed': is_followed})
    else:
        return JsonResponse({'error': 'Invalid request'})



########################################################################
#################### toggle favorite on episodes ####################### 
########################################################################
@login_required
@csrf_exempt
def toggle_favorite(request, pk):

    if request.method == 'POST':
        episode = Episode.objects.get(id=pk)
        listener = Listener.objects.get(user=request.user.userprofile)
        #check if the episode is existing inside the the listener favorited
        episode_exists = listener.favorited_episodes.filter(id=episode.id).exists()

        if episode_exists:
            listener.favorited_episodes.remove(episode)
            is_favorite = False
        else:
            listener.favorited_episodes.add(episode)
            is_favorite = True

        return JsonResponse({'is_favorite': is_favorite})
    else:
        return JsonResponse({'error': 'Invalid request'})






class Button:
    def __init__(self, label, time):
        self.label = label
        self.time = time







########################################################################
#################### Required to stream audio ########################## 
########################################################################
def serve_audio(request, filename):
    filepath = os.path.join('static', filename)
    wrapper = WSGIFileWrapper(open(filepath, 'rb'))
    response = HttpResponse(wrapper, content_type='audio/mpeg')
    response['Content-Length'] = os.path.getsize(filepath)
    response['Accept-Ranges'] = 'bytes'
    return response




########################################################################
#################### Play audio ######################################## 
########################################################################

def episode_play(request, pk):

    episode = Episode.objects.get(id=pk)

    audio_file = episode.media_file

    # audio_file = '/audio/david_lin_interview_doomberg.mp3'
    # audio_file = '/audio/eric_sprott.mp3'
    # audio_file = "/audio/admiral_mcraven_speech.mp3"
    # audio_file = "/audio/all_in_rkj_interview.mp3"
    
    
    buttons_list = [
        Button('Skip to 0:00', 0),
        Button('Skip to 1:00', 60),
        Button('Skip to 2:00', 120),
        Button('Skip to 3:00', 180),
        Button('Skip to 4:00', 240)
    ]

    print ('audio playing')

    buttons = buttons_list

    # Get 'time' query parameter, default to 0 if not provided
    timestamp = request.GET.get('time', 0)

    # context = {}

    context = {
        'audio_file': audio_file,
        'buttons': buttons,
        'timestamp': timestamp
    }
    return render(request, 'episode_play.html', context)
    # return render(request, 'z_test_audio.html', context)

def audio_speed(request, speed):
    audio_speeds = {'1.5': 1.5, '2.0': 2.0}
    audio_speed = audio_speeds.get(speed, 1.0)
    return JsonResponse({'status': 'success', 'audio_speed': audio_speed})

def audio_forward(request):
    print ('Audio forward')
    return JsonResponse({'status': 'success', 'forward_time': 10})

def audio_backward(request):
    print ('Audio backward')
    return JsonResponse({'status': 'success', 'backward_time': 10})





# ########################################################################
# #################### Flask reference ################################# 
# ########################################################################


# from flask import Flask, render_template
# import json

# app = Flask(__name__)

# class Button:
#     def __init__(self, label, time):
#         self.label = label
#         self.time = time

# @app.route('/')
# def index():
#     print ('testing')

#     # update with your dynamic buttons
#     buttons_list = [
#         Button('Skip to 0:00', 0), 
#         Button('Skip to 1:00', 60), 
#         Button('Skip to 2:00', 120),
#         Button('Skip to 3:00', 180),
#         Button('Skip to 4:00', 240)
#     ]

#     # audio_file = 'admiral_mcraven_speech.mp3'
#     # audio_file = 'all_in_rkj_interview.mp3'

#     audio_file = 'david_lin_interview_doomberg.mp3'

#     buttons = buttons_list
#     return render_template('index.html', audio_file=audio_file, buttons=buttons)

# @app.route('/audio/speed/<speed>')
# def audio_speed(speed):
#     audio_speeds = {'1.5': 1.5, '2.0': 2.0}
#     audio_speed = audio_speeds.get(speed, 1.0)
#     return json.dumps({'status': 'success', 'audio_speed': audio_speed})

# @app.route('/audio/forward/')
# def audio_forward():
#     return json.dumps({'status': 'success', 'forward_time': 10})

# @app.route('/audio/backward/')
# def audio_backward():
#     return json.dumps({'status': 'success', 'backward_time': 10})

# if __name__ == '__main__':
#     app.run()
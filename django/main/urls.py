from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.home, name="home"),

    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('user_profile/<int:pk>/', views.user_profile, name='user_profile'),
    path('user_profile_update/<int:pk>/', views.user_profile_update, name='user_profile_update'),

    path('podcast_profile/<int:pk>/', views.podcast_profile, name='podcast_profile'),
    path('podcast_profile_update/<int:pk>/', views.podcast_profile_update, name='podcast_profile_update'),
    path('podcast_profile_create/', views.podcast_profile_create, name='podcast_profile_create'),

    path('episode_profile/<int:pk>/', views.episode_profile, name='episode_profile'),
    path('episode_profile_update/<int:pk>/', views.episode_profile_update, name='episode_profile_update'),
    path('episode_profile_create/<int:pk>/', views.episode_profile_create, name='episode_profile_create'),
    path('episode_delete/<int:pk>/', views.episode_delete, name='episode_delete'),

    # path('episode_play_sample/', views.episode_play_sample, name='episode_play_sample'),
    path('episode_play/<int:pk>/', views.episode_play, name='episode_play'),
    path('serve_audio/<path:filename>', views.serve_audio, name='serve_audio'),

    path('favorite_episodes/', views.favorite_episodes, name='favorite_episodes'),
    path('followed_podcasts/', views.followed_podcasts, name='followed_podcasts'),

    path('search/', views.search, name='search'),
    path('browse/', views.browse, name='browse'),


    path('make_flask_api_call/', views.make_flask_api_call, name='make_flask_api_call'),
    path('process_operation/', views.process_operation, name='process_operation'),



    path('toggle-follow/<int:pk>/', views.toggle_follow, name='toggle_follow'),
    path('toggle-favorite/<int:pk>/', views.toggle_favorite, name='toggle_favorite'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






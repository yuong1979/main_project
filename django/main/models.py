from django.db import models
from django.contrib.auth.models import User
from django.db.models import UniqueConstraint
import random
import string
import os
# Create your models here.



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_name = models.CharField(max_length=500, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(blank=True, null=True, default="avatar.svg")
    audio_skip_time = models.IntegerField(default=10)
    audio_speed = models.IntegerField(default=1)
    token = models.IntegerField(default=1000)
    referral_code = models.CharField(max_length=6, unique=True, null=True, blank=True)
    referred_by_referral_code = models.CharField(max_length=6, unique=True, null=True, blank=True)
    notification = models.BooleanField(default=True)
    points = models.IntegerField(default=0)


    REQUIRED_FIELDS = []

    def __str__(self):
        return self.user.username

    def generate_referral_code(self):
        chars = string.ascii_uppercase + string.digits
        code = ''.join(random.choice(chars) for _ in range(6))
        self.referral_code = code
        self.save()


# dictated by podcast creator
class Topic(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.name



# dictated by AI for episodes
class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=500, null=True, blank=True, unique=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.name



class Podcast(models.Model):
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='created_podcasts')
    operator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='operating_podcasts', blank=True, null=True)
    podcast_image = models.ImageField(upload_to='podcast_image/', blank=True, null=True, default="avatar.svg")
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, related_name='podcasts')
    description = models.TextField(max_length=4000, null=True, blank=True)
    is_active = models.BooleanField(default=False, help_text="Visibility and accessiblity of podcast to public")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.title




class Episode(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=4000, null=True, blank=True)
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE, related_name='episodes')
    tags = models.ManyToManyField(Tag, related_name='episodes')
    media_file = models.FileField(upload_to='episode_audio/')
    timestamp = models.BooleanField(default=False, help_text="Time stamp active")
    ## include the field that contains the all the words in the podcast - this serves as data for chatbot or data for subtitles
    is_active = models.BooleanField(default=False, help_text="Visibility and accessiblity of episode to public")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        # Delete the associated media file before deleting the episode object
        if self.media_file:
            # Get the file path
            file_path = self.media_file.path
            # Delete the file from the storage
            if os.path.exists(file_path):
                os.remove(file_path)

        # Call the superclass delete() method to delete the episode object
        super().delete(*args, **kwargs)



class Listener(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='listeners')
    followed_podcasts = models.ManyToManyField(Podcast, related_name='followers', blank=True)
    favorited_episodes = models.ManyToManyField(Episode, related_name='favorites', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return str(self.user)



class EpisodeTimestamps(models.Model):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, related_name='timestamps')
    timestamp_time = models.DurationField(null=True, blank=True)
    timestamp_description = models.TextField(max_length=500, null=True, blank=True)
    timestamp_first_sentence = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.episode.title






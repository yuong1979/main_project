# forms.py
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, UserProfile, Podcast, Episode
# from django.contrib.auth.models import User

class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100)


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class UserProfileForm(ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = '__all__'
#         # exclude = ['user', 'token','notification']
#         exclude = ['user', 'token']

class PodcastForm(ModelForm):
    class Meta:
        model = Podcast
        fields = '__all__'
        exclude = ['updated', 'created', 'owner']

class EpisodeForm(ModelForm):
    class Meta:
        model = Episode
        fields = '__all__'
        exclude = ['updated', 'created', 'podcast']




class UserProfileForm(forms.ModelForm):
    # UserForm fields
    username = forms.CharField()
    # UserProfileForm fields
    bio = forms.CharField()
    avatar = forms.ImageField()
    audio_skip_time = forms.IntegerField()
    audio_speed = forms.IntegerField()
    notification = forms.BooleanField(required=False)

    class Meta:
        model = UserProfile
        fields = ['bio', 'avatar', 'audio_skip_time', 'audio_speed', 'notification']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.user:
            self.fields['username'].initial = self.instance.user.username

    def save(self, commit=True):
        instance = super().save(commit=False)
        if not instance.user:
            instance.user = User.objects.create(username=self.cleaned_data['username'])
        if commit:
            instance.user.username = self.cleaned_data['username']
            instance.user.save()
            instance.save()
        return instance






# class RoomForm(ModelForm):
#     class Meta:
#         model = Room
#         fields = '__all__'
#         exclude = ['host', 'participants']

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(blank=True, null=True)
#     avatar = models.ImageField(null=True, default="avatar.svg")
#     audio_skip_time = models.IntegerField(default=10)
#     audio_speed = models.IntegerField(default=1)
#     token = models.IntegerField(default=1000)
#     # Add additional fields as per your user profile requirements
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.user.username

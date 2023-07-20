from django.contrib import admin

# Register your models here.


from .models import UserProfile, Topic, Tag, Podcast, Episode, Listener, EpisodeTimestamps


admin.site.register(UserProfile)
admin.site.register(Topic)
admin.site.register(Tag)
admin.site.register(Podcast)
admin.site.register(Episode)
admin.site.register(Listener)
admin.site.register(EpisodeTimestamps)



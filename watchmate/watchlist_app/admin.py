from django.contrib import admin
from watchlist_app.models import WatchList,StreamPlatform,Reviews
# Register your models here.

admin.site.register(WatchList)
admin.site.register(StreamPlatform)
admin.site.register(Reviews)
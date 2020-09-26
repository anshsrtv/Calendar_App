from django.contrib import admin
from calendarapp.models import Event, EventMember, Profile, EventForm

class EventMemberAdmin(admin.ModelAdmin):
    model = EventMember
    list_display = ['event', 'user']

admin.site.register(Event)
admin.site.register(EventMember, EventMemberAdmin)
admin.site.register(Profile)
admin.site.register(EventForm)

from django.apps import AppConfig


class CalendarappConfig(AppConfig):
    name = 'calendarapp'
    
    def ready(self):
        from . import signals

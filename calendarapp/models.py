from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('calendarapp:event-detail', args=(self.id,))

    @property
    def get_html_url(self):
        url = reverse('calendarapp:event-detail', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'


class EventMember(models.Model):
    status_choices = [
        ['APP','Approved'],
        ['PND','Pending'],
        ['RJD','Rejected']
    ]
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices = status_choices, default='PND')
    host_id = models.IntegerField()

    class Meta:
        unique_together = ['event', 'user']

    def __str__(self):
        return str(self.user)


class Profile(models.Model):
    user_types = [
        ['GST','Guest'],
        ['HST','Host'],
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=100, choices=user_types, default='GST')

    def __str__(self):
        return self.user.username+'-'+self.user_type
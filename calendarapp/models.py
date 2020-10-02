from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# class Event(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200, unique=True)
#     description = models.TextField()
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()
#     created_date = models.DateTimeField(auto_now_add=True)
#     status = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title
    
#     def get_absolute_url(self):
#         return reverse('calendarapp:event-detail', args=(self.id,))

#     @property   
#     def get_html_url(self):
#         url = reverse('calendarapp:event-detail', args=(self.id,))
#         return f'<a href="{url}"> {self.title} </a>'


# class EventMember(models.Model):
#     status_choices = [
#         ['APP','Approved'],
#         ['PND','Pending'],
#         ['RJD','Rejected']
#     ]
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     status = models.CharField(max_length=100, choices = status_choices, default='PND')
#     host_id = models.IntegerField()

#     class Meta:
#         unique_together = ['event', 'user']

#     def __str__(self):
#         return str(self.user)


class Profile(models.Model):
    user_types = [
        ['GST','Guest'],
        ['HST','Host'],
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=100, choices=user_types, default='GST')

    def __str__(self):
        return self.user.username+'-'+self.user_type

class EventForm(models.Model):
    form_status_choices = [
        ['APP','Approved'],
        ['PND','Pending'],
        ['RJD','Rejected']
    ]

    name = models.CharField(max_length=500)
    address = models.TextField()
    email = models.EmailField()
    link = models.URLField()
    date = models.DateField(unique=True)
    mem_org = models.CharField(max_length=500)
    tc_pc = models.CharField(max_length=500)
    mo_approval = models.BooleanField(default=False)
    tc_pc_approval = models.BooleanField(default=False)
    fund_support = models.BooleanField()
    add_info = models.TextField(null=True, blank=True)
    form_status = models.CharField(max_length=100, choices = form_status_choices, default='PND')
    days = models.IntegerField(default=1)

    def __str__(self):
        return self.name+'-'+str(self.date)

    def get_absolute_url(self):
        return self.link

    @property   
    def get_html_url(self):
        url = self.link
        return f'<a href="{url}" style="color:#000000;"><font size=2>{self.name}</font></a>'

class ContinuedEvent(models.Model):
    event = models.ForeignKey(EventForm, on_delete= models.CASCADE)
    date = models.DateField(unique=True)

    def __str__(self):
        return self.event.name+'-'+str(self.date)
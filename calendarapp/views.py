# cal/views.py

from datetime import date
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import timedelta
import calendar
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .serializers import EventFormSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import datetime
from .models import *
from .utils import Calendar
# from .forms import EventForm, AddMemberForm

@login_required(login_url='signup')
def index(request):
    return HttpResponse('hello')

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

class CalendarView(LoginRequiredMixin, generic.ListView):
    login_url = 'login'
    model = EventForm
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        try:
            profile= Profile.objects.get(user=self.request.user)
        except:
            context['host']=False
        else:
            if(profile.user_type=='HST'):
                context['host']=True
            else:
                context['host']=False
        return context

# @login_required(login_url='signup')
# def create_event(request):    
#     form = EventForm(request.POST or None)
#     if request.POST and form.is_valid():
#         title = form.cleaned_data['title']
#         description = form.cleaned_data['description']
#         start_time = form.cleaned_data['start_time']
#         end_time = form.cleaned_data['end_time']
#         Event.objects.get_or_create(
#             user=request.user,
#             title=title,
#             description=description,
#             start_time=start_time,
#             end_time=end_time
#         )
#         return HttpResponseRedirect(reverse('calendarapp:calendar'))
#     return render(request, 'event.html', {'form': form})

# class EventEdit(generic.UpdateView):
#     model = EventForm
#     fields = ['title', 'description', 'start_time', 'end_time']
#     template_name = 'event.html'

# @login_required(login_url='signup')
# def event_details(request, event_id):
#     event = Event.objects.get(id=event_id)
#     eventmember = EventMember.objects.filter(event=event)
#     context = {
#         'event': event,
#         'eventmember': eventmember,
#     }
#     # event_request=EventMember.objects.get(user=request.user, event=event)
#     try:
#         profile= Profile.objects.get(user=request.user)
#     except:
#         context['host']=False
#     else:
#         if(profile.user_type=='HST'):
#             context['host']=True
#         else:
#             context['host']=False
#         print(profile)
#     print(context['host'])
    
#     return render(request, 'event-details.html', context)


# def add_eventmember(request, event_id):
#     forms = AddMemberForm()
#     if request.method == 'POST':
#         forms = AddMemberForm(request.POST)
#         if forms.is_valid():
#             member = EventMember.objects.filter(event=event_id)
#             event = Event.objects.get(id=event_id)
#             user = forms.cleaned_data['user']
#             EventMember.objects.create(
#                 event=event,
#                 user=user,
#                 status='APP',
#                 host_id=user.pk
#             )
#             return redirect('calendarapp:calendar')
#     context = {
#         'form': forms
#     }
#     return render(request, 'add_member.html', context)

# class EventMemberDeleteView(generic.DeleteView):
#     model = EventMember
#     template_name = 'event_delete.html'
#     success_url = reverse_lazy('calendarapp:calendar')

# @login_required(login_url='login')
# def event_member_request(request, event_id):
#     event = Event.objects.get(pk=event_id)
#     context = {
#         'event': event
#     }
#     try: 
#         profile = Profile.objects.get(user=request.user)
#     except:
#         print("NO PROFILE")
#         return render(request, 'event-details.html', context)
#     else: 
#         if profile.user_type=='GST':
#             try:
#                 eventmember = EventMember.objects.create(
#                     event=event,
#                     user=request.user,
#                     status='PND',
#                     host_id=event.user.pk
#                 )
#             except:
#                 eventmember = EventMember.objects.get(user=request.user, event=event)
#                 print("Event Member")
#                 context['eventmember'] = eventmember
#                 return render(request, 'event-details.html', context)
#             else:
#                 context['eventmember'] = eventmember
#                 print("created")
#                 return render(request, 'event-details.html', context)
#         else:
#             context['eventmember.status'] = "Approved"
#             print("HST")
#             return render(request, 'event-details.html', context)

# def change_request_status(request, request_id, **kwargs):
#     req = EventMember.objects.get(pk= request_id)
#     print(req.event)
#     event = Event.objects.get(pk=req.event.id)
#     eventmember = EventMember.objects.filter(event=event)
#     context = {
#         'event': event,
#         'eventmember': eventmember,
#     }
#     try: 
#         profile = Profile.objects.get(user=request.user)
#     except:
#         return render(request, 'event-details.html', context)
#     else: 
#         if profile.user_type=='HST':
#             req.status='APP'
#             req.save()
#             context['host']=True
#     return render(request, 'event-details.html', context)

# New Stuff
class EventFormView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EventFormSerializer
    # template_name = 'index.html'

    def get(self, request, **kwargs):
        return render(request, 'index.html', kwargs)

    def post(self, request, **kwargs):
        # try: 
        #     profile = Profile.objects.get(user=self.request.user)
        # except:
        #     return Response(
        #         {"detail":"You are not a member of this organisation"},
        #         status.HTTP_401_UNAUTHORIZED
        #     )
        # else: 
        #     if profile.user_type=='HST':
        try: 
            date = datetime.date(int(kwargs['year']), int(kwargs['month']), int(kwargs['day']))
        except:
            return Response({"Not a Valid Date"}, status.HTTP_400_BAD_REQUEST)
        else:
            for i in range(1, int(request.data['days'])):
                days = timedelta(days=i)
                # try:
                conts=ContinuedEvent.objects.filter(
                    date=date + days
                ) 
                events = EventForm.objects.filter(
                    date=date + days
                )
                if events or conts:
                    return render(request, 'error.html', {"header":"400 BAD REQUEST", "errors": f"Conflicting Dates with {events[0]}. Please conduct your event on free dates"})

            serializer = EventFormSerializer(data = self.request.data)
            if serializer.is_valid():
                serializer.save(date)
                print(serializer.data)
                return render(request, 'form_submit.html')
            else:
                data = serializer.errors
                print(data)
                return render(request, 'error.html', {"header":"400 BAD REQUEST","errors": data})
        # else:
        #     return Response({"detail": "You are not authorised to create this."}, status.HTTP_403_FORBIDDEN)
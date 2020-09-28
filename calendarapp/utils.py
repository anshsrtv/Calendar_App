# calendarapp/utils.py

from datetime import datetime, timedelta, date
from calendar import HTMLCalendar
from .models import EventForm
from eventcalendar.helper import get_current_user

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, eventforms):
		events_per_day = eventforms.filter(date__day=day)
		d = ''
		
		for event in events_per_day:
			d += f'<li> {event.get_html_url} </li>'
		# today = date.today()
		#  and day>today.day and self.month>=today.month and self.year>=today.year
		if day != 0:
			if d=='':
				return f"<td bgcolor='#27ae60'><span class='date'><a href='/event/{self.year}/{self.month}/{day}/'>{day}</a></span><ul><font color='black'> {d} </font></ul></td>"
			elif events_per_day[0].form_status=='APP':
				return f"<td bgcolor='#DC143C'><span class='date'>{day}</span><ul> <font color='black'>{d} </font></ul></td>"
			elif events_per_day[0].form_status=='PND':
				return f"<td bgcolor='#fada5e'><span class='date'>{day}</span><ul><font color='black'> {d} </font></ul></td>"
				
		else:
			return "<td bgcolor='#d0d3d4'></td>"

	# formats a week as a tr 
	def formatweek(self, theweek, eventforms):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, eventforms)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		events = EventForm.objects.filter(date__year=self.year, date__month=self.month)

		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}\n'
		return cal
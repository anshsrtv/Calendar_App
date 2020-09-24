
from django.contrib import admin
from django.urls import path, include
from .views import signup, user_logout, log_in
from calendarapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('login/', log_in, name='login'),
    path('logout/', user_logout, name='logout'),
    path('event/<int:event_id>/request/', views.event_member_request, name='event_member_request'),
    path('request/<int:request_id>/', views.change_request_status, name='change_request_status'),
    path('', include('calendarapp.urls')),
]

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import EventForm
from django.core.mail import send_mail

@receiver(post_save, sender=EventForm)
def mail_user(sender, created, instance, **kwargs):
    # send_mail(
    #         'Acknowledgement from IFTOMM',
    #         'We have successfully received your application. We will contact you, in case things work out well.',
    #         'naughty.ansh007@gmail.com',
    #         [instance.email]
    #     )
    # print(instance.email)
    if created==True:

        try:
            send_mail(
            'Acknowledgement from IFTOMM',
            'We have successfully received your application. We will contact you, in case things work out well.',
            'naughty.ansh007@gmail.com',
            [instance.email],
            fail_silently=False,
        )
        except:
            print("Email Not Sent")
    else: 
        pass

@receiver(pre_save, sender=EventForm)
def mail_status(sender, created, instance, **kwargs):
    # print(instance.email+'-'+str(instance.pk))
    if created==False:
        try:
            form = EventForm.objects.get(pk=instance.pk)
        except:
            print("Form not Found")
        else:
            if form.form_status!=instance.form_status and instance.form_status=='APP':
                try:
                    send_mail(
                        'Approval for event on {} by IFTOMM'.format(instance.date),
                        'Your application has been approved by IFTOMM. We will forward to your event',
                        'naughty.ansh007@gmail.com',
                        [instance.email],
                        fail_silently=False,
                    )
                except:
                    print("Email Not Sent")
            else: 
                pass
    else: 
        pass


        
    
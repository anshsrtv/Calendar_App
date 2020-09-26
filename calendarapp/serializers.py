from rest_framework import serializers
from .models import EventForm

class EventFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventForm
        fields = [
            'name', 
            'address', 
            'email', 
            'link', 
            'mem_org', 
            'tc_pc', 
            'mo_approval', 
            'tc_pc_approval', 
            'fund_support', 
            'add_info'
        ] 
    def save(self, date):
        name = self.validated_data['name']
        link = self.validated_data['link']
        address = self.validated_data['address']
        email = self.validated_data['email']
        mem_org = self.validated_data['mem_org']
        tc_pc = self.validated_data['tc_pc']
        mo_approval = self.validated_data['mo_approval']
        tc_pc_approval = self.validated_data['tc_pc_approval']
        fund_support = self.validated_data['fund_support']
        add_info = self.validated_data['add_info']
        try: 
            EventForm.objects.create(
                name = name,
                address = address,
                email = email,
                link= link,
                date= date,
                mem_org= mem_org,
                tc_pc= tc_pc,
                mo_approval= mo_approval,
                tc_pc_approval= tc_pc_approval,
                fund_support= fund_support,
                add_info= add_info
            )
        except:
            pass
from django import forms
from.models import Appointment, Vehicle, Service

class DynamicServiceChoiceField(forms.ModelChoiceField):
    def __init__(self, *args, **kwargs):
        self.vehicle = kwargs.pop('vehicle', None)
        super(DynamicServiceChoiceField, self).__init__(*args, **kwargs)
        if self.vehicle:
            self.queryset = Service.objects.filter(category=self.vehicle.category)

class AppointmentForm(forms.ModelForm):
    service = DynamicServiceChoiceField(queryset=Service.objects.none(), required=False)

    class Meta:
        model = Appointment
        fields = ['vehicle', 'service', 'status', 'appointment_date', 'description']

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['service'].widget.attrs.update({'class': 'form-control'})
        # Update the queryset dynamically based on the selected vehicle
        if self.instance.pk:
            self.fields['service'].queryset = Service.objects.filter(category=self.instance.vehicle.category)

    def clean(self):
        cleaned_data = super(AppointmentForm, self).clean()
        service = cleaned_data.get('service')
        description = cleaned_data.get('description')

        if service and service.type == Service.ServiceTypeChoices.CUSTOM and not description:
            self._errors['description'] = self.error_class(['Please enter service details for custom appointment.'])
            del cleaned_data['description']
        return cleaned_data


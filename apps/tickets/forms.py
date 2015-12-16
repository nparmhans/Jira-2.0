from __future__ import unicode_literals

from django import forms

from .models import Ticket


class TicketForm(forms.ModelForm):

    title = forms.CharField(max_length=128)
    description = forms.Textarea()
    priority_level = forms.ChoiceField(choices=Ticket.PRIORITY_LEVEL)

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'priority_level']
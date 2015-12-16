import json
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from django.shortcuts import render

from .forms import TicketForm
from .models import Ticket


# Create your views here.


def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(data=request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': 'Ticket successfully created! Click View Tickets.'})
        else:
            return HttpResponse(json.dumps({'error': 'Please check form.'}), content_type='application/json',
                                status=400)
    return HttpResponse(status=400)


def show_tickets(request):
    ticket = Ticket.objects.all().order_by('priority_level')
    context = {'ticket': ticket}
    return render(request, 'tickets/tickets.html', context)

from django.conf.urls import url

urlpatterns = [
    url(r'^new/', 'apps.tickets.views.create_ticket', name='new_ticket'),
    url(r'^show/$', 'apps.tickets.views.show_tickets', name='show')
]

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Ticket(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    engineer = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='engineer', null=True, blank=True)
    ticket_id = models.CharField(max_length=15, unique=True)
    ticket_title = models.CharField(max_length=50)
    ticket_description = models.TextField()
    ticket_type = models.CharField(max_length=20, choices=(('Hostel', 'Hostel'), ('College Issue', 'College Issue'), ('General', 'General')), default='General')
    status = models.CharField(max_length=20, choices=(('Active', 'Active'), ('Pending', 'Pending'), ('Resolved', 'Resolved')), default='Pending')
    created_on = models.DateTimeField(auto_now_add=True)
    lastmodified = models.DateTimeField(auto_now=True)
    is_resolved = models.BooleanField(default=False)
    severity = models.CharField(max_length=5, choices=(('1', '1'), ('2', '2'), ('3', '3')), default = '2')
    is_assigned_to_engineer = models.BooleanField(default=False)
    resolution_steps = models.TextField(blank = True, null = True)


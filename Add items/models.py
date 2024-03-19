from django.db import models
from django.conf import settings

class Event(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.name

class TicketType(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.IntegerField()

    def __str__(self):
        return f"{self.name} for {self.event.name}"

class Ticket(models.Model):
    ticket_type = models.ForeignKey(TicketType, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ticket_type.name} owned by {self.owner.username}"

class Purchase(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tickets = models.ManyToManyField(Ticket)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Purchase by {self.user.username} on {self.purchase_time}"
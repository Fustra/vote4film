from datetime import datetime

from django.conf import settings
from django.db import models


class Event(models.Model):
    date = models.DateField(unique=True)

    def __str__(self):
        return f"Event on {self.date}"

    def __repr__(self):
        return f"<Event(pk={self.pk})>"


class RegisterQuerySet(models.QuerySet):
    def next_event_register(self, user):
        # TODO: This might not be right even for Europe/London!
        today = datetime.utcnow().date()
        next_event = Event.objects.filter(date__gte=today).order_by("date").first()
        if not next_event:
            return Register.objects.none()

        return Register.objects.get_or_create(user=user, event=next_event)[0]


class Register(models.Model):
    class Meta:
        unique_together = [["user", "event"]]

    objects = RegisterQuerySet.as_manager()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    is_present = models.NullBooleanField()

    def __str__(self):
        text = "present" if self.is_present else "absent"
        return f"{self.user} is {text} on {self.event.date}"

    def __repr__(self):
        return f"<Register(pk={self.pk})>"

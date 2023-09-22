from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Wallet(models.Model):
    def balance(self):
        total_received = self.payments_received.filter(receiver=self).aggregate(
            total_received=models.Sum("amount")).get(
            "total_received")
        total_payed = self.payments_made.filter(receiver=self).aggregate(total_received=models.Sum("amount")).get(
            "total_received")
        return total_received - total_payed


class Payment(models.Model):
    print("running payment")
    payer = models.ForeignKey(Wallet, on_delete=models.PROTECT, related_name="payments_made", null=True)
    receiver = models.ForeignKey(Wallet, on_delete=models.PROTECT, related_name="payments_received", null=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2)


class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)

    phone_number = models.CharField(max_length=15, blank=True)
    wallet = models.OneToOneField("Wallet", on_delete=models.PROTECT, null=True)

    def save(self, *args, **kwargs):
        if not self.wallet:
            self.wallet = Wallet.objects.create()
        super().save(*args, **kwargs)


class Event(models.Model):
    title = models.CharField(max_length=50)
    wallet = models.OneToOneField(Wallet, on_delete=models.PROTECT)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name="events_owned")
    staff = models.ManyToManyField(User, related_name="events_staffed")

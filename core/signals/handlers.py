from store.models import Customer
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from store.signals import order_created

@receiver(order_created)
def on_order_created(sender, **kwargs):
    print(kwargs['order'])
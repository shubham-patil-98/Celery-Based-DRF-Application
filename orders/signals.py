from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Order
from django.core.signals import request_finished



@receiver(post_save, sender = Order)
def order_saved(sender, instance, created, **kwargs):
    if created:
        # Perform action for a newly created instance
        print(f"New order created:  by {instance.customer}")
    else:
        # Perform action for an updated instance
        print(f"Order updated: {instance.customer}")

@receiver(pre_save, sender = Order)
def order_saved(sender, instance, **kwargs):
    print(f"New Pre Request")

# @receiver(request_finished)
# def log_request(sender, **kwargs):
#     print("A request has been finished!")
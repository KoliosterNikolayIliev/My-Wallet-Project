from django.db.models.signals import post_save
from django.dispatch import receiver

from authentication.models import UserProfile, NordigenRequisition


@receiver(post_save, sender=UserProfile)
def create_and_save_requisition(sender, instance, created, **kwargs):
    if created:
        NordigenRequisition.objects.create(user=instance).save()

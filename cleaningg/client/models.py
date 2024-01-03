from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], blank=True, null=True)
    communication_rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], blank=True, null=True)
    
    def __str__(self):
        return self.profile.user.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=30, blank=True, null=True)
    building_number = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    apartment_number = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    INN = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    card_number = models.DecimalField(max_digits=16, decimal_places=0, blank=True, null=True)
    is_cleaner = models.BooleanField(blank=True, null=True)
    reviews = models.ManyToManyField('Review', blank=True, related_name='profiles')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class CleanerProfile(models.Model):
    CITY_CHOICES = [
        ('Lviv', 'Lviv'),
        ('Kiyv', 'Kiyv'),
        ('Odessa', 'Odessa'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    reason_for_leaving = models.TextField(blank=True, null=True)
    previous_work_experience = models.BooleanField(default=False)
    punctuality = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], blank=True, null=True)
    stress_resilience = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], blank=True, null=True)
    cleaning_speed = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], blank=True, null=True)
    cleaning_quality = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], blank=True, null=True)
    willing_to_work_in_team = models.BooleanField(default=False)
    own_cleaning_equipment = models.BooleanField(default=False)
    city = models.CharField(max_length=10, choices=CITY_CHOICES, blank=True, null=True)


class Package(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=4, decimal_places=0)
    description = models.TextField()

    def __str__(self):
        return self.name


class Order(models.Model):
    WAYS_TO_ENTER = {
        ('H', 'I will be at home'),
        ('K', 'I will give a key'),
        ('O', 'Other option')
    }

    street = models.CharField(max_length=55)
    city = models.CharField(max_length=20)
    building_number = models.CharField(max_length=3)
    apartment_number = models.DecimalField(max_digits=3, decimal_places=0)
    metres = models.DecimalField(max_digits=3, decimal_places=0)
    date = models.DateField()
    time = models.TimeField()
    created_by = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE, null=True)
    is_taken = models.BooleanField(blank=True, null=True, default=False)
    proposals = models.DecimalField(max_digits=3, decimal_places=0, default=0)
    accepted = models.DecimalField(max_digits=1, decimal_places=0, default=0)
    proposals_list = models.ManyToManyField('Proposal', related_name='orders', blank=True)
    taken_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    is_done_cleaner = models.BooleanField(blank=True, null=True, default=False)
    is_done_client = models.BooleanField(blank=True, null=True, default=False)
    client_price = models.DecimalField(max_digits=4, decimal_places=0)
    

    enter = models.CharField(
        max_length=1,
        choices=WAYS_TO_ENTER,
        default='H'
    )    

    package = models.ForeignKey(Package, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.street
    
class Proposal(models.Model):
    price = models.DecimalField(max_digits=5, decimal_places=0)
    comment = models.CharField(max_length=200)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.order.street
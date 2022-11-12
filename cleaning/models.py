from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

STATUS = ((0, 'Draft'), (1, 'Published'))
APPROVED = ((0, 'Pending'), (1, 'Confirmed'))
TYPES = ((0, 'Deep Cleaning'), (1, 'General Cleaning'))
TIME_SLOTS = (
        (0, '09:00 – 09:30'),
        (1, '10:00 – 10:30'),
        (2, '11:00 – 11:30'),
        (3, '12:00 – 12:30'),
        (4, '13:00 – 13:30'),
        (5, '14:00 – 14:30'),
        (6, '15:00 – 15:30'),
        (7, '16:00 – 16:30'),
    )


class Reviews(models.Model):
    title = models.CharField(max_length=100, unique=True)
    name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='review_post')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    image = CloudinaryField('image', blank=True, default=' ')
    status = models.IntegerField(choices=STATUS, default=1)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class BookingSystem(models.Model):
    name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='booking_sys')
    cleaning_type = models.IntegerField(choices=TYPES)
    booked = models.DateTimeField(auto_now=True)
    cleaning_date = models.DateField()
    time_slot = models.IntegerField(choices=TIME_SLOTS)
    status = models.IntegerField(choices=APPROVED, default=0)

    class Meta:
        ordering = ['-booked']

    def __str__(self):
        return f"""{self.name} booked a {self.get_cleaning_type_display()}
        to {self.cleaning_date} at {self.get_time_slot_display()}"""

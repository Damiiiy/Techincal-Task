from django.db import models

class PropertyListing(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    property_type = models.CharField(max_length=100)
    bedrooms = models.PositiveIntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    agent_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

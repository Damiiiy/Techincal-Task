from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import PropertyListing

class PropertyListingTests(APITestCase):
    def setUp(self):
        self.listing1 = PropertyListing.objects.create(
            title="Lagos Apartment",
            price=5000000.00,
            property_type="Apartment",
            bedrooms=3,
            latitude=6.5244,
            longitude=3.3792,
            agent_id="agent_1"
        )
        self.listing2 = PropertyListing.objects.create(
            title="Abuja House",
            price=15000000.00,
            property_type="House",
            bedrooms=5,
            latitude=9.0579,
            longitude=7.4951,
            agent_id="agent_2"
        )

    def test_create_listing(self):
        url = reverse('listing-list')
        data = {
            "title": "New Villa",
            "price": "25000000.00",
            "property_type": "Villa",
            "bedrooms": 4,
            "latitude": 6.4654,
            "longitude": 3.4064,
            "agent_id": "agent_3"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PropertyListing.objects.count(), 3)

    def test_get_listings(self):
        url = reverse('listing-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_filter_listings_by_price(self):
        url = reverse('listing-list')
        response = self.client.get(url, {'price__lte': 10000000})
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], "Lagos Apartment")

    def test_filter_listings_by_location(self):
        url = reverse('listing-list')
        response = self.client.get(url, {'lat': 6.5, 'lng': 3.3, 'radius': 50})
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], "Lagos Apartment")

import math
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend
from .models import PropertyListing
from .serializers import PropertyListingSerializer

def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371.0
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    return R * c

class PropertyListingViewSet(viewsets.ModelViewSet):
    queryset = PropertyListing.objects.all().order_by('-created_at')
    serializer_class = PropertyListingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'property_type': ['exact', 'icontains'],
        'price': ['gte', 'lte'],
        'bedrooms': ['exact', 'gte'],
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        
        lat = self.request.query_params.get('lat')
        lng = self.request.query_params.get('lng')
        radius = self.request.query_params.get('radius')
        
        if lat and lng and radius:
            try:
                lat = float(lat)
                lng = float(lng)
                radius = float(radius)
                
                filtered_ids = []
                for listing in queryset:
                    distance = haversine_distance(lat, lng, listing.latitude, listing.longitude)
                    if distance <= radius:
                        filtered_ids.append(listing.id)
                
                queryset = queryset.filter(id__in=filtered_ids)
            except ValueError:
                raise ValidationError({"error": "lat, lng, and radius must be valid numbers."})
                
        return queryset

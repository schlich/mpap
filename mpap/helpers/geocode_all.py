from data.models import Complaint
import geocoder, time
from django.contrib.gis.geos import Point

queryset = Complaint.objects.all()

for complaint in queryset:
    g = geocoder.google(complaint.location + ', St Louis, MO')
    latlong = g.latlng
    complaint.latlng = Point([latlong[1], latlong[0]])
    print(complaint.latlng)
    complaint.save()
    time.sleep(1)
from django.contrib.gis.db import models

class Officer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=300)
    DSN = models.IntegerField(primary_key=True)
    rank = models.CharField(max_length=200)

    def __str__(self):
        return (str(self.DSN) + ' - ' + self.first_name + ' ' + self.last_name)

class Complaint(models.Model):
    from django.contrib.gis.geos import Point

    file_no = models.CharField(max_length=200, primary_key=True)
    officer = models.ForeignKey(Officer, on_delete=models.CASCADE)
    district = models.CharField(max_length=100)
    complaint_nature = models.CharField(max_length=10000)
    complaint_text = models.CharField(max_length=10000)
    date = models.DateField()
    location = models.CharField(max_length=200)
    latlng = models.PointField()
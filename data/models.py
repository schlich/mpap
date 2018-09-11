from django.db import models

class Officer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    DSN = models.IntegerField()
    rank = models.CharField(max_length=20)

    def __str__(self):
        return (self.first_name + ' ' + self.last_name + '(' + DSN + ')')

class Complaint(models.Model):
    officer = models.ForeignKey(Officer, on_delete=models.CASCADE)
    complaint_text = models.CharField(max_length=1000)
    complaint_date = models.DateTimeField()

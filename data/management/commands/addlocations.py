from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    def handle(self,*args,**options):
        """import tablib
        from import_export import resources
        from data.models import Officer
        from data.models import Complaint
        from data.admin import OfficerResource
        from data.admin import ComplaintResource

        #complaint_resource = ComplaintResource()
        officer_resource = OfficerResource()

        dataset = tablib.Dataset()
        dataset.csv = open('old_officers.csv').read()
        #dataset.headers = ['file_no','DSN','date','district','complaint_nature','complaint_text']
        dataset.headers = ['DSN']

        result = officer_resource.import_data(dataset,dry_run=True)
        
 """

        import csv
        from data.models import Officer, Complaint
        with open('LEO_july_6.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                file_no = row[0]
                location = row[18]
                district = row[3]
                complaint_nature = row[4]
                complaint_text = row[5]
                if Complaint.objects.filter(file_no=file_no).count()!=0:
                    Complaint.objects.filter(file_no=file_no).update(location=location)
                    



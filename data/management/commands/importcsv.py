from django.core.management.base import BaseCommand, CommandError
from data.models import Complaint
from data.models import Officer

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
        with open('complaints_simplified_v2.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                file_no = row[0]

                DSN = row[1]
                date = row[2].split('/')
                print(date)
                date = '20' + date[2] + '-' + date[0] + '-' + date[1]
                print(date)
                district = row[3]
                complaint_nature = row[4]
                complaint_text = row[5]
                if Complaint.objects.filter(file_no=file_no).count()==0:
                    try:
                        DSN = int(DSN)
                        if not Officer.objects.filter(DSN=DSN).exists():
                            officer = Officer(DSN=DSN)
                            officer.save()
                            print(officer)
                        else:
                            officer = Officer.objects.get(DSN=DSN)
                            print(officer)
                        complaint = Complaint(file_no=file_no,officer=officer,date=date,district=district,complaint_nature=complaint_nature,complaint_text=complaint_text)
                        complaint.save()
                    except:
                        complaint = Complaint(file_no=file_no,date=date,district=district,complaint_nature=complaint_nature,complaint_text=complaint_text)
                        complaint.save()



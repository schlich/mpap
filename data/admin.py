from django.contrib.gis import admin
from django import forms
from searchableselect.widgets import SearchableSelect
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from data.models import Officer, Complaint

admin.site.register(Officer)
admin.site.register(Complaint, admin.GeoModelAdmin)

class OfficerResource(resources.ModelResource):

    class Meta:
        model = Officer
        import_id_fields = ('DSN')

class ComplaintResource(resources.ModelResource):
    officer = fields.Field(
        column_name='DSN',
        attribute='DSN',
        widget=ForeignKeyWidget(Officer,'DSN')
    )

    class Meta:
        model = Complaint
        fields = ('file_no','officer','date','district','complaint_nature','complaint_text')
        import_id_fields = ('file_no',)

'''class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        exclude = ()
        widgets = {
            'officer': SearchableSelect(model='data.Officer',search_field='DSN',many=False)
        }

class ComplaintAdmin(admin.ModelAdmin):
    form = ComplaintForm

admin.site.register(Complaint,ComplaintAdmin) '''
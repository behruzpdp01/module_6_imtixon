import csv
import io
from typing import io
from django.forms import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.shortcuts import redirect ,render
from django.urls import path
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from apps.models import Employee


# Register your models here.
class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    change_list_template = "admin/change_list.html"
    list_display = ['id', 'title']

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            decoded_file = csv_file.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)
            reader = csv.reader(io_string)
            next(reader)
            result = []
            for row in reader:
                result.append(Employee(
                    pk=int(row[0]),
                    title=row[1],
                    image=row[2],
                    description=row[3],
                    quantity=row[4],
                    price=row[5]
                ))

            Employee.objects.bulk_create(result)
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(request, "apps/csv_form.html", payload)





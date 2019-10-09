from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse
from .forms import TrialBalanceForm
from .models import TrialBalanceFile
from django.conf import settings
import csv
import xlrd
import os
# Create your views here.


def index(request):
    if request.method == 'POST':
        form = TrialBalanceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            path = os.path.join(settings.MEDIA_ROOT, request.FILES['document'].name.replace(" ", "_"))
            f = xlrd.open_workbook(path)
            for sheet in f.sheets():
                row = sheet.row_slice(0)
                print(row[0].value)
            return HttpResponse('<h1>Success</h1>')
    else:
        form = TrialBalanceForm()
    return render(request, 'mainpage/uploadForm.html', {
        'form': form
    })

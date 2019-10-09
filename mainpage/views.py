from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse
from .forms import TrialBalanceForm
from .models import TrialBalance
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
                for rowindex in range(1,sheet.nrows):
                    row = sheet.row_slice(rowindex)
                    entry = TrialBalance(
                        accountNumber = row[0].value,
                        account = row[1].value,
                        AssetType = row[2].value,
                        accountSubType = row[3].value,
                        accountClass = row[4].value,
                        accountSubClass = row[5].value,
                        beginningBalance = float(row[6].value),
                        endingBalance = float(row[7].value),
                    )
                    entry.save();

            return HttpResponse('<h1>File uploaded under media folder in project directory</h1>')
    else:
        form = TrialBalanceForm()
    return render(request, 'mainpage/uploadForm.html', {
        'form': form
    })

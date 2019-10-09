from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse
from .forms import TrialBalanceForm
from .models import TrialBalanceFile
from django.conf import settings
import xlrd
import os
# Create your views here.


def index(request):
    if request.method == 'POST':
        form = TrialBalanceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            path = settings.MEDIA_ROOT + '\\' + request.FILES['document'].name
            print(path)
            f = xlrd.open_workbook(path)
            return HttpResponse('<h1>Success</h1>')
    else:
        form = TrialBalanceForm()
    return render(request, 'mainpage/uploadForm.html', {
        'form': form
    })

from django.shortcuts import render

# Create your views here.
import json

from django.http import HttpResponse, Http404
from django.shortcuts import render

from arkapp.models import Minter, Ark


def minters_list(request):
    minters = [str(m) for m in Minter.objects.all()]
    return HttpResponse(json.dumps(minters))

def arks_list(request):
    arks = [str(a) for a in Ark.objects.all()]
    return HttpResponse(json.dumps(arks))

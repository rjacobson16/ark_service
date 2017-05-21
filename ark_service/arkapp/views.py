from django.shortcuts import render, get_object_or_404

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

def mint(request, minter_id, qty):
	minter = get_object_or_404(Minter, pk=minter_id)
	return HttpResponse(minter.mint(qty=int(qty)))

def bind(request, key, url):
	ark = get_object_or_404(Ark, key=key)
	ark.url = url
	ark.save()
	return HttpResponse(ark)

def resolve(request, key):
	ark=get_object_or_404(Ark, key=key)
	return HttpResponseRedirect(ark.url)



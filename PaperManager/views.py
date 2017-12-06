from django.shortcuts import render
from django.http import JsonResponse, FileResponse
from django.core import serializers
import json

def getjs(request):
    return FileResponse(open('frontend/dist/2826b73b13025c06cdf2.worker.js', 'r').read())

def test(request):
    return FileResponse(open('/home/codergwy/a.py', 'r').read())

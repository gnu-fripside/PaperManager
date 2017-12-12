from django.shortcuts import render
from django.http import JsonResponse, FileResponse
from django.core import serializers
import json

def getjs(request):
    return None # FileResponse(open('frontend/dist/4bc84e4f3c7fa58a3e6e.worker.js', 'r').read())

def test(request):
    return FileResponse(open('/home/codergwy/a.py', 'r').read())

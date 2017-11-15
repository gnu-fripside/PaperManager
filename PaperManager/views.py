from django.shortcuts import render
from django.http import JsonResponse, FileResponse
from django.core import serializers
import json

def getjs(request):
    return FileResponse(open('/home/codergwy/project/PaperManager/frontend/dist/3c6d3132839126b91aea.worker.js', 'r').read())

def test(request):
    return FileResponse(open('/home/codergwy/a.py', 'r').read())

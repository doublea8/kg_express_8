import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import SubCategory


def get_subcategories(request):
    id = request.GET.get('id', '')
    result = list(SubCategory.objects.filter(
        category_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")

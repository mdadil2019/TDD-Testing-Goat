from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page(request):
    return render(request,'home.html',{'item_text_data': request.POST.get('item_text','')})

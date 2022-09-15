from django.shortcuts import render

# Create your views here.
def bankDetails (request):
    return render(request, 'api/bankdetails.html', {})
from django.shortcuts import render

def handler404(request):
    return render(request, 'page_404.html', status=404)
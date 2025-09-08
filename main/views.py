from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'Kick&Goal', 
        'name': 'Fairuz Akhtar Randrasyah',
        'npm': '2406403955',
        'class': 'PBP D'
    }
    return render(request, "main.html", context)

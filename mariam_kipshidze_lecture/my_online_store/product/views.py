from django.shortcuts import render

def personal_info(request):

    return render(request, 'personal_info.html', context={
        "name": "მარიამი",
        "last_name": "ყიფშიძე",
        "age": 24,
        "favorite_colors": ["red", "blue"]
    })

def check_age(request):
    return render(request, 'check_age.html', context={
        "age": 16,
    })

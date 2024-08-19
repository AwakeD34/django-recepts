from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    
}


def start(request):
    return render (request, 'calculator/start.html')


def omlet(request):
    context = {'recipe': DATA['omlet']}
    return render(request, 'calculator/index.html', context)


def pasta(request):
    context = {'recipe': DATA['pasta']}
    return render(request, 'calculator/index.html', context)


def buter(request):
    context = {'recipe': DATA['buter']}
    return render(request, 'calculator/index.html', context)

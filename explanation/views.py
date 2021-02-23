from django.shortcuts import render
from .models import Explanation


def explanation_view(request):
    explanations = Explanation.objects.all()
    context = {
        'explanations': explanations
    }
    return render(request, 'explanation.html', context)

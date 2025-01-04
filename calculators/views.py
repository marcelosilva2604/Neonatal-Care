from django.shortcuts import render

def home(request):
    """Renderiza a página inicial."""
    return render(request, 'calculators/index.html')
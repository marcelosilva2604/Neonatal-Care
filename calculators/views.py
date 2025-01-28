from django.shortcuts import render

def home(request):
    """Renderiza a página inicial."""
    return render(request, 'calculators/index.html')

def bilirubin_calculator(request):
    return render(request, 'calculators/bilirubin.html')

def medications_calculator(request):
    return render(request, 'calculators/medications.html')

def fluid_balance_calculator(request):
    return render(request, 'calculators/fluid_balance.html')

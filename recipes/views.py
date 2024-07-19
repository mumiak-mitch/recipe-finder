from django.shortcuts import render
from .utils import fetch_recipes

def search_recipes(request):
    query = request.GET.get('q')
    if query:
        results = fetch_recipes(query)
        #print(f"Results: {results}") #for debugging
    else:
        results = {}
    return render(request, 'results.html', {'results': results})

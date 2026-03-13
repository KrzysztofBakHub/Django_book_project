from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def book_search(request):
    book = request.GET.get("book") or 'EMPTY'
    return render(request, 'book_search.html', {'book_name': book})
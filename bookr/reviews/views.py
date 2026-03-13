from django.shortcuts import render

def book_search(request):
    book = request.GET.get("book") or 'EMPTY'
    return render(request, 'book_search.html', {'book_name': book})

def welcome(request):
    return render(request, 'base.html')
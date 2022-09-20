from django.shortcuts import render
from django.http import HttpResponse
from pprint import pprint as pp
import requests
from django.http import JsonResponse
# Create your views here.


def welcome(request):
    #pp(request)
    msg = "<h2>Welcome to book catalogue details</h2>"
    return HttpResponse(msg)#, content_type='text/plain')

def extract_book_details(request):
    search_details = dict(request.GET)
    book_id = search_details['search'][0]
    
    
    base_url = "https://www.googleapis.com/books/v1/volumes"#?q=isbn:9781449372620
    param_q = {'q' : f'isbn:{book_id}'}
    
    r = requests.get(url = base_url, params = param_q)
    
    raw_data = r.json()
    
    try :
        book_items = raw_data['items'][0]
        title = book_items['volumeInfo']['title']
        authors = ", ".join(book_items['volumeInfo']['authors'])
        page_count = book_items['volumeInfo']['pageCount']
        avg_rating = book_items['volumeInfo']['maturityRating']
        
        data = {'isbn' : book_id,
            'title' : title,
            'authors' : authors,
            'page_count' : page_count,
            'avg_rating' : avg_rating}
    
        return render(request,'display_book_details.html', data)
    
    
    except :
        data = {'isbn' : book_id}
        return render(request,'display_error.html', data)
    
    
    

from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(
        request,
        'home.html',
        {
            'new_item_text': request.POST.get('item_text', ''), # default value '' in case of normal GET request => so the POST dictionary is empty
        } 
    )

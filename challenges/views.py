from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
# def january(request):
#     return HttpResponse('Eat no meat for the entire month!')

# def february(request):
#     return HttpResponse('walk for at least 20 minutes everyday!')


# def march(request):
#     return HttpResponse('learn Django for at least 20 minutes everyday!')


monthly_challenges = {
    "january": "Contribute to an open source project",
    "february": "Build a personal website",
    "march": "Learn a new programming language",
    "april": "Participate in a coding competition",
    "may": "Automate a daily task",
    "june": "Read a book about algorithms",
    "july": "Create a mobile application",
    "august": "Improve your testing skills",
    "september": "Learn about cloud computing",
    "october": "Participate in Hacktoberfest",
    "november": "Learn a new database technology",
    "december": "Review and refactor an old project"
}

def monthly_challenge_by_number(request, month):
    months =list(monthly_challenges.keys())
    if month> len(months):
        return HttpResponseNotFound('Invalid month')
    redirect_month = months[month-1]
    redirect_path = reverse('month-challenge', args =[redirect_month])
    return HttpResponseRedirect(redirect_path)
    



def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
    
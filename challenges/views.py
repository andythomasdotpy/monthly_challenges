from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

monthly_challenges = {
    "january": "Hi, I'm January!",
    "february": "Hi, I'm February!",
    "march": "Hi, I'm March!",
    "april": "Hi, I'm April!",
    "may": "Hi, I'm May!",
    "june": "Hi, I'm June!",
    "july": "Hi, I'm July!",
    "august": "Hi, I'm August!",
    "september": "Hi, I'm September!",
    "october": "Hi, I'm October!",
    "november": "Hi, I'm November!",
    "december": "Hi, I'm December!",
}

# Create your views here.


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Hi, I'm January!"
    elif month == "february":
        challenge_text = "Hi, I'm February!"
    elif month == "march":
        challenge_text = "Hi, I'm March!"
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)
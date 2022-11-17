from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{month.capitalize()}</a></li>"

    months_list = f"""
        <ul>
            {list_items}
        </ul>
    """

    return HttpResponse(months_list)


def monthly_challenge_by_number(request, month):
    try:
        monthly_keys_list = list(monthly_challenges.keys())
        redirect_month_name = monthly_keys_list[month - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month_name])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("Sorry, month not found.")


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>Can't find that month</h1>")

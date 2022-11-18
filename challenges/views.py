from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december": None,
}

# Create your views here.


def index(request):
    months = list(monthly_challenges.keys())

    for month in monthly_challenges:
        print(monthly_challenges[month])

    def sum():
        return 1 + 5

    return render(request, "challenges/index.html", {
        "months": monthly_challenges,
        "sum": sum
        })


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
        # response_data = render_to_string("challenges/challenge.html", {"challenge_text": challenge_text})
        # return HttpResponse(response_data)
        return render(request, "challenges/challenge.html", {
            "text":challenge_text,
            "month": month, 
            })
    except:
        
        # response_data = render_to_string("404_error.html")
        # return HttpResponseNotFound(response_data)
        raise Http404("404.html")

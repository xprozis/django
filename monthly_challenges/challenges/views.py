from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
# Create your views here.

monthly_challenges = {
    "january": "janeiro",
    "february": "fevreiro",
    "march": "march",
    "april": "april",
    "may": "may"
}

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month < 1:
        month = 1
    if month > 5:
        month = 5
    redirect_month = months[month-1]
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except: 
        return HttpResponseNotFound("Nao foi encontrado")
   
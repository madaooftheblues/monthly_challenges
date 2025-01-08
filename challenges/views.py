from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    'january': 'initiate ascendence',
    'february': 'master the art of client hunting',
    'march': 'hunt clients and execute projects',
    'april': 'get monei from the clients',
    'may': 'get more clients',
    'june': 'try to scale up',
    'july': 'learn ai development and scale up',
    'august': 'make connections and initiate company',
    'september': 'hire people and hand them projects',
    'october': 'rinse and repeat',
    'november': 'rinse and repeat',
    'december': 'reflect and improve'
}

# Create your views here.


def monthly_challenge(request, month):
    try:
        response = monthly_challenges[month]
        return HttpResponse(response)
    except:
        return HttpResponseNotFound("Woops, month does not exits.")


def monthly_challenge_by_number(request, month):
    if len(monthly_challenges) < month or month < 1:
        return HttpResponseNotFound('Woops, month does not exist.')

    months = list(monthly_challenges.keys())
    redirect_month = months[month - 1]
    redirect_url = reverse("month-url", args=[redirect_month])

    return HttpResponseRedirect(redirect_url)


def get_months_list(request):
    out = "<div>"
    out += "<h1>Monthly Challenges</h1>"
    out += "<ul>"
    months_list = [f'<li><a href="{reverse("month-url", args=[month])}">{month}</a></li>' for month in list(
        monthly_challenges.keys())]
    out += "".join(months_list)
    out += "</ul>"
    out += "</div>"

    return HttpResponse(out)

from turtle import forward
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


monthly_challenges = {
    "january" : "Eat no meat!",
    "february" : "Walk for 20 mins every day!",
    "march" : "Learn English!",
    "april" : "Read a book!",
    "may" : "Learn Django!",
    "june" : "Consume no sugar!",
    "july" : "Learn HTML!",
    "august" : "drink no alcohol!",
    "september" : "Walk instead of Driving!",
    "october" : "Tell no lies!",
    "november" : "Face your fears!",
    "december" : "Listen to music!"
}

def monthly_challenge_by_number(request, month_index):
    months = list(monthly_challenges.keys())
    if month_index > len(monthly_challenges):
        return HttpResponseNotFound("Invalid month!")
    forward_month = months[month_index-1]
    return HttpResponseRedirect(f"/challenges/{forward_month}")

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(f"<h1>{month} : {challenge_text}</h1>")
    except:
        return HttpResponseNotFound(f"<h2>{month} is not supported!</h2>")
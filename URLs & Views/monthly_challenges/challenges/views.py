from django.shortcuts import render
from django.http import HttpResponse


monthly_challenges={
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

def monthly_challenge_by_number(request, month):
    return HttpResponse()

def monthly_challenge(request, month):
    return HttpResponse(f"{month}")
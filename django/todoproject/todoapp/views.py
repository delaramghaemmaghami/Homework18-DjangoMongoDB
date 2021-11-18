from django.shortcuts import render


def welcome_page(requests):
    return render(requests, "welcome.html")

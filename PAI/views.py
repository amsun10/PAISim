from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("Welcome To USE PAI Simulator")


def get_heart_rate(request):
    return HttpResponse(status=204)
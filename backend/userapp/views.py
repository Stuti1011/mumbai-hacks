from django.shortcuts import render

def index(request):
    return render(request, "index.html")
import google.generativeai as genai
from django.conf import settings

genai.configure(api_key=settings.GOOGLE_API_KEY)

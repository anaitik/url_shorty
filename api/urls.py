
from django.urls import path
from .views import api_doc, send_api, short_generate
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('shorten/', csrf_exempt(short_generate), name="shorten"),
    path('send-api-key/', csrf_exempt(send_api), name="send_api"),
    path('doc/', api_doc, name='api_doc')
]

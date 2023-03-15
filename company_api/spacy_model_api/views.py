from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import glob
# Create your views here.

FILE_NAME_SPACY_MODEL = "en_core_web_lg-3.4.1-py3-none-any.whl"

#  Jainesh, here you can just put the path in the server, then django launches the server much faster,
#  the bellow code only for automatic searching of the file in the C disc (if server works on Windows)
MODEL_PATH = glob.glob(f'C://**/{FILE_NAME_SPACY_MODEL}', recursive=True)[0]

api_dict = {"path": MODEL_PATH}


@api_view(["GET"])
def download_from(request):
    return Response(api_dict)

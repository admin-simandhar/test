from django.shortcuts import render
import hashlib
# Create your views here.
def getHashSha256(data):
    try:
        return hashlib.sha256(data.encode()).hexdigest()
    except:
        raise 
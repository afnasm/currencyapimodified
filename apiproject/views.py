from django.shortcuts import render
import requests,json


def currency(request):
    api = requests.get("https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,EOS&tsyms=USD&api_key=b2d716d554efca9694a866580a89aa65df08f74f478a46f62c6a8c050e3af6cf")
    api= json.loads(api.content)
    return render(request,'index.html',{'api':api})

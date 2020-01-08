from django.shortcuts import render
import requests

def index(request):
    if "ad" in request.GET:
      try:
        url1=request.GET["ad"]
        stream = url1.split("watch?v=")[1].replace('"',"")
        url = "https://ytextract.p.rapidapi.com/json/mp3/"+stream
        headers = {
            'x-rapidapi-host': "ytextract.p.rapidapi.com",
            'x-rapidapi-key': "529e3f03c0msh06af56ae5d4985dp153eeejsna77eac11e459"
        }

        response = requests.request("GET", url, headers=headers)
        baslik=[]
        resim=[]
        sure=[]
        d_link=[]
        boyut=[]
        format=[]

        for i in response.json()["vidInfo"]:
            for j in i:
                baslik.append(response.json()["vidTitle"])
                resim.append(response.json()["vidThumb"])
                sure.append(str(round(response.json()["duration"]/60, 2)) + " minutes")
                d_link.append(response.json()["vidInfo"][j]["dloadUrl"])
                boyut.append(response.json()["vidInfo"][j]["mp3size"])
                format.append(response.json()["vidInfo"][j]["bitrate"])
        return render(request, "sonuc.html", {"format":format,"baslik": baslik, "resim": resim, "sure": sure,"d_link":d_link,"boyut":boyut})
      except:
          return render(request,"hata.html")
    else:
        return render(request, "index.html")


def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
import json
import requests

print("Döviz Çevirme".center(50,"="))
bozdurulanDoviz = input("Bozdurulan döviz türü: ")
alinandoviz = input("Alınacak döviz türü: ")
cevrilenpara = input("Para miktarı: ")

doviz = requests.get("https://api.exchangeratesapi.io/latest" + "?base=" + bozdurulanDoviz)

with open("dovizler.json","w") as f:
    data = doviz.text
    f.write(data)

with open("dovizler.json", "r") as f:
    x = f.read()
    datadict = json.loads(x)
    oran = datadict["rates"][alinandoviz]

tarih = datadict["date"]
tarih = tarih.split("-")
tarih = tarih[2] + "/" + tarih[1] + "/"+ tarih[0] 

print("Döviz bilgilerinin tarihi: " +  tarih)
print("1 "+bozdurulanDoviz + " = " + str(oran) + " " + alinandoviz)
print(cevrilenpara + " " + bozdurulanDoviz + " = " + str(int(cevrilenpara)*oran) + " " + alinandoviz)
    
input("Çıkmak için enter tuşuna basınız...")

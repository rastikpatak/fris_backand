import requests

url = "https://boozeapi.com/api/v1/cocktails"
params = {
"search": "Blind Russian"
}

response = requests.get(url)


if response.status_code != 200:
    print("Chyba:", response.status_code)
    exit()

meno = []
obr = []
data = response.json()
#print(data)
def vyhladaj_typ(typ, alkohol=None):
    pocet = 0
    for a in data['data']:
        for b in a["ingredients"]:
            #print(a)
            #print(b["type"])
            if  alkohol == b["contains_alcohol"] or alkohol == None and b["type"] == typ:
                #print(b["name"]) 
                meno.append(b["name"])
                
                #print(b["image"])
                obr.append(b["image"])
                pocet +=1
    #print(f"Pocet {typ} v receptoch: {pocet}")
vyhladaj_typ("Liqueur")
vyhladaj_typ("Rum")
#vyhladaj_typ("Vodka")
#vyhladaj_typ("Gin")
#print (meno)
#print (obr)

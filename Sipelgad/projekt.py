# autorid: Sheila Kalde ja Markus Tavel

# Ülesanne: Sipelgakoloonial on suur mure. Pidevalt tuleb juurde uusi beebisipelgaid, aga nad ei taha, et kellelegi satuks sama nimi.
# Sipelgakoloonia tahab nimede andmebaasi, kus on võimalus nimesid juurde lisada ning kontrollida kas mingi nimi on juba olemas.

# avame faili kus asuvad juba olemasolevad nimed
fail = open("sipelgad.txt", encoding="UTF-8")
nimed = [] #loome massiivi kuhu nimed sisse lugeda
for rida in fail: # loeme ühekaupa nimed massiivi
        rida = rida.strip("\n")
        nimed.append(rida)
fail.close() # sulgeme faili

# funktsioon võtab paramteerina sõne tüüpi muutuja
def korrasta(nimi):
    # saadud sõnes muudetakse kõik tähed väikesteks tähtedeks
    # ning esimene täht tehakse suureks
    nimi = nimi.lower()
    nimi = nimi.title()
    return nimi # funktsioon tagastab korrastatud sõne/nime
   
while True:
    # iga tsükli alguses kuvatakse valikud ja küsitakse kasutajalt mida ta soovib teha
    valik = input("Nimekirja lisamiseks vajuta Y, nimekirja vaatamiseks N, muu sisendi korral programm lõpetab töö. ") #eeldame et kasutaja sisestab õigesti
    # kui kasutaja sisestab n või N väljastatakse for tsükliga terve nimekiri 
    if valik.upper() == "N": # kasutatud upper meetodit et juhul kui sisestatakse väike täht ei lõpeta programm tööd
        for i in nimed:
            print(i)
    
    # kui kasutaja sisestab y või Y küsitakse kasutajalt nime
    elif valik.upper() == 'Y': #see on selleks kui kasutaja sisestab väikesed tähed
        nimi = input("Sisestage nimi: ")
        nimi = korrasta(nimi) # korrastakse sisestatud nimi
        if nimi in nimed: # kui nimi on juba nimekirjas olemas teavitatakse sellest kasutajat
            print("See nimi on juba valitud. Vali midagi muud")
            continue # kui nimi on juba olemas liigub programm tagasi tsükli algusesse
        nimed.append(nimi) # kui nime ei asu nimekirjas lisatakse see nimekirja
        print("Nimi", nimi, "on edukalt nimekirja lisatud!")
        
    else: # muu sisendi korral murrab break tsüklist välja
        print("Sulgen programmi. Ilusat kasvatamist!")
        break

# avatakse uuesti fail ja kirjutatakse muudetud nimekiri eelmisest üle
fail = open("sipelgad.txt","w",encoding = "UTF-8")
for i in nimed:
    fail.write(i + "\n")
    
fail.close() # fail sulgeb ja programm lõpetab töö

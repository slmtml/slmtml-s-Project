import time
yo = {
"LOL":"komik bir şeye verilen cevap",
"CRINGE":"garip ya da utandırıcı bir şey",  
"ROFL":"bir şakaya karşılık cevap",
"SHEESH":"onaylamamak",
"CREEPY":"korkunç",
"AGGRO":"agresifleşmek/sinirlenmek"
}
soru="a"
ogrenilenler=[]
for i in yo.keys():
    print(i)
while len(ogrenilenler)!=len(yo):
    time.sleep(0.5)
    soru=input("\n"+"Bİlmediğiniz kelimeyi yazın --> ").upper()
    time.sleep(0.5)
    for i in yo.keys() :
        if soru in i:
            print(yo[i])
            ogrenilenler.append(i)
                

    if soru not in yo:
        print("Böyle bir kelime mevcut değil")
        
print("\n"+"Tebrikler bütün kelimeleri öğrendin.")

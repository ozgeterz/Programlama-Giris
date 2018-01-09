#!usr/bin/python3
# _*_ coding: utf-8 _*_
# 19-24 yaş arası kadın-erkek yetişkinler için vücut kitle endeksi hesaplayan program

k=int(input("kilonuzu giriniz(kg):"))
b=float(input("boyunuzu giriniz(m):"))
endeks=k/b**2

if 20.0<endeks<24.9:
    print(endeks,"normal kilodasınız")
    
elif 25.0<endeks<29.9:
    print(endeks,"hafif şişmansınız")
    
elif 30.0<endeks<34.9:
    print(endeks,"şişmansınız")
    
elif 35.0<endeks<44.9:
    print(endeks,"kilonuza dikkat etmelisiniz")
    
elif 45.0<endeks<49.9:
    print(endeks,"aşırı şişmansınız")
    
elif endeks>50.0:
    print(endeks,"ölümcül seviyedesiniz")
    
    

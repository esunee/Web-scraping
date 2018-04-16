import os
import requests
import csv
import argparse
from datetime import datetime
from datetime import timedelta
from bs4 import BeautifulSoup
import requests
import pandas as pd


def queryLoto(combinacion):
    
    MAX_PAGES = 4
    counter = 0
        
    for i in range(0, MAX_PAGES):
        
        # Construyo la URL
        if i == 1:
            url = "https://www.loteriasyapuestas.es/es/la-primitiva/sorteos/2018/1015004030"
        if i == 2:
            url = 'https://www.loteriasyapuestas.es/es/la-primitiva/sorteos/2018/1014804029'
        if i == 3:
            url = "https://www.loteriasyapuestas.es/es/la-primitiva/sorteos/2018/1014304028"         
        if i == 4:
            url = "https://www.loteriasyapuestas.es/es/la-primitiva/sorteos/2018/1014104027"
       
        # Realizamos la petición a la web
        req = requests.get(url)
        # Comprobamos que la petición nos devuelve un Status Code = 200
    
        soup = BeautifulSoup(req.text, "html.parser")
    
        combinacion = []   
        table=soup.find('table',{'summary' : 'Tabla Detalle - La Primitiva'});
        
        for row in table.findAll("tr"):
           cells = row.findAll('td')   
           if len(cells)==3:
               premio=cells[0].find(text=True)
               acertantes=cells[1].find(text=True)
               dinero=cells[2].find(text=True)
                    
                         
           break   
        for re in soup.find_all('div', {'class': 'cuerpoRegionMed'}):
            reinte = re.find('span', {'class': 'bolaPeq'}).getText()
            
            break
        for co in soup.find_all('div', {'class': 'cuerpoRegionDerecha'}):
            comple = co.find('span', {'class': 'bolaPeq'}).getText()
            break    
        for combi in soup.find_all('ul', {'id': 'mainNumbers'}):
            litag = combi.find_all('li')
            if len(litag)==6: 
                c1=litag[0].find(text=True)
                c2=litag[1].find(text=True)
                c3=litag[2].find(text=True)
                c4=litag[3].find(text=True)
                c5=litag[4].find(text=True)
                c6=litag[5].find(text=True)
                combinacion.append((c1,c2,c3,c4,c5,c6,reinte,comple,premio,acertantes,dinero))
    
            
            break
    return

    #for ant in soup.find_all('div', {'class': 'contenedorEnlaces'}):
       # for ante in ant.find_all('div', {'class': 'resultadoAnterior'}):
         #   print (ante['href'])
LotoList=[]
headerList=['c1','c2','c3','c4','c5','c6','Reintegro','Complementario','premio','acertantes','dinero']
LotoList.append(headerList)
        


queryLoto(LotoList)

print (LotoList)
  
with open("Primitiva.csv", 'w', newline='') as csvFile:
  writer = csv.writer(csvFile)
  for sorteo in LotoList:
    writer.writerow(sorteo)
        
#df= pd.DataFrame(combinacion, columns=['c1','c2','c3','c4','c5','c6','Reintegro','Complementario','premio','acertantes','dinero'])
#df.to_csv('Primitiva.csv',index=False, encoding='utf-8')    
      

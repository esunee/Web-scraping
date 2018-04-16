
Práctica 1: Web scraping
En esta practica nos ha faltado poder extraer la url del sorteo anterior:

    for ant in soup.find_all('div', {'class': 'contenedorEnlaces'}):
        for ante in ant.find_all('div', {'class': 'resultadoAnterior'}):
            print (ante['href'])

Con esta url que iría variando cada vez que entras en la anterior podríamos extraer todos los sorteos que quisieramos, mi intención era poder extraer un mes, que en este caso sería repetir el scraping 8 veces.

Tambíen me ha faltado poder ir añadiendo los sorteos anteriores al fichero, con el siguiente código solo podia extraer el primer sorteo.

df= pd.DataFrame(combinacion, columns=['c1','c2','c3','c4','c5','c6','Reintegro','Complementario','premio','acertantes','dinero'])
df.to_csv('Primitiva.csv',index=False, encoding='utf-8')

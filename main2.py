#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Se importa el archivo .csv a utilizar asi como las librerias a usar
import csv
from IPython.display import clear_output
import time


# In[2]:


# Se hace una copia de la información original para porder modificarla 
copia1 = [] 
with open('synergy_logistics_database.csv', 'r') as logistica_completa1:
    documento = csv.reader(logistica_completa1)
    r = 0
    for fila in documento:
        if r == 0:
            r += 1
        else:
            copia1.append(fila)


# In[3]:


# En esta parte se extrae solo las exportaciones de el archivo copia y se ordenan de mayor a menor de acuerdo a su demanda 
#Exportaciones 

def mejores_exportaciones():
    rutas1 = [] 
    repeticion1 = 0 
    ingreso1 = 0
    rutas_repeticion = [] 
    exportaciones = "Exports"
    
    for ruta1 in copia1:
        circuito1  = [ruta1[2],ruta1[3]]
        if ruta1[1] == exportaciones and circuito1 not in rutas_repeticion:
            for corrida1 in copia1:
                if circuito1 == [corrida1[2],corrida1[3]] and corrida1[1] == exportaciones:
                    repeticion1 += 1
                    ingreso1 += int(corrida1[9])        
                    rutas_repeticion.append(circuito1)
            lista = [ruta1[2],ruta1[3],repeticion1,ingreso1]
            rutas1.append(lista)
            repeticion1 = 0
            ingreso1 = 0
    
    rutas1.sort(reverse=True,key=lambda x:x[2]) 
    j = 0
    for i in rutas1:
        if j < 10:    
            print(i[0],i[1],i[2])
            j += 1
  


# In[4]:


# Se hace lo mismo que en la seccion anterior solo que ahora se extrae solo los movimientos relacionados con las importaciones 
#importaciones 

def mejores_importaciones():
    rutas1 = [] 
    repeticion1 = 0 
    ingreso1 = 0
    rutas_repeticion = [] 
    importaciones = "Imports"
    
    for ruta1 in copia1:
        circuito1  = [ruta1[2],ruta1[3]]
        if ruta1[1] == importaciones and circuito1 not in rutas_repeticion:
            for corrida1 in copia1:
                if circuito1 == [corrida1[2],corrida1[3]] and corrida1[1] == importaciones:
                    repeticion1 += 1
                    ingreso1 += int(corrida1[9])        
                    rutas_repeticion.append(circuito1)
            lista = [ruta1[2],ruta1[3],repeticion1,ingreso1]
            rutas1.append(lista)
            repeticion1 = 0
            ingreso1 = 0
    
    rutas1.sort(reverse=True,key=lambda x:x[2]) 
    j = 0
    for i in rutas1:
        if j < 10:    
            print(i[0],i[1],i[2])
            j += 1
    


# In[5]:


#mejores_exportaciones()


# In[6]:


#mejores_importaciones()


# In[7]:


# En la tercera seccion, correspondiente al problema 2 se buscan los diferentes tipos de transporte incluyendo a los usdados en las exportaciones y en las importaciones 
def transportes():
    rutas1 = [] 
    repeticion1 = 0 
    ingreso1 = 0
    rutas_repeticion = [] 
    importaciones = "Imports" and "Exports"
    #[copia1[7]]
    
    for ruta1 in copia1:
        circuito1  = [ruta1[7]]
        if ruta1[1] == importaciones and circuito1 not in rutas_repeticion:
            for corrida1 in copia1:
                if circuito1 == [corrida1[7]] and corrida1[1] == importaciones:
                    repeticion1 += 1
                    ingreso1 += int(corrida1[9])        
                    rutas_repeticion.append(circuito1)
            lista = [ruta1[7],repeticion1,ingreso1]
            rutas1.append(lista)
            repeticion1 = 0
            ingreso1 = 0
    
    rutas1.sort(reverse=True,key=lambda x:x[2]) 
    j = 0
    for i in rutas1:
        if j < 10:    
            print(i[0],i[2])
            j += 1
    


# In[8]:


#transportes()


# In[9]:


# En la seccion 4 se resuelve el problema 3 en la cual de la lista copia se extraen los ingresos por pais (importaciones y exportaciones) y despues se le compara con el 100 % de ingreso para obtener su porcentaje dentro del ingreso total y asi saber su participación en la empresa
def movimientos_80 ():
    direccion = "Exports" and "Imports"
    
    valor= 0
    suma= 0
    parcial= 0

    pais_exp_int = []
    corrida5=[]
    lista_porcentaje = []
    for ruta in copia1:
        if direccion==ruta[1]:
            suma=suma+int(ruta[9])
            corrida5.append(ruta)
        if ruta[2] not in pais_exp_int:
            pais_exp_int.append(ruta[2])
    for opcion in pais_exp_int:
        for registro in corrida5:
            if opcion==registro[2]:
                valor=valor+int(registro[9])
        parcial=valor*100
        parcial_t = parcial/suma
        lista_porcentaje.append([opcion,valor,parcial_t])
        valor=0
    lista_porcentaje.sort(reverse = True, key = lambda x:x[1])
    lista_porcentaje[0].append(lista_porcentaje[0][2])
    for p in range(0,len(lista_porcentaje)-1):
        lista_porcentaje[p+1].append(lista_porcentaje[p][3]+lista_porcentaje[p+1][2])
    
    lista_porcentaje.sort(reverse = True, key = lambda x:x[1])
    j = 0
    for i in lista_porcentaje:
        if j < 7:    
            print(i[0],i[3])
            j += 1


# In[10]:


#movimientos_80()


# In[11]:


# En la ultima seccion se hace una interfaz de ususario para presentar los resultados de salida de las secciones anteriores.
elegir=input("Bienvenido al sistema de reportes de 'Synergy Logistics'\n\n¿Desea imprimir el reporte?\nY/N:  ")

if elegir == "Y" or "y":
    clear_output(wait=True)
    print("\n Imprimiendo... espere por favor...")
    time.sleep(5)
    clear_output(wait=True)
    print("Informe Completo\n\n\n")
    print("Mejores 10 rutas para exportaciones:\n")
    mejores_exportaciones()
    print("\n\n Mejores 10 rutas para importaciones\n")
    mejores_importaciones()
    print("\n\n Medios de transporte mas utilizados\n")
    transportes()
    print("\n\n Paises dentro del 80% de ingresos \n")
    movimientos_80()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





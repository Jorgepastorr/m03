### Algoritmica for



**Bucle: Imprimir los informes de 2010 a 2016  
 Ha de quedar:  
 Informe año 2010  
 ...  
 Informe año 2016  
 ejercicio-bucle-informes.py**  
```python
for i in range(2010,2017) :
	print (i)
```

**Bucle: contar desde el número 1 hasta el 50.  
ejercicio-bucle-contar.py**  
```python
for i in range(1,51) :
	print (i)
```


**Bucle: Que cuente del número 1 hasta el límite que yo le diga  
ejercicio-bucle-contar2.py**  
```python
var = input("num: ")
for i in range(1,var+1) :
		print (i)
```


**Bucle: Que cuente del número 1 hasta el límite que yo le diga. Sólo los pares.  
ejercicio-bucle-contar-pares.py**  
```python
var = input("num: ")
for i in range(1,var+1) :
	if i %2==0:
		print (i)
```

**Bucle: sumar desde el número 1 hasta el 5  
Ha de salir por pantalla  
1+2+3+4+5=15  
ejercicio-bucle-sumar.py**  
```python
todo= 0
for i in range(1,6) :
	print (i),"+",
	todo =todo+i

print "=",todo
```
**Bucle: sumar pares desde el número 1 hasta el 5  
Ha de salir por pantalla  
2+4=6   
ejercicio-bucle-sumar.py**
```python
todo= 0
for i in range(1,6) :
	if i %2==0:
		print (i),"+",
		todo =todo+i
print "=",todo
```






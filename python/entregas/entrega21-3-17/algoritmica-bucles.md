### Algoritmica bucles.  
  
#### Bucle 1: Imprimir los informes de 2010 a 2016  
``` python  
anio = 2010
salir = False
while salir == False do
	print anio
	if (anio == 2016 ) then
		salir = True
	eif
	anio = anio +1
ewhile
```    

#### Bucle 2: contar desde el número 1 hasta el 50.  
``` python  
num = 1
salir = False
while salir == False do
	print num
	if ( num == 50 ) then
		salir = True
	eif
	num=num+1
ewhile
```  

#### Bucle 3: Que cuente del número 1 hasta el límite que yo le diga.  
``` python
num = 1
limite = read()
salir = False
while salir == False do 
	print num
	if ( num == limite ) then
		salir = True
	eif
	num=num+1
ewhile
```  
#### Bucle 4.1: Que cuente del número 1 hasta el límite que yo le diga. Sólo los pares.
``` python  
num = 1
limite = read()
salir = False
while salir == False do
	if ( num == %2==0 ) then
		print num
	if ( num == limite ) then
		salir = True
	eif
	num=num+1
ewhile
``` 
#### Bucle 4.2: sumar desde el número 1 hasta el 5. 
``` python
num = 1
salir = False
while salir == False do
	print num
	total= total+num
	if ( num == 5 ) then
		print total
		salir = True
	eif
	num=num+1
ewhile
```  
#### Bucle 5: Lee un número y dice si es primo o no.  
**Al cansarme lo e sacado de internet, ni de coña lo hubiera sacado**
``` python
num = read()
num2 = 2
salir = False
while salir == False do
	 
	if  num%num2==0 then
		print num,"no es primo"
		salir = True
	eif	
		print  num,"es primo"
		salir = True
	
	num2=num2+1

ewhile
```  



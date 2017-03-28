#### Bucles examen.

**1º 1 al 21 cada 7 "yupi"**
```python
num = 1
salir = False
while salir == False do
    print num
    if num%7==0 then
      print "yupi"
    eif
    if num == 21 then
      salir = True
    eif
    num = num+1
ewhile
```
   
**2º extra días de la semana**
```python
num = 1
salir = False
while salir == False do
    if num%7==1 then
        print "L tancat"
    eif
    if num%7==2 then
        print "M"
    eif
    if num%7==3 then
        print "X día espectacular"
    eif
    if num%7==4 then
        print "J día espectacular"
    eif
    if num%7==5 then
        print "V"
    eif
    if num%7==6 then
        print "S sesio golfa"
    eif
    if num%7==0 then
        print "D"
    eif
    if num == 7 then
        salir = True
    eif
    num=num+1
ewhile   
```

**borracho derecha una vuelta**
```python
num= 1
salir = False
while salir == False do
    if num%8==1 or num%8==2 then
        print "arriba"
    eif
    if num%8==3 or num%8==4 then
        print "derecha"
    eif
    if num%8==5 or num%8==6 then
        print "abajo"
    eif
    if num%8==7 or num%8==0 then
        print "izquierda"
    eif
    if num == 8 then
      salir = True
    eif
    num=num+1
ewhile        
```

**muy borracho derecha o izquierda**
```python
dir = read( D o I )
num= 1
salir = False
while salir == False do
    if num%8==1 or num%8==2 then
        print "Arriba"
    eif
    if num%8==3 or num%8==4 then
      if read == D then
          print "derecha"
      else
          print "izquierda"
    eif
    if num%8==5 or num%8==6 then
        print "abajo"
    eif
    if num%8==7 or num%8==0 then
      if read == D then
          print "izquierda"
      else
          print "derecha"
    eif
    if num == 8 then
      salir =True
    eif
    num=num+1
ewhile   
```
**bucle 1-8 paa en la 3ª vuelta**
```python

num= 1
vueltas= 0
salir= False

while salir == False do
    print num
    if num%8==0 then
      vueltas= vueltas+1
    eif
    if vueltas == 3 then
      salir = True
    eif
    
    num=num+1
ewhile    
```

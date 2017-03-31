
**bucle piedra, papel, tijera, del 31-57**

```python
num= 31
salir= False
while salir == False do
	print num,
	
	if num%7==0 or num%7==1 then
		pl1 = "ti"
	eif
	if num%7==2 or num%7==3 or num%7==6 then
		pl1 = "pi"
	eif		
	if num%7==4 or num%7==5 then
		pl1 = "pa"
	eif	
	if num%5==0 or num%5==1 or num%5==2 then
		pl2 = "pa"
	eif	
	if num%5==3 then
		pl2 = "ti"
	eif	
	if num%5==4 then
		pl2 = "pi"
	eif	
	if  pl1 == pl2 then
		print empate
	eif
	if ( pl1 == "pi" and pl2 == "ti" ) or ( pl1 == "pa" and pl2 == "pi" ) or   ( pl1 == "ti" and pl2 == "pa" )then
		print gana pl1
	else:
		print gana pl2
	eif
	if num == 57 then
		salir = True
	eif

	num = num+1
```


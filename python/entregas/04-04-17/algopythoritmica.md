### algo-python-ritmica

**spok**
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
#tirada de jugador
j1 = raw_input("Opciones a elegir: /pa/pi/ti/la/sp ")

#aleatorio maquina
maq = randint(1,5)

if maq == 1 then
	maq = "pa"
fi
if maq == 2 then
	maq = "pi"
fi
if maq == 3 then
	maq = "ti"
fi
if maq == 4 then
	maq = "la"
fi
if maq == 5 then
	maq = "sp"
fi

# de 25 opciones descarto 5 igiales	
if j1 == maq then
	print "Empate"
else
# de 20 opciones descarto 10 que puede ganar j1
	if ( j1 == "pa" and ( maq == "sp" or maq == "pi") or
	   ( j1 == "pi" and ( maq == "ti" or maq == "la") or
	   ( j1 == "ti" and ( maq == "pa" or maq == "la") or
	   ( j1 == "la" and ( maq == "sp" or maq == "pa") or
	   ( j1 == "sp" and ( maq == "pi" or maq == "ti") or
	   )then
		   print "Ganas tu"
	else
	# solo quedan las 10 opciones que ganaria maquina
		print "pierdes"

```

**carta francesa**
```python
import os
os.system('clear')
from random import randint

j1 = randint(1,13)
maq = randint(1,13)
tipo = randint(1,4)

# 11 a 13 de maquina
if maq == 11 then
	maq1 = "J"
fi
if maq == 12 then
	maq1 = "Q"
fi
if maq == 13 then
	maq1 = "K"
fi
# 11 a 13 de jugador
if j1 == 11 then
	j11 = "J"
fi
if j1 == 12 then
	j11 = "Q"
fi
if j1 == 13 then
	j11 = "K"
fi

# define tipos
if tipo == 1 then
	tipo = trebol
fi
if tipo == 2 then
	tipo = picas
fi
if tipo == 3 then
	tipo = corazones
fi
if tipo == 4 then
	tipo = diamantes
fi



if maq == j1 then
	print "¡¡Empate!!"
else
# gana jugador1 si elguna variable es mayor que 10 se l asigna la variable con catacter alfabetico.
	if j1 > maq then
		if j1 > 10 then
			j1 = j11
		fi
		if maq > 10 then
			maq = maq1	
		fi
		print "tu",j1,j11,tipo,"Maquina",maq1,maq,tipo,": ¡¡Ganas tu!!"
	else
		if j1 > 10 then
			j1 = j11
		fi
		if maq > 10 then
			maq = maq1
		fi
		print "tu",j1,j11,tipo,"Maquina",maq1,maq,tipo,": ¡¡Pierdes!!"
```

**cartas con apuestas**

```python

import os
os.system('clear')
from random import randint
credito = 100

salir = False
while salir == False do
	print "Tienes",credito,"€"
	apuesta = input("Cuanto quiere apostar tienes : ")
	os.system('clear')
	
# condicióm de salida apuesta 0 o sin credito
	
	if apuesta == 0 then
		salir = True
	else
	   	if apuesta > credito then
	       		print "¡¡No puedes apostar tanto!!"
			print ""
		else
			if apuesta <= credito then
		
				j1 = randint(1,13)
				maq = randint(1,13)
				tipo = randint(1,4)

				# 11 a 13 de maquina le asigna una letra
				if maq == 11 then
					maq1 = "J"
				else
				if maq == 12 then
					maq1 = "Q"
				else
				if maq == 13 then
					maq1 = "K"

				# 11 a 13 de jugador le asigna una letra
				if j1 == 11 then
					j11 = "J"
				else
				if j1 == 12 then
					j11 = "Q"
				else
				if j1 == 13 then
					j11 = "K"

				# define tipos de cartas
				if tipo == 1 then
					tipo = "treboles"
				else
				if tipo == 2 then
					tipo = "picas"
				else
				if tipo == 3 then
					tipo = "corazones"
				else
				if tipo == 4 then
					tipo = "diamantes"

				# gana jugador1 si elguna variable es mayor que 10 se le asigna la variable con catacter alfabetico.
				if maq == j1 then
					print "¡¡Empate!!"
				else
				if j1 > maq then
					if j1 > 10 then
						j1 = j11
					fi
					if maq > 10 then
						maq = maq1
					fi
					print "tu:",j1,tipo,"Maquina:",maq,tipo," ¡¡Ganas tu!!"
					credito = credito + apuesta

				# pierde jugador1 si elguna variable es mayor que 10 se le asigna la variable con catacter alfabetico.
				else
					if j1 > 10 then
						j1 = j11
					fi		
					if maq > 10 then
						maq = maq1
					fi
					print "tu:",j1,tipo,"Maquina:",maq,tipo," ¡¡Pierdes!!"
					credito = credito - apuesta
			
				if credito <= 0 then
					print ("\033[;31m"+"Te quedaste sin pasta ¡¡Pringado!!"+"\033[0;m")
					print ""
					salir = True
				fi
				
ewhile
```


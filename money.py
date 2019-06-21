importo_str = input("Inserisci importo: ")
importo = int(importo_str)

if importo < 0:
	print("Per favore, inserisca un numero positivo!")

else:
	venti = 20
	dieci = 10
	cinque = 5
	uno = 1
	
	#Venti#
	b_venti = importo // venti
	resto_venti = importo % venti
	#Dieci#
	resto_venti = importo_a
	b_dieci = importo_a // dieci
	resto_dieci = importo_a % dieci
	#Cinque#
	resto_dieci = importo_b
	b_cinque = importo_b // cinque
	resto_cinque = importo_b % cinque
	#Uno#
	resto_cinque = importo_c
	b_uno = importo_c // uno
	resto_uno = importo_c % uno
	
	print("Biglietti da 20: ", b_venti,"\n" "Biglietti da 10: ", b_dieci,"\n" "Biglietti da 5: ", b_cinque,"\n" "Biglietti da 1: ", b_uno,"\n")
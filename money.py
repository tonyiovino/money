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
	importo = resto_venti
	b_dieci = importo // dieci
	resto_dieci = importo % dieci
	#Cinque#
	importo = resto_dieci
	b_cinque = importo // cinque
	resto_cinque = importo % cinque
	#Uno#
	importo = resto_cinque
	b_uno = importo // uno
	resto_uno = importo % uno
	
	print("Biglietti da 20: ", b_venti,"\n" "Biglietti da 10: ", b_dieci,"\n" "Biglietti da 5: ", b_cinque,"\n" "Biglietti da 1: ", b_uno,"\n")
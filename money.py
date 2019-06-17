print("Inserisci importo: ")
importo_str = input()
importo = float(importo_str)

if importo < 0:
	print("Per favore, inserisca un numero positivo!")

else:
	resto = importo

	importo / 20
	resto % 20

	importo = resto

	importo / 10
	resto % 10

	resto = importo

	importo / 5
	resto % 5

	importo = resto

	importo / 1
	resto % 1

	print(importo, resto)



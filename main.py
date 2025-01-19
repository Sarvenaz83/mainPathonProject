#1 Skapa projekt och synka med GitHub:

print("Hello World")
print("This program was made by Sarvenaz Sinaei")

# 3 Använda variabler och datatyper:
# 1a:

tal1_str= input("Skriv in ett heltal: ")
tal1 = int(tal1_str)
print("Du angav talet:", tal1)

# 1b:

tal2_str= input("Skriv in ett annat heltal: ")
tal2 = int(tal2_str)
summa =tal1 + tal2
print("Summan av talen är:",summa)

#2a:

pris = 2000
rea_procent = 50

slut_pris = pris * rea_procent / 100
print("Jackan kostar med 50% rea:", slut_pris, "kr")

#2b
pris = 2000

rea_input = input("Vilken procentsats har rean? (t.ex. 10, 50 osv): ")
rea_procent = int(rea_input)

rabatt = pris * rea_procent / 100
slut_pris = pris - rabatt

print("Jackans ordinarie pris är:", pris, "kr")
print("Du får", rea_procent, "% rabbat, vilket är", rabatt, "kr")
print("Slutpriset blir då:", slut_pris, "kr")



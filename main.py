import math
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

# 4 Fler övningar:
# 1a:
distance_km = 470
distance_m = distance_km / 1000

speed_kmh = float(input("Ange hastighet i km/h: "))

speed_ms = speed_kmh / 3.6

time_seconds = distance_m / speed_ms

time_hours = time_seconds / 3600
print("Det tar cirka", time_hours, "timmar att åka", distance_km, "km.")

# 1b
distance_km = 470
distance_m = distance_km * 1000

speed_kmh = float(input("Ange hastighet i km/h: "))
speed_ms = speed_kmh / 3.6

time_seconds = distance_m / speed_ms
time_minutes = time_seconds / 60

print("Det tar cirka", time_minutes, "minuter att åka", distance_km, "km.")

# 1c
distance_km = 470
distance_m = distance_km * 1000

speed_kmh = float(input("Ange hastighet i km/h: "))
speed_ms = speed_kmh / 3.6

time_seconds = distance_m / speed_ms
time_minutes = time_seconds / 60

hours = int(time_minutes // 60)
minutes = int(time_minutes % 60)

print(f"Det tar cirka {hours} timmar och {minutes} minuter att åka {distance_km} km.")


#2
a = float(input("Ange längden på sida a: "))
b= float(input("Ange längden på sida b: "))

c = math.sqrt(a**2 + b**2)
print("Hypotenusan är:", c)


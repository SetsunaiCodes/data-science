# X Value
x = input("Bitte X Wert angeben: ")
x = int(x)

# Schleifen wiederholung
times = input("Bitte Anzahl an Schleifen Iterationen angeben: ")
times = int(times)

# Variable zur Speicherung des vorherigen x-Werts
prev_x = None

for i in range(times):
    f = (x*x - x - 1)/(2*x-1) 
    x = x - f

    print(str(i) + ". Iteration, Wert: " + str(x))

    # Überprüfung, ob der aktuelle Wert von x dem vorherigen entspricht
    if prev_x is not None and x == prev_x:
        print("Finaler X Wert der Nullstelle: " + str(x))
        break
    
    # Speichern des aktuellen x-Werts für den nächsten Vergleich
    prev_x = x


from datetime import date

metai = 1900
while 2101 > metai:
 
    d0 = date(metai, 1, 1)
    d1 = date(metai, 12, 31)
    delta = d1 - d0
    if delta.days + 1 > 365:
        print("Keliamieji " + str(metai))     
    metai += 1

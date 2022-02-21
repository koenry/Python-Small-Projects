import time

answer1 = "1"
answer2 = "2"
required = ("\nPlease enter 1 or 2 and press ENTER ")

def pradzia():
  print("To calculate net salary press 1 and ENTER ")
  print("To calculate gross salary press 2 and ENTER ")
  choice = input("\n>>> ")
  if choice in answer1:
    popierius()
  elif choice in answer2:
    rankos()
  else:
    print( required)
    time.sleep(1)
    pradzia()
  

def popierius():                             # gross salary
    try:
       x = int(input("Enter gross salary " ))       
    except ValueError:
       print("Please enter a NUMBER ")
    else:
      npd = 400 - 0.18 * (x - 642)
      if npd > 400:                 # npd cant exceed 400
          npd = 400
      elif npd < 0:                # so we dont go less than 0
          npd = 0
      p = (x - npd) / 100


      if x > 400:                     # full tax
          pajamu = p * 20
          sodra = (x / 100) * 6.98
          sodra2 = (x / 100) * 12.52
          a = x - pajamu - sodra - sodra2
          print("NET Salary " "{:.2f}".format(round(a, 2)))
          print("Pajamu mokestis TAX ""{:.2f}".format(round(pajamu, 2)))
          print("Sodra. Sveikatos draudimas TAX ""{:.2f}".format(round(sodra, 2)))
          print("Sodra. Pensijų ir soc. draudimas TAX ""{:.2f}".format(round(sodra2, 2)))

      else:                           # tax without extra 20%
          sodra = (x / 100) * 6.98
          sodra2 = (x / 100) * 12.52
          a = x - sodra - sodra2
          print("NET Salary " "{:.2f}".format(round(a, 2)))
          print("Sodra. Sveikatos draudimas TAX ""{:.2f}".format(round(sodra, 2)))
          print("Sodra. Pensijų ir soc. draudimas TAX ""{:.2f}".format(round(sodra2, 2)))

      input("\nPress ENTER...")
def rankos():         # net salary
    try:
       x = int(input("Enter NET salary " ))       
    except ValueError:
       print("Please enter a NUMBER ")
    else:
      if x < 468.44:
        sodra = (x / 0.805) - x
        a = x + sodra
        print("GROSS Salary " "{:.2f}".format(round(a, 2)))
        
      elif x > 1732.8:
        sodraPaj = (x / 0.605) - x
        a = x + sodraPaj
        print("GROSS Salary " "{:.2f}".format(round(a, 2)))

      else:
        if x == 468.88:
          b = 642.07
          print("GROSS Salary " "{:.2f}".format(round(b, 2)))
        else:
          a = 642.07
          b = (x - 468.88) * 1.76
          c = a + b
          print("GROSS Salary " "{:.2f}".format(round(c, 2)))

        
      input("\nPress ENTER...")
        
while True:
  pradzia()


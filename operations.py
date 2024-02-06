def addition (a, b):
  resultat = a + b
  return resultat

def soustraction (a, b):
  resultat = a - b
  return resultat

def multiplication (a, b):
  resultat = a * b
  return resultat

def division (a, b):
  try:
    resultat = a / b
    return resultat
  except ZeroDivisionError:
    print("Erreur : Division par 0 !")
  except ValueError:
    print("Erreur : Ce n'est pas un nombre entier !")


  
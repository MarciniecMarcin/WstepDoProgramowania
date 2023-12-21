prad={'styczeń': 320,
      'luty': 300,
      'marzec': 310,
      'kwiecień': 295,
      'maj': 290,
      'czerwiec': 270,
      'lipiec': 270,
      'sierpień': 275,
      'wrzesień': 280,
      'październik': 290,
      'lstopad': 300,
      'grudzień': 315}
faktura=list(prad.values())

mean = round(sum(faktura)/len(faktura),2)
ListaWartości={'wartość max faktury':max(faktura),
               'wartość min faktury':min(faktura),
               'średnia': mean}
print(ListaWartości)

if mean > faktura[-1]: #porównuję do średniej zawsze ostatni element słownika
      print("Jesteś bezpieczny")
elif mean < faktura[-1]:
      print("zacznij oszczędzać")
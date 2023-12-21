from pprint import pprint

listaZakupow = {'masło': 3,
                'twaróg': 5,
                'miód': 10,
                'bułka': 7}
pprint(listaZakupow)
rachunek=sum(listaZakupow.values())
print(rachunek)
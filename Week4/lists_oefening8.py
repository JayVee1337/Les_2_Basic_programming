# Schrijf een functie ‘som_num_in_list’ met als parameter een list van getallen die de totale
# som van de list getallen teruggeeft.

lijst= list(range(1,101))
def som_num_in_list(lijst):
    b = sum(lijst)
    print(b)
som_num_in_list(lijst)
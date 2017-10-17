#Oefening1
Gehele_Getallen = [2,4,6,8]
Decimale_Getallen = [2.1, 4.2, 8.4, 16.8, 33.6]
Strings = ["Donald Trump", "Hillary Clinton", "Bernie Sanders"]

def print_list(lijst):
    for item in lijst:
        print("{0} staat op plaats {1} in zijn lijst".format(item, lijst.index(item)))

print_list(Gehele_Getallen)
print_list(Decimale_Getallen)
print_list(Strings)

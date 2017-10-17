vrienden = ["Barack Obama", "Donald Trump", "Hillary Clinton", "Theodore Roosevelt"] #Dynamisch datatype lijst
getallen = [1,6,78,-70,6,45,78,454]

def print_lijst(lijst):
    for item in lijst:
        print(item)

# print(vrienden)
# print(getallen)
#
# print_lijst(vrienden)
# print_lijst(getallen)
vrienden.append("Bernie Sanders")
# print_lijst(vrienden[1:3])
vrienden.insert(1, "Michelle Obama")
vrienden.remove("Donald Trump")
# print (vrienden)
# print (len(vrienden))
vrienden[0] = "George Washington"
print(getallen.count(78))
print(getallen.index(78))
print(vrienden)
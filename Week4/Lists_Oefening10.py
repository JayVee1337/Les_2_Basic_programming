#Oefening10

def zijn_verschillend(list1, list2):
    for item_van_list1 in list1:
        if item_van_list1 in list2:
            return False
    #Ik heb alle items van lijst1 gecontroleerd
    return True
list1= [2,5,6,8,4861,45,62]
list2= [2,41,54,52]

if zijn_verschillend(list1,list2):
    print("lijsten zijn helemaal verschillend")
else: print("er is minstens 1 gemeenschappelijk element")
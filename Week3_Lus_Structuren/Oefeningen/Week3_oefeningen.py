# # # # def som_eerste_100_getallen():
# # # #     som = 0
# # # #     for i in range (1,101):
# # # #         som= som + i
# # # #     print ("de som van de eerste 100 getallen is {0}".format(som))
# # # #
# # # som_eerste_100_getallen()
# # # print 10 veelvouden van
# # #
# # # def print_veelvouden_van(getal):
# # #     for i in range(0, 11):
# # #         print (i*getal)
# # # getal = int(input("geef getal "))
# # # print_veelvouden_van(getal)
# # # print 20 tot 50
# # # def print_20__tot_50():
# # #     for i in range (20,51):
# # #         print (i)
# # #
# # # print_20__tot_50()
# # #print alle even getallen tussen 2 en 100
# # # def even_getallen():
# # #     for i in range(4,101,2):
# # #         print (i)
# # # even_getallen()
# #
# # #deelbaar door 7 maar gn vv v 5 tussen 200 en 308
# # # def db7nvvv5():
# # #     for i in range(200,309):
# # #         if i%7 ==0 and not i%5 ==0:
# # #             print(i)
# # #
# # #
# # # #oneven getallen
# # # def oneven():
# # #     for i in range (11, 130, 2):
# # #         print(i)
# # #oneven2
# # def oneven2():
# #     for i in range (99,0,-3):
# #         print(i)
# # oneven2()
# #
# # # import math
# # #
# # # def bereken_oppervlakte_cirkel(diameter):
# # #     opp = ((diameter/2.0) ** 2) * math.pi
# # #     return opp
# # # oppervlakte = bereken_oppervlakte_cirkel(4)
# # # print(oppervlakte)
# #
# #
# #deelbaar door 7 maar gn vv v 5 tussen 200 en 308
# def db7nvvv5():
#      for i in range(200,309):
#          if i%7 ==0 and not i%5 ==0:
#              print(i)
# db7nvvv5()


# #3_getallen_opvragen
# def print_lijst_getallen():
#      startwaarde=int(input("Geef een startwaarde op: "))
#      Stapgroote = int(input("Geef een positieve stapgrootte op: "))
#      printgetal= int(input("Hoeveel getallen moeten er afgeprint worden? "))
#      for i in range(startwaarde,startwaarde+(Stapgroote*printgetal),Stapgroote):
#          print(i)
# print_lijst_getallen()

# #while lus
# def eerste100metwhile(getal = 0):
#     som = 0
#     while getal <=100:
#         getal = getal+1
#         som = som+getal
#     print(som)
# eerste100metwhile()
#

#random getal gokker
import random
i = random.randrange(1,21)
def Gokjewagen(i):


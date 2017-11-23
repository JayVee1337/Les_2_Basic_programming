scores = {}
gemiddelde = {}
def scores_inlezen(dict1,dict2):
    file = open("Scores.txt","r+")
    for x in file:
        x = x.rstrip("\n")
        x = x.split(":")
        dict1[x[0]] = x[1] +" "+ x[2] +" "+ x[3] +" "+ x[4] +" "+ x[5]
        get1= int(x[1])
        get2= int(x[2])
        get3= int(x[3])
        get4= int(x[4])
        get5= int(x[5])
        gem = (get1+get2+get3+get4+get5) / 5
        dict2[x[0]] = gem
scores_inlezen(scores,gemiddelde)

def naam_score_gemiddelde(student):
    for item in scores:
        if student in item:
            print(item +": "+ scores[item])
            print("Gemiddelde ==> {0}/20" .format(gemiddelde[item]))

naam_score_gemiddelde(input("Geef een student in(HOOFDLETTER GEVOELIG): "))
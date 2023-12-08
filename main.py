import time


def startInterview (entrepriseName,candidateName,interview) :
    start_time = time.time()
    Timing [candidateName]=start_time
    t=900
    while t:
        time.sleep(1)
        t -= 1
    print(f"inetrview started with {candidateName} since 15 min preparez un autre candidat")

    return 0


def endInterview (entrepriseName,Queue,candidateName,interview) :
    end_time = time.time()
    elapsed_time = end_time - interview[candidateName]
    print ( f"{Queue[entrepriseName][0]} is next")
    Queue[entrepriseName].remove(Queue[entrepriseName][0])
    return 0


def addToQueue(candidateName,entrepriseName,Queue) :
    if entrepriseName not in Queue.keys() :
        Queue[entrepriseName] = []
    Queue[entrepriseName].append(candidateName)
    return 0



def init () :
    nbr_entreprsie= int(input("donner le nombre d'entreprise dans cette etage"))
    max_queue=int(input("donner le nombre maximal des candidat en attente"))
    Queue={}
    interview={}
    for i in range(nbr_entreprsie) :
      entreprise_name=input(f"donner le nom de l'entreprise numéro {i}")
      nbr_place=int(input("donner le nombre des candidats max que cette entreprise peut le voir en meme temp "))
      interview[entreprise_name]=nbr_place
    return 0


def setEntrepriseNumber() :
  return 0
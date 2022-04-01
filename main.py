import sys
import math
import numpy
#variables
zombie_id=0
zombie_xnext=0
zombie_ynext=0
#
liste_pos_humains={}
liste_pos_zombies={}
#
liste_pos_euclidian=[]
dict_pos_euclidian={}
#

# Distance euclidienne
def euclidian_distance(point1, point2):
    differences = [point1[x] - point2[x] for x in range(len(point1))]
    differences_squared = [difference ** 2 for difference in differences]
    sum_of_squares = sum(differences_squared)
    return int(sum_of_squares ** 0.5)
#


# game loop
while True:
    x, y = [int(i) for i in input().split()]
    print("position Ash:",x,y, file=sys.stderr, flush=True)
    


    # HUMAINS ZONE (autre que Ash)
    human_count = int(input())
    for i in range(human_count):
        human_id, human_x, human_y = [int(j) for j in input().split()]
        #print("position Humains:",human_id, human_x, human_y, file=sys.stderr, flush=True)
        liste_pos_humains.update({human_id: (human_x,human_y)})
    print(liste_pos_humains, file=sys.stderr, flush=True)
    #

    zombie_count = int(input())
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]
        #print("position Zombies:",zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext, file=sys.stderr, flush=True)
        liste_pos_zombies.update({zombie_id: (zombie_xnext,zombie_ynext)})
    print(liste_pos_zombies, file=sys.stderr, flush=True)
    #
    for loop in range(human_count):
        for x, y in liste_pos_zombies.items():
            liste_pos_euclidian.append(euclidian_distance(liste_pos_humains[loop], y))
            dict_pos_euclidian.update({"{}:{}".format(x,loop): euclidian_distance(liste_pos_humains[loop], y)})
            tuple_str = "{} {}"
            print(tuple_str.format(*y))
    liste_pos_euclidian.sort()   
    print(liste_pos_euclidian, file=sys.stderr, flush=True)
    print(dict_pos_euclidian, file=sys.stderr, flush=True)




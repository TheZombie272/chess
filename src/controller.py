
from src.utils import *
from src.model import *


# Rey: K, Dama: D, Peon: P, Caballo: C, Alfil: A, Torre: T
def entry(table_b, table_w, piece, i_pos, f_pos):

    #if dont_put(table_b, table_w, type, i_pos, f_pos):
     #   return False

    if not validatorPosition(table_b, table_w, piece, f_pos):
        return False

    if piece[0] == 'K':
        if not validatorKing(table_b, table_w, piece, i_pos, f_pos):
            return False
    elif piece[0] == 'D':
        if not validatorD(table_b, table_w, piece, i_pos, f_pos):
            return False
    elif piece[0] == 'P':
        if not validatorP(table_b, table_w, piece, i_pos, f_pos):
            return False
    elif piece[0] == 'C':
        if not validatorC(table_b, table_w, piece, i_pos, f_pos):
            return False
    elif piece[0] == 'A':
        if not validatorA(table_b, table_w, piece, i_pos, f_pos):
            return False
    elif piece[0] == 'T':
        if not validatorT(table_b, table_w, piece, i_pos, f_pos):
            return False

    print("llegamos a save")
    save_play(table_b, table_w, piece, i_pos, f_pos)
    return True


def prueba(turno, table_w, table_b):

    juego  = juntar(table_w, table_b)

    for i in juego:
        print(i)

    i_pos = [0,0]
    f_pos = [0,0]
    i_pos[0]=int(input("posición inicial en y: "))
    i_pos[1]=int(input("posición inicial en x: "))

    f_pos[0]=int(input("posición final en y: "))
    f_pos[1]=int(input("posición final en x: "))

    type = [0,0]
    if turno == 0:
        type=[ table_w[i_pos[0]][i_pos[1]] , 0]
        print(type)
        if not table_w[i_pos[0]][i_pos[1]] is None:
            if entry(table_b, table_w, type, i_pos, f_pos):
                return 1

    else:
        type = [table_b[i_pos[0]][i_pos[1]], 1]
        if not table_b[i_pos[0]][i_pos[1]] is None:
            if entry(table_b, table_w, type, i_pos, f_pos):
                return 0
    print("devuelve turno")
    return turno



table_w = [
    ['T', 'C', 'A', 'K', 'D', 'A', 'C', 'T'],
    ['P'] * 8,
    [None] * 8,
    [None] * 8,
    [None] * 8,
    [None] * 8,
    [None] * 8,
    [None] * 8
]

table_b = [
    [None] * 8,
    [None] * 8,
    [None] * 8,
    [None] * 8,
    [None] * 8,
    [None] * 8,
    ['P'] * 8,
    ['T', 'C', 'A', 'K', 'D', 'A', 'C', 'T']
]

turno=0

while True:

    turno = prueba(turno, table_w, table_b)

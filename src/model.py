def validatorPosition(table_b, table_w, piece, f_pos):
    # Validar que no se salga
    if not (((f_pos[0] <= 7) and (f_pos[0] >= 0)) and (f_pos[1] <= 7) and (f_pos[1] >= 0)):
        return False

    # Validar que no se paró en otra ficha del mismo color
    if piece[1] == 0:
        if table_w[f_pos[0]][f_pos[1]] is None:
            return True
    else:
        if table_b[f_pos[0]][f_pos[1]] is None:
            return True

    return False

def validatorKing(table_b, table_w, piece, i_pos, f_pos):

    # Validar que solo se movió una casilla
    if not (abs(f_pos[0] - i_pos[0]) <= 1 and abs(f_pos[1] - i_pos[1]) <= 1 ):
        return False


def validatorD(table_b, table_w, piece, i_pos, f_pos):

    # Validar si se movió horizontal, vertical o diagonal
    if not (f_pos[0]==i_pos[0] or f_pos[1]==i_pos[1]):
        # Validar si se movio en diagonal
        if not (abs(i_pos[0] - i_pos[1]) == abs(f_pos[0] - f_pos[1]) or abs(i_pos[0] + i_pos[1]) == abs(f_pos[0] + f_pos[1])):
            return False


    if not validatorLineal(table_b, table_w, piece, i_pos, f_pos):
        return False

    if not validatorDiagon(table_b, table_w, i_pos, f_pos):
        return False

    return True


def validatorP(table_b, table_w, piece, i_pos, f_pos):

    # Si es negra va hacia abajo y si es blanca hacia arriba
    a=1
    if piece[1] == 1:
        a=-1
    # Validar que se movió hacia adelante
    if not i_pos[0]+a == f_pos[0] :
        return False

    print("adelante")
    # Mirar si comió
    if abs(i_pos[1]-f_pos[1]) == 1 :

        if piece[1] == 0:
            if table_b[f_pos[0]][f_pos[1]] is None:
                return False
        else:
            if table_w[f_pos[0]][f_pos[1]] is None:
                return False
    return True


def validatorC(table_b, table_w, piece, i_pos, f_pos):

    # Si se movio en x 2 entonces 1 en y, si se movio 2 en y entonces 1 en x
    if not ((abs(i_pos[0]-f_pos[0]) == 2 and abs(i_pos[1]-f_pos[1]) == 1) or (abs(i_pos[0]-f_pos[0]) == 1 and abs(i_pos[1]-f_pos[1]) == 2)) :
        return False

    return True


def validatorA(table_b, table_w, piece, i_pos, f_pos):

    # Validar si se movio en diagonal
    if not (abs(i_pos[0] - i_pos[1]) == abs(f_pos[0] - f_pos[1]) or abs(i_pos[0] + i_pos[1]) == abs(f_pos[0] + f_pos[1])):
        return False

    if not validatorDiagon(table_b, table_w, i_pos, f_pos):
        return False


    return True


def validatorT(table_b, table_w, piece, i_pos, f_pos):

    # Validar que se movio en horizontal o vertical
    if not (i_pos[0] == f_pos[0] or i_pos[1] == f_pos[1]):
        return False


    return True


def validatorLineal(table_b, table_w, piece, i_pos, f_pos):

    i_t_pos= i_pos.copy()
    f_t_pos= f_pos.copy()

    # Validar que no se paró en otra ficha en horizontal vertical
    for a in range(2):
        while abs(i_t_pos[a] - f_t_pos[a]) > 1:

            if i_t_pos[a] < f_t_pos[a]:
                i_t_pos[a] +=1
            else:
                f_t_pos[a] += 1

            if not table_b[i_t_pos[a]][f_t_pos[1]] is None:
                return False
            if not table_w[i_t_pos[a]][f_t_pos[1]] is None:
                return False

    return True


def validatorDiagon(table_b, table_w, i_pos, f_pos):

    i_t_pos = i_pos.copy()

    # Validar que no se paro en otra ficha en diagonal
    cont = 0
    while abs(i_t_pos[0] - f_pos[0])< 1:

        #si está abajo
        if i_t_pos[0] < f_pos[0]:
            i_t_pos[0] += 1
            if i_t_pos[1] < f_pos[1]:# si está a la izquierda
                i_t_pos[1] += 1
            else:
                i_t_pos[0] -= 1

        #si está arriba
        else:
            f_pos[0] -= 1
            if i_t_pos[1] < f_pos[1]: # si está a la izquierda
                i_t_pos[1] += 1
            else:
                i_t_pos[0] -= 1

        # Revisar que no haya ninguna ficha en las posiciones de negras y blancas
        if not (table_b[i_t_pos[0]][i_t_pos[1]] is None or table_w[i_t_pos[0]][i_t_pos[1]] is None):
            return False

    return True

def save_play(table_b, table_w, piece, i_pos, f_pos):
    if piece[1] == 0:
        table_w[f_pos[0]][f_pos[1]] = piece[0]
        table_w[i_pos[0]][i_pos[1]] = None
        table_b[f_pos[0]][f_pos[1]] = None
    else:
        table_b[f_pos[0]][f_pos[1]] = piece[0]
        table_b[i_pos[0]][i_pos[1]] = None
        table_w[f_pos[0]][f_pos[1]] = None


def juntar(table_w, table_b):

    # Tabla donde se almeacenan las dos matrices juntas
    new_table = []

    # Juntar las tablas
    for i in range(len(table_w)):
        temp=[]
        for j in range(len(table_b[i])):
            if table_w[i][j] is None:
                temp.append(table_b[i][j])
            else:
                temp.append(table_w[i][j])
        new_table.append(temp)
    return new_table

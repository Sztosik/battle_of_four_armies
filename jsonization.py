from board import Board

def jsonization(board: Board, board_x: int, board_y: int) -> []:
    """
    Zwraca słownik zawierający informacje na temat każdego pola, które stanem różni się od domyślnego
    """
    data = []

    def is_occupied(unit_list):
        if len(unit_list) == 0:
            return False
        else:
            return True

    for x in range(board_x):
        for y in range(board_y):
            field_state = is_occupied(board.board_fields[y][x].get_units())
            if not board.board_fields[y][x].get_fraction() == "none":
                json_data = {
                    "x": x,
                    "y": y,
                    "fraction": board.board_fields[y][x].get_fraction(),
                    "isOccupied": field_state
                }
                data.append(json_data)

    return data




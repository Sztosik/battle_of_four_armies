import csv


def get_rows(stats_list: list[dict]) -> dict:
    """
    Generator statystyk dla kolejnych iteracji.

    :param stats_list: lista statystyk
    :yield: dict
    """
    for stats_dict in stats_list:
        yield stats_dict


def get_header(stats_list: list[dict]):
    """
    Zwraca klucze słownika.

    :param stats_list: lista statystyk
    :return: dict_keys
    """

    stats_dict = stats_list[0]
    header = stats_dict.keys()
    return header


class Stast:
    """
    Przetwarza i zapisuje statystyki do plików csv.
    """

    def __init__(self):
        self.__units_stats: list[dict] = []
        self.__captured_fields_stats: list[dict] = []

    def add_row(self, captured_fields_row: dict, units_row: dict):
        """
        Dodaje nowe statystyki.

        :param captured_fields_row: słownik statystyk planszy
        :param units_row: słownik statystyk jednostek armii
        """
        self.__units_stats.append(units_row)
        self.__captured_fields_stats.append(captured_fields_row)

    def save_to_csv(self):
        """
        Zapisuje wszystkie statystyki do dwóch plików csv.

        :return: None
        """
        with open("captured_fields_stats.csv", "w") as file:
            fieldnames = get_header(self.__captured_fields_stats)
            csv_writer = csv.DictWriter(file, delimiter=",", fieldnames=fieldnames)
            csv_writer.writeheader()
            for row in get_rows(self.__captured_fields_stats):
                csv_writer.writerow(row)

        print("Stats saved into captured_fields_stats.csv")

        with open("units_stats.csv", "w") as file:
            fieldnames = get_header(self.__units_stats)
            csv_writer = csv.DictWriter(file, delimiter=",", fieldnames=fieldnames)
            csv_writer.writeheader()
            for row in get_rows(self.__units_stats):
                csv_writer.writerow(row)

        print("Stats saved into units_stats.csv")

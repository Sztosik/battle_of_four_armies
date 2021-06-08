import csv

class Stast:
    def __init__(self):
        self.__units_stats: list[dict] = []
        self.__captured_fields_stats: list[dict] = []

    def add_row(self, captured_fields_row: dict):
        # self.__units_stats.append(units_row)
        self.__captured_fields_stats.append(captured_fields_row)

    def get_rows(self, stats_list: list[dict]):
        for stats_dict in stats_list:
            yield stats_dict

    def get_header(self, stats_list: list[dict]):
        stats_dict = stats_list[0]
        header = stats_dict.keys()
        return header

    def save_to_csv(self):
        with open('captured_fields_stats.csv', 'w') as file:
            fieldnames = self.get_header(self.__captured_fields_stats)
            csv_writer = csv.DictWriter(file, delimiter=',', fieldnames=fieldnames)
            csv_writer.writeheader()
            for row in self.get_rows(self.__captured_fields_stats):
                csv_writer.writerow(row)
                # print(row)
        print("Stats saved into captured_fields_stats.csv")
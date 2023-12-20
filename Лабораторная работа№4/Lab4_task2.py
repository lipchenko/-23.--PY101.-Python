# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
def convert_csv_to_json(input_file: str, output_file: str) -> None:
    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    with open(output_file, 'w', encoding='utf-8') as jsonfile:
        json.dump(rows, jsonfile, indent=4)








if __name__ == '__main__':
    convert_csv_to_json(INPUT_FILENAME, OUTPUT_FILENAME)
    with open(OUTPUT_FILENAME, 'r', encoding='utf-8') as output_f:
        for line in output_f:
            print(line, end="")

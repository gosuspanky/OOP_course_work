import os.path

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(ROOT_DIR, 'data', 'data.json')
SORTED_DATA_DIR = os.path.join(ROOT_DIR, 'data', "sorted_data.json")

TXT_OUTPUT_DIR = os.path.join(ROOT_DIR, 'data', "Vacancies.txt")
JSON_OUTPUT_DIR = os.path.join(ROOT_DIR, 'data', "Vacancies.json")

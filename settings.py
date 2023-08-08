from pathlib import Path

# Директории
ROOT = Path(__file__).resolve().parent
DATA = Path(ROOT, 'data')

#  Файлы
HH_VACANCIES = Path(DATA, 'vacancies.json')
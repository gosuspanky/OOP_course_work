# Парсер вакансий с HeadHunter

Данная программа получает информацию о вакансиях с платформы hh.ru по России, сортирует данные по городу,
заработной плате, позволяет вывести топ вакансий и сохранить их в отдельный .txt файл. Так же сохраняет данные в .json
файл. 

## **Структура проекта:**

### **data:**

* [Vacancies.json](data/Vacancies.json) - файл хранения обработанных вакансий в формате .json
* [Vacancies.txt](data/Vacancies.txt) - файл хранения краткого описания вакансий в формате .txt

### **src:**

* [hh_data.py](src/hh_data.py) - класс получения данных с HeadHunter'а по его API
* [save_vacancies.py](src/save_vacancies.py) - классы для сохранения данных в файл
* [utils.py](src/utils.py) - функции проекта
* [vacancy.py](src/vacancy.py) - класс обработки вакансии

### **tests:**

* [test_hh_data.py](tests/test_hh_data.py) - тесты класса hh_data
* [test_utils.py](tests/test_utils.py) - тесты функций
* [test_vacancy.py](tests/test_vacancy.py) - тесты класса Vacancy

### **root:**

* [.gitignore](.gitignore) - файл .gitignore
* [config.py](config.py) - конфиг путей
* [main.py](main.py) - основной файл для запуска
* [pyproject.toml](pyproject.toml) - файл подключенных библиотек
* [README.md](README.md) - описание проекта


Чтобы скачать проект, нажмите на зеленую кнопку <>Code и либо склонируйте себе в свой IDE, либо скачайте ZIP архив.
Для запуска программы нужно запустить код из main файла в корне проекта.
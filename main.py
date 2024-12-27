from environs import Env
import requests
from terminaltables import AsciiTable

LANGUAGES = (
    "Python",
    "Java",
    "Javascript",
    "Ruby",
    "PHP",
    "C++",
    "C#:",
    "C",
    "Go",
    "Shell",
)


def predict_rub_salary_for_hh(vacancy):
    if vacancy["salary"]:
        if vacancy["salary"]["currency"] == "RUR":
            salary_from = vacancy["salary"]["from"]
            salary_to = vacancy["salary"]["to"]
            return predict_salary(salary_from, salary_to)
    return None


def predict_rub_salary_for_sj(vacancy):
    if vacancy["currency"] == "rub":
        salary_from = vacancy["payment_from"]
        salary_to = vacancy["payment_to"]
        return predict_salary(salary_from, salary_to)
    return None


def predict_salary(salary_from, salary_to):
    if salary_from and salary_to:
        return salary_from + salary_to / 2
    elif salary_from and not salary_to:
        return salary_from * 1.2
    elif not salary_from and salary_to:
        return salary_to * 0.8
    else:
        return None


def get_statistics_on_languages_from_hh(languages):
    statistics = {}
    url = "https://api.hh.ru/vacancies"
    for language in languages:
        response_file = []
        page = 0

        while True:
            payload = {
                "text": "программист " + language,
                "area": "1",
                "page": page,
                "per_page": 100,
            }
            response = requests.get(url, params=payload)
            response.raise_for_status()
            response_file.append(response.json())
            if response_file[page]["pages"] == page + 1:
                break
            page += 1

        vacancies_found = response_file[0]["found"]
        vacancies_processed = 0
        total_salary = 0

        for response_page in response_file:
            for vacancy in response_page["items"]:
                predict_salary = predict_rub_salary_for_hh(vacancy)
                if predict_salary:
                    vacancies_processed += 1
                    total_salary += predict_salary
        if not total_salary:
            average_salary = 0
        else:
            average_salary = int(total_salary / vacancies_processed)

        statistics[language] = {
            "vacancies_found": vacancies_found,
            "vacancies_processed": vacancies_processed,
            "average_salary": average_salary,
        }
    return statistics


def get_statistics_on_languages_from_sj(languages, sj_api):
    statistics = {}
    url = "	https://api.superjob.ru/4.0/vacancies/"
    headers = {
        "X-Api-App-Id": sj_api
    }

    for language in languages:
        response_file = []
        page = 0

        while True:
            payload = {
                "keyword": "Программист " + language,
                "town": 4,
                "catalogues": 48,
                "count": 100,
                "page": page,
            }
            response = requests.get(url, headers=headers, params=payload)
            response.raise_for_status()
            response_file.append(response.json())
            if not response_file[page]["more"]:
                break
            print(page)
            page += 1

        vacancies_found = response_file[0]["total"]
        vacancies_processed = 0
        total_salary = 0

        for response_page in response_file:
            for vacancy in response_page["objects"]:
                predict_salary = predict_rub_salary_for_sj(vacancy)
                if predict_salary:
                    vacancies_processed += 1
                    total_salary += predict_salary
        if not total_salary:
            average_salary = 0
        else:
            average_salary = int(total_salary / vacancies_processed)

        statistics[language] = {
            "vacancies_found": vacancies_found,
            "vacancies_processed": vacancies_processed,
            "average_salary": average_salary,
        }
    return statistics


def print_statistics(statistics, table_name):
    table_data = [["Язык программирования", "Вакансий найдено", "Вакансий обработано", "Средняя зарплата "], ]
    for language, language_statistics in statistics.items():
        row = []
        row.append(language)
        [row.append(column) for column in list(language_statistics.values())]
        table_data.append(row)
    table = AsciiTable(table_data, title=table_name)
    print(table.table)
    print()


def main():
    env = Env()
    env.read_env()
    print_statistics(get_statistics_on_languages_from_sj(LANGUAGES, env("SUPERJOB_API_KEY")), "SuperJob Moscow")
    print_statistics(get_statistics_on_languages_from_hh(LANGUAGES), "HeadHunter Moscow")


if __name__ == '__main__':
    main()

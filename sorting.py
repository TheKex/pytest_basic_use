from pprint import pprint
# Наводим порядок: упорядочиваем курсы по продолжительности

courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
           "Frontend-разработчик с нуля"]
mentors = [
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
durations = [14, 20, 12, 20]


def get_cources_sorted_by_duration(courses, durations):
    courses_list = []
    for course, duration in zip(courses, durations):
        course_dict = {"title": course, "duration": duration}
        courses_list.append(course_dict)

    durations_dict = {}

    for item in courses_list:
        key = str(item["duration"])
        if key in durations_dict:
            durations_dict[key] += [item["title"]]
        else:
            durations_dict[key] = [item["title"]]
    durations_dict = dict(sorted(durations_dict.items()))

    return durations_dict



durations_dict = get_cources_sorted_by_duration(courses, durations)

# Выведите курсы, отсортированные по длительности
# Допишите код цикла так, чтобы в нём вы получали из durations_dict ключи и значения
for key, titles in durations_dict.items():
    # Допишите код, который проходит по всему списку значений и выводит на экран текст вида «название курса — длительность»
    for title in titles:
        print(f'{title} - {key} месяцев')
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


def get_min_max_duration_cource(courses, durations):
    courses_list = []
    # Допишите код, который генерирует словарь-курс с тремя ключами: "title", "mentors", "duration"
    for title, duration in zip(courses, durations):
        course_dict = {"title": title, "duration": duration}
        courses_list.append(course_dict)

    # min_dur = min(courses_list, key=lambda x: x["duration"])["duration"]
    # max_dur = max(courses_list, key=lambda x: x["duration"])["duration"]

    min_dur = min(durations)
    max_dur = max(durations)

    maxes = []
    minis = []
    for i, _ in enumerate(durations):
        if _ == max_dur:
            maxes.append(i)
        elif _ == min_dur:
            minis.append(i)

    courses_min = []
    courses_max = []
    for i in minis:
        courses_min.append(courses_list[i]["title"])
    for i in maxes:
        courses_max.append(courses_list[i]["title"])

    return courses_min, min_dur, courses_max, max_dur


if __name__ == "__main__":
    courses_min, min_dur, courses_max, max_dur = get_min_max_duration_cource(courses, durations)

    # Допишите конструкцию вывода результата. Можете использовать string.join()
    print(f'Самый короткий курс(ы): {", ".join(courses_min)} - {min_dur} месяца(ев)')
    print(f'Самый длинный курс(ы): {", ".join(courses_max)} - {max_dur} месяца(ев)')
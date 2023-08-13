from my_collections import min_max, names, sorting

import pytest


class TestCollection:
    def test_unique_mentors_codes(self):
        mentors = [
            ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
             "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина",
             "Азамат Искаков",
             "Роман Гордиенко"],
            ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
             "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
             "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
             "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
            ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
             "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая",
             "Денис Ежков",
             "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
            ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
             "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
        ]
        expected = [[],
                    ['Адилет', 'Азамат', 'Денис', 'Евгений', 'Ринат', 'Роман', 'Сергей'],
                    ['Владимир', 'Иван', 'Тимур'],
                    ['Олег', 'Татьяна'],
                    ['Антон', 'Кирилл', 'Павел'],
                    ['Алексей', 'Анна', 'Елена', 'Илья', 'Никита', 'Эдгар'],
                    ['Анатолий', 'Вадим', 'Николай'],
                    ['Дмитрий', 'Максим'],
                    ['Валерий', 'Константин', 'Михаил', 'Филипп', 'Юрий'],
                    ['Александр', 'Алена']]
        result = names.get_unique_names_codes(mentors)
        assert result == expected


    @pytest.mark.parametrize(
        "courses, durations, exp_courses_min, exp_min_dur, exp_courses_max, exp_max_dur",
        [
            (['Test1', 'Test2', 'Test3'], [10, 20, 30], ['Test1'], 10, ['Test3'], 30),
            (['Test1', 'Test2', 'Test3'], [10, 20, 10], ['Test1', 'Test3'], 10, ['Test2'], 20),
            (['Test1', 'Test2', 'Test3'], [10, 20, 20], ['Test1'], 10, ['Test2', 'Test3'], 20)
        ]
    )
    def test_min_max(self, courses, durations, exp_courses_min, exp_min_dur, exp_courses_max, exp_max_dur):
        courses_min, min_dur, courses_max, max_dur = min_max.get_min_max_duration_cource(courses, durations)
        assert (courses_min, min_dur, courses_max, max_dur) == (exp_courses_min, exp_min_dur, exp_courses_max, exp_max_dur)


    @pytest.mark.parametrize(
        "courses, durations, expected_result",
        [
            (['test1', 'test2'], [10, 20], {'10': ['test1'], '20': ['test2']}),
            (['test1', 'test2'], [10, 10], {'10': ['test1', 'test2']}),
            (['test1', 'test2', 'test3'], [10, 20, 20], {'10': ['test1'], '20': ['test2', 'test3']})
        ]
    )
    def test_sorting(self, courses, durations, expected_result):
        res = sorting.get_cources_sorted_by_duration(courses, durations)
        assert expected_result == res

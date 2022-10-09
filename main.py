from os.path import exists


def read_file(file_path: str) -> list:
    """
    Чтение файла по строкам
    :param file_path: путь к файлу
    :return: список строк из файла
    """
    with open(file_path) as file:
        return file.readlines()


def get_filter(data: list, user_input: str) -> list:
    """
    Фильтрует список и приводит его в красивый вид
    :param data: список с данными
    :param user_input: искомый элемент пользователя
    :return: выводит отсортированный список
    """
    data_filter = filter(lambda d: user_input in d, data)
    filtered_data = []
    for d in data_filter:
        filtered_data.append(' '.join(list(d.replace('- - ', '').split(' ')[:7])))
    return filtered_data


def map_func(data: list, num_col: str) -> list:
    """
    Фильтрация списка по номеру столбца
    :param data: список с данными
    :param num_col: номер итерируемого столбца
    :return: возвращает список искомых столбцов
    """
    map_text = map(lambda x: x.split(' ')[int(num_col)], data)
    return list(map_text)


def unique_func(data: list, _: any) -> list:
    """
    Оставляет только уникальные строки
    :param _: любой параметр, не используется
    :param data: список с данными
    """
    unique_text = set(data)
    return list(unique_text)


def sort_func(data: list, param: str) -> list:
    """
    Сортирует список по возрастанию или убыванию, в зависимости от param
    :param data: список с данными для обработки
    :param param: вводимый пользователем параметр обработки
    :return: возвращает отсортированный список
    """
    if param == 'asc':
        return sorted(data)
    elif param == 'desc':
        return sorted(data, reverse=True)


def limit_func(data: list, param: str) -> list:
    """
    Ограничивает вывод строк в зависимости от param
    :param data: список с данными для обработки
    :param param: вводимый пользователем параметр обработки
    :return: возвращает необходимое количество строк
    """
    limit_text = (line for line in data[:int(param)])
    return list(limit_text)


def main() -> None:
    command_dict = {
        "filter": get_filter,
        "limit": limit_func,
        "map": map_func,
        "sort": sort_func,
        "unique": unique_func
    }

    while True:
        file_path = input('Введите путь до файла:\n>>> ')
        if not exists(file_path):
            print('Такого файла не существует, введите заново\n')
            continue
        else:
            break

    print('Доступные функции и их параметры:\n'
          'filter: любой искомый элемент\n'
          'limit: число выводимых элементов\n'
          'map: номер искомой колонки\n'
          'sort: asc - сортировка по возрастанию, desc - сортировка по убыванию\n'
          'unique: любой символ\n')

    while True:
        user_input = input('Введите команду в формате "функция параметр | функция параметр"\n>>> ')
        if user_input == 'exit':
            break
        data = read_file(file_path)
        list_c = user_input.strip().split("|")

        for i in list_c:
            command, value = i.split()
            if command in command_dict:
                data = command_dict[command](data, value)
            else:
                print("Не могу выполнить данную команду. Повторите ввод.")

        for text in data:
            print(text)


if __name__ == '__main__':
    main()

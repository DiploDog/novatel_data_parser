def missing_file(rus):
    if rus:
        print('Ошибка! Файл отсутствует или поврежден.')
    else:
        print('Error! File does not exist or invalid.')


def empty_prof_data(rus):
    if rus:
        print('Файл профиля пути пуст.')
    else:
        print('Profile data is empty.')


def no_widened_data(rus):
    if rus:
        print('Невозможно рассчитать уклон. Проверьте данные массива.')
    else:
        print('Can not calculate the slope. Check the array data.')

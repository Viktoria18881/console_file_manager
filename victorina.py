def victorina():

    def check_year(year):
        while year != '1799':
            print("Неверно!")
            year = input('Ввведите год рождения А.С.Пушкина: ')

    def check_day(day):
        while day != '6':
            print("Неверно!")
            day = input('В какой день июня родился Пушкин? ')

    check_year(input('Ввведите год рождения А.С.Пушкина: '))
    check_day(input('Ввведите день рождения Пушкин? '))
    print('Верно!')
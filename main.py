def make_dict():
    """Configure dictionary from file"""

    recipes = read_file()
    cook_book = {}
    counter = 0
    for i in range(0, len(recipes)):
        if recipes[i - 1] == '\n':
            counter = 0
        if counter == 0:
            cook_book[recipes[i][:-1]] = []
            for n in range(0, int(recipes[i + 1][:-1])):
                cook_book[recipes[i][:-1]].append({
                    'ingredient_name': recipes[i + 2 + n].split('|')[0].strip(),
                    'quantity': recipes[i + 2 + n].split('|')[1].strip(),
                    'measure': recipes[i + 2 + n].split('|')[2][:-1].strip()
                })
        counter += 1
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    """Count ingridients by dishes and persons"""

    cook_book = make_dict()
    shop_list = {}
    for dish in cook_book:
        if dish in dishes:
            for ingridient in cook_book[dish]:
                shop_list[ingridient['ingredient_name']] = {
                    'measure': ingridient['measure'],
                    'quantity': int(ingridient['quantity']) * person_count
                }

    return shop_list


def read_file():
    """Read cook book from file"""
    with open('recipes.txt', 'r', encoding='utf-8') as file:
        result = file.readlines()
    return result


def main():
    """Main function"""

    # print(make_dict(), '\n')  # Задача №1
    # print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2), '\n')  # Задача №2


if __name__ == "__main__":
    main()

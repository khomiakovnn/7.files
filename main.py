def make_dict():
    """Configure dictionary cook_book from recipes.txt file, task 1"""

    recipes = read_file("recipes.txt")
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
    """Count ingridients by dishes and persons, task 2"""

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


def string_processing(txt_files, result_file):
    """String processing from 3 txt files. Task 3"""

    count = {}
    result = []
    for file in txt_files:
        strings = read_file(file)
        count[file] = [len(strings)]
    sorted_count = sorted(count.items(), key=lambda x: x[1][0])
    for file in sorted_count:
        strings = read_file(file[0])
        result.append(str(file[0]) + '\n')
        result.append(str(file[1]).replace('[', '').replace(']', '') + '\n')
        for string in strings:
            result.append(string.replace('\n', '') + '\n')
    write_file(result, result_file)


def read_file(txt_file):
    """Read cook book from file"""
    with open(txt_file, 'r', encoding='utf-8') as file:
        result = file.readlines()
    return result


def write_file(content, filename):
    """Write string processing to file"""
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(content)
    print(f'file {filename} was created')


def main():
    """Main function"""

    # print(make_dict())  # Задача №1
    # print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))  # Задача №2
    # string_processing(['lines_1.txt', 'lines_2.txt', 'lines_3.txt'], 'result.txt') # Задача №3


if __name__ == "__main__":
    main()

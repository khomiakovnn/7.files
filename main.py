def find_dishes(recipes):
    """Finde all names of dishes"""

    cook_book = {}
    counter = 0
    for i in range(0, len(recipes)):
        if recipes[i - 1] == '\n':
            counter = 0
        if counter == 0:
            cook_book[recipes[i][:-1]] = []
            for n in range(0, int(recipes[i + 1][:-1])):
                cook_book[recipes[i][:-1]].append({
                    'ingredient_name': recipes[i + 2 + n].split('|')[0],
                    'quantity': recipes[i + 2 + n].split('|')[1],
                    'measure': recipes[i + 2 + n].split('|')[2][:-1]
                })
        counter += 1
    return cook_book


def main():
    """Main function"""
    with open('recipes.txt', 'r', encoding='utf-8') as file:
        result = file.readlines()

    print(find_dishes(result))


if __name__ == "__main__":
    main()

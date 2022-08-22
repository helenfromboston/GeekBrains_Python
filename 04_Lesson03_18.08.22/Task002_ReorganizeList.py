# Задача 2. При работе с документацией менеджер допустил ошибку,
# названия товаров перемешались с ценами. Помогите восстановить документ.
# Порядковый номер товара совпадает с номером цены.
# туфли рубашка 2000 1000 шарф юбка шорты 1500 3000 сапоги 500 5000 брюки 1500 2000 свитер

# Решение Сергея

def sort_product(list_of_products):
    new_list = list_of_products[0].split(' ')
    list_product = []
    list_cost = []
    for i in range(len(new_list)):
        if new_list[i].isdigit():
            list_cost.append(new_list[i])
        elif new_list[i].isalpha():
            list_product.append(new_list[i])
        elif "\n" in new_list[i]:
            tmp = new_list[i].split('\n')
            if new_list[i].isdigit():
                list_cost.append(tmp[0])
            else:
                list_cost.append(tmp[0])

    return list_product, list_cost


def write_file(list_of_products, list_of_costs):
    for i in range(len(list_of_products)):
        with open('sort_file.txt', 'a', encoding='utf-8') as file:
            file.writelines(f'{list_of_products[i]} {list_of_costs[i]}\n')


def read_file():
    data = None
    with open("products.txt", 'r', encoding='utf-8') as file:
        data = file.readlines()

    return data


list_products = read_file()
products, costs = sort_product(list_products)
write_file(products, costs)

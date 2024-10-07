from operator import itemgetter

cook_book = {}
with open('recipes.txt', encoding='utf-8') as f:
    for line in f:
        recepie_name = line.strip()
        ingredients_count = f.readline()
        ingredients = []
        for p in range(int(ingredients_count)):
            recepie = f.readline().strip().split(' | ')
            product, quantity, word = recepie
            ingredients.append({'product': product, 'quantity': quantity, 'measure': word})
        f.readline()
        cook_book[recepie_name] = ingredients

print(cook_book)
print()

         
def get_shop_list_by_dishes(dishes: list, person_count: int):
    shopping_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['product'] in shopping_list:
                    shopping_list[ingredient['product']]['quantity'] += int(ingredient['quantity']) * person_count
                else:
                    shopping_list[ingredient['product']] = {'measure': ingredient['measure'],'quantity': (int(ingredient['quantity']) * person_count)}
        else:
            print('Блюдо не найдено')
    print(shopping_list)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print()


def count_line(*files):
	list_of_files = []
	text_f = []		
	for file in files:
		with open(file, encoding = 'utf-8') as file_obj:
			text_f = file_obj.read().splitlines()
			file_length = len(text_f)
			name_file = file
			list_of_files.append([name_file, file_length, text_f])
			list_of_files.sort(key = itemgetter(1))
	print(list_of_files)
	return list_of_files

count_line = count_line('1.txt', '2.txt', '3.txt')
a = 'result.txt'


def writing_file(list_of_files,a):
	with open('result.txt', 'w', encoding='utf-8') as file_obj:
		for file in list_of_files:
			for element in file:
				file_obj.write(f'{element}\n')			
	file_path = 'result.txt'
	return file_path


print(writing_file(count_line, 'result.txt'))
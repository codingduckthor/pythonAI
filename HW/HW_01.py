# 1.	Найти сумму чётных чисел в списке
#
# nums = [1, 13, 10, 4, 8, 9, 11, 22]
#
# def sum_of_even_nums(lst):
#     sum = 0
#     for i in lst:
#         if i % 2 == 0:
#             sum += i
#     print(f"Sum of all even numbers in the list: {sum}")
#
# sum_of_even_nums(nums)



# 2.	Словарь товаров → найти самый дорогой

# products = {
#     "apple": 1.20,
#     "banana": 0.80,
#     "milk": 1.50,
#     "bread": 1.10,
#     "cheese": 2.75,
#     "chicken": 4.30
# }
#
# def most_expensive(dct):
#     product = max(dct, key = dct.get)
#     max_price = dct[product]
#     print(f"Most expensive product: {product} ${max_price}")
#
# most_expensive(products)



# 3.	Список оценок → сколько >= 10

# grades = [15, 4, 13, 5, 2, 14, 5]
#
# def bigger_that_ten(grds):
#     result = []
#     for i in grds:
#         if i >= 10:
#             result.append(i)
#     print(result)
#
# bigger_that_ten(grades)



# 4.	Анкета ученика (dict)

# student = {
#     "name": "Alex",
#     "age": 16,
#     "grade": 10,
#     "average_score": 4.5,
#     "city": "Almaty"
# }
#
# for key, value in student.items():
#     print(f"{key}: {value}")



# 5.	Мини-опрос (input → список → анализ)

yes_count = 0
no_count = 0

questions = [
    "Do you like programming? (yes/no): ",
    "Do you like math? (yes/no): ",
    "Do you like Python? (yes/no): "
]

for q in questions:
    answer = input(q).lower()
    if answer == "yes":
        yes_count += 1
    elif answer == "no":
        no_count += 1

print("Yes answers:", yes_count)
print("No answers:", no_count)


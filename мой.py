# # 1. user_data funksiyasi
# def user_data(first_name, last_name, age):
#     print(f"Ism: {first_name}")
#     print(f"Familiya: {last_name}")
#     print(f"Yosh: {age}")
#
# user_data("Alisher", "Olimov", 27)
#
#
# def find_max(a, b, c):
#     max_val = max(a, b, c)
#     results = []
#     if a == max_val:
#         results.append("A")
#     if b == max_val:
#         results.append("B")
#     if c == max_val:
#         results.append("C")
#     print(f"Eng katta son - {' va '.join(results)} = {max_val}")
#
# # Misol uchun
# find_max(10, 10, 5)
#
#
# def find_letter_count(word, letter):
#     count = word.lower().count(letter.lower())
#     print(f'"{word}" so‘zida "{letter}" dan {count} ta.')
#
# # Misol uchun
# find_letter_count("Programing", "r")
#
#
#
# def list_sum(myList):
#     print("Listning elementlar yig'indisi =", sum(myList))
#
# # Misol uchun
# list_sum([5, 10, 7, 10])
#
#
#
# def daraja(a, b):
#     print(a ** b)
#
# daraja(2, 3)
#
#
#
# def daraja4(a, b, c, d):
#     print(a ** b, a ** c, a ** d)
#
# daraja4(2, 2, 3, 4)
#
#
#
# def digit_count_and_sum(word):
#     digits = [int(ch) for ch in word if ch.isdigit()]
#     print("Raqamlar soni:", len(digits))
#     print("Raqamlar yig‘indisi:", sum(digits))
#
# digit_count_and_sum("salom123dunyo45")
#
#
#
# def add_right(a, b):
#     print(int(str(a) + str(b)))
#
# add_right(123, 45)
#
#
#
# def add_left(a, b):
#     print(int(str(b) + str(a)))
#
# add_left(123, 45)
#
#
# # 10. work_with_list funksiyasi
# def work_with_list(a):
#     min_val = min(a)
#     new_list = [x * min_val for x in a]
#     print(new_list)
#
# work_with_list([2, 5, 3, 7])
#
#
#
# def big_sales(sales):
#     max_month = max(sales, key=sales.get)
#     return max_month
#
# sales = {
#   "yanvar": 12000,
#   "mart": 6000,
#   "aprel": 15000,
#   "sentabr": 9000,
#   "dekabr": 10000,
# }
# print("Eng ko‘p sotuv bo‘lgan oy:", big_sales(sales))
#
#
#
# def min_max(numbers, max_num, min_num):
#     if max_num == max(numbers):
#         print(f"{max_num} eng katta son ✅")
#     else:
#         print(f"{max_num} eng katta son emas ")
#     if min_num == min(numbers):
#         print(f"{min_num} eng kichik son ✅")
#     else:
#         print(f"{min_num} eng kichik son emas ")
#
# min_max([3, 8, 1, 5, 10], 10, 1)



def expensiveProduct(products):
    max_product = max(products, key=lambda x: x["price"])
    print("Eng qimmat telefon:", max_product["name"])

products = [
    {"name": "Iphone X", "price": 600},
    {"name": "Iphone 12", "price": 1500},
    {"name": "Samsung Note 9", "price": 800},
    {"name": "Samsung S10", "price": 1100},
]
expensiveProduct(products)

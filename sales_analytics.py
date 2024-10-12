import csv # для работы с исходными данными
from collections import defaultdict # для упрощения работы с подсчетами
import matplotlib.pyplot as plt
#Функция чтения данных из файла
def read_sales_data(file_path):
    sales_data = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:#Каждая строка файла преобразуется в список значений
            product_name = row[0]
            quantity = int(row[1])
            price = float(row[2])
            date = row[3]
            sales_data.append({#Создание словаря с ключами
                'product_name': product_name,
                'quantity': quantity,
                'price': price,
                'date': date
            })
    return sales_data
def total_sales_per_product(sales_data):
    product_sales = defaultdict(float)
    for sale in sales_data:
        total = sale['quantity'] * sale['price']  # Общая выручка за одну продажу
        product_sales[sale['product_name']] += total  # Сумма выручки для каждого продукта
    return dict(product_sales)
def sales_over_time(sales_data):
    sales_by_date = defaultdict(float)
    for sale in sales_data:
        total = sale['quantity'] * sale['price']  # Общая выручка за одну продажу
        sales_by_date[sale['date']] += total  # Сумма выручки для каждой даты
    return dict(sales_by_date)
def plot_sales_data(product_sales, sales_by_date):
    products = list(product_sales.keys())
    sales = list(product_sales.values())
    plt.figure(figsize=(10, 5))
    plt.bar(products, sales, color='yellow', edgecolor = 'black')
    plt.title('Общая сумма продаж по продуктам')
    plt.xlabel('Продукты')
    plt.ylabel('Сумма продаж')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    dates = list(sales_by_date.keys())
    sales = list(sales_by_date.values())
    plt.figure(figsize=(10, 5))
    plt.bar(dates, sales, color='cyan', edgecolor = 'black')
    plt.title('Общая сумма продаж по дням')
    plt.xlabel('Дата')
    plt.ylabel('Сумма продаж')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
file_path = 'sales_data.csv'
sales_data = read_sales_data(file_path)
product_sales = total_sales_per_product(sales_data)
sales_by_date = sales_over_time(sales_data)
best_selling_product = max(product_sales, key=product_sales.get)
print(f'Продукт с наибольшей выручкой: {best_selling_product}, Сумма: {product_sales[best_selling_product]:.2f}')
best_sales_day = max(sales_by_date, key=sales_by_date.get)
print(f'День с наибольшими продажами: {best_sales_day}, Сумма: {sales_by_date[best_sales_day]:.2f}')
plot_sales_data(product_sales, sales_by_date)
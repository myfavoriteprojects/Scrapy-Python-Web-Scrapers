import csv
reviews_base_url = 'https://www.amazon.com/product-reviews/{}'
products_base_url = 'https://www.amazon.com/dp/{}'


def getAsinList() -> list:
    asin_list = []
    with open('collect_data/config/asin.csv', 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i==0:
                continue #header
            if row[0]:
                asin_list.append(row[0])
        return asin_list


print(getAsinList())
asinList = getAsinList()

# asin_list = [
#     'B07RXGDQ4Y'

# ]

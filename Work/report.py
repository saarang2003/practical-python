# import csv;
# from collections import defaultdict

# portfolio = [
#     ('GOOG', 100, 490.1),
#     ('IBM', 50, 91.1),
#     ('CAT', 150, 83.44),
#     ('IBM', 100, 45.23),
#     ('GOOG', 75, 572.45),
#     ('AA', 50, 23.15)
# ]

# holdings = defaultdict(list)
# for name, shares, price in portfolio:
#     holdings[name].append((shares, price))
# # print(holdings['IBM'])


# import csv
# f = open('Data/portfolio.csv')
# rows = csv.reader(f)
# headers = next(rows)
# headers

# def read_prices(filename):
#     prices = {}
#     with open(filename) as f:
#         f_csv = csv.reader(f)
#         for row in f_csv:
#             prices[row[0]] = float(row[1])
#     return prices

# def read_portfolio(filename):
#     '''
#     Read a stock portfolio file into a list of dictionaries with keys
#     name, shares, and price.
#     '''
#     portfolio = []
#     with open(filename) as f:
#         rows = csv.reader(f)
#         headers = next(rows)

#         for row in rows:
#             record = dict(zip(headers, row))
#             stock = {
#                 'name' : record['name'],
#                 'shares' : int(record['shares']),
#                 'price' : float(record['price'])
#             }
#             portfolio.append(stock)
#     return portfolio

# def parse_csv(filename):
#     '''
#     Parse a CSV file into a list of records
#     '''
#     with open(filename) as f:
#         rows = csv.reader(f)

#         # Read the file headers
#         headers = next(rows)
#         records = []
#         for row in rows:
#             if not row:    # Skip rows with no data
#                 continue
#             record = dict(zip(headers, row))
#             records.append(record)

#     return records


# print(parse_csv('Data/portfolio.csv'))


def read_data(lines):
    records = []
    for line in lines:
        ...
        records.append(r)
    return records

with open('Data/file.csv') as f:
    d = read_data(f)
    print(d)


class Player:
    def __init__(self , x, y):
        self.x = x
        self.y = y
        self.health = 100
        
    def move(self , x, y):
        self.x = x
        self.y = y
    
    def damage(self , pts):
        self.health -= pts

# report.py
"""
Requirements: 현재 보유한 주식을 확인하고 업데이트된 가격을 확인한 후 최종 수익이 얼마인지 확인하는 프로그램을작성하시오
보유한 주식은 portpolio.csv를 통해 기록이 되어 있고 
보유주식은 name shares price로 구성 되어 있음 현재 price는 구매시 unit price이고 
현재 주식의 가격 변동은 price.csv를 통해 확인 할 수 있음. 

Problem Define:
1. 보유 주식의 portpolio를  'portpolio.csv'를 통해 확인
2. 현재 가격이 얼마인지 price를 'price.csv'통해 확인
3. portpolio와 price 가격 비교를 통해 total cost와 total gain을 구할 것 

"""
#
import csv

"""
Name:
precondition: 
Method:
Post:
"""
def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = []
    
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            stock = {
                 'name'   : row[0],
                 'shares' : int(row[1]),
                 'price'   : float(row[2])
            }
            portfolio.append(stock)
            
    return portfolio

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
  
    return prices

portfolio = read_portfolio('portfolio.csv')
prices    = read_prices('prices.csv')

# Calculate the total cost of the portfolio
total_cost = 0.0
# each element of portpolio

# Compute the current value of the portfolio
total_value = 0.0
# each element of portpolio 
# find the name of stock in price list


print('Current value', total_value)

# Compute Gain
print('Gain', total_value - total_cost)

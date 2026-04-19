from dataclasses import dataclass
from datetime import date
@dataclass
class DailyStockPrice:
    openPrice: float
    closePrice: float
    date: date
    stockName: str
@dataclass
class AverageStockPrice:
    price: float
    startOfAveragePeriod: date
    endOfAveragePeriod: date
    stockName:str
    
    
def CalculateWeeklyPriceOfStocks(stockPrices: list[DailyStockPrice])-> list[AverageStockPrice]:
    # Description: processes a collection of stock data and computes the average weekly price for each stock
    
    # Parameters:
    #   - stockPrices (list[DailyStockPrice]): a list of DailyStockPrice objects that store the OpenPrice, ClosePrice, StockName of a stock and the Date of recording. daily stock prices must fall inside a monday->friday week.
    # Outputs:
    #   - list[float]: a list of floats that is the weekly average of each stock price
    
    
    # Preconditions:
    #   The list must contain instances of type StockPrice
    #   The list must be 
    
    # Post-Conditions:
    #   Returns a list of AverageStockPrices, where each AverageStockPrice is the average of the daily stock prices for each stock in the list
    
    pass


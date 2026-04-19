import unittest
from lab2_34 import AverageStockPrice, CalculateWeeklyPriceOfStocks, DailyStockPrice
from datetime import date
class TestCalculateWeeklyPriceOfStocks(unittest.TestCase):
    def TestTypicalUsage(self):
        stockPrices = [
            DailyStockPrice(10,50,date(2026,4,13),"APPL"),DailyStockPrice(50,20,date(2026,4,14),"APPL"), DailyStockPrice(20,100,date(2026,4,17),'APPL')
        ]
        self.assertEqual(CalculateWeeklyPriceOfStocks(stockPrices),[AverageStockPrice(56.67,date(2026,4,13),date(2026,4,17),"APPL")])
    def TestEdgeCases(self):
        self.assertRaises(IndexError,CalculateWeeklyPriceOfStocks,[])
        self.assertRaises(TypeError,CalculateWeeklyPriceOfStocks,[10])
        self.assertRaises(TypeError,CalculateWeeklyPriceOfStocks,[str])
        self.assertRaises(IndexError,CalculateWeeklyPriceOfStocks,str)
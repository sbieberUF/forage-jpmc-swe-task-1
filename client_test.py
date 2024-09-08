import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            self.assertEqual(stock, quote['stock'])
            self.assertEqual(bid_price, quote['top_bid']['price'])
            self.assertEqual(ask_price, quote['top_ask']['price'])
            self.assertEqual(price, (quote['top_bid']['price'] + quote['top_ask']['price']) / 2)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            self.assertEqual(stock, quote['stock'])
            self.assertEqual(bid_price, quote['top_bid']['price'])
            self.assertEqual(ask_price, quote['top_ask']['price'])
            self.assertEqual(price, (quote['top_bid']['price'] + quote['top_ask']['price']) / 2)


  """ ------------ Add more unit tests ------------ """
  def test_getDataPoint_calculatePriceZero(self):
    quotes = [
        {'top_ask': {'price': 0.0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0.0, 'size': 109}, 'stock': 'ABC'},
        {'top_ask': {'price': 0.0, 'size': 10}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0.0, 'size': 50}, 'stock': 'DEF'}
    ]
    for quote in quotes:
        stock, bid_price, ask_price, price = getDataPoint(quote)
        self.assertEqual(bid_price, 0.0)
        self.assertEqual(ask_price, 0.0)
        self.assertEqual(price, 0.0)  
        self.assertEqual(stock, quote['stock'])  

if __name__ == '__main__':
    unittest.main()

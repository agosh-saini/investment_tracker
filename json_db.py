import json
from typing import Dict, Union, Type

class stock_holding:
    def __init__(self, account: Type[str], 
                 symbol: Type[str], 
                 quantity: Type[int], 
                 last_price: Type[float], 
                 exchange: Type[str]) -> None:
        self.account = account
        self.symbol = symbol
        self.quantity = quantity
        self.last_price = last_price
        self.exchange = exchange

        return None

    def to_dict(self) -> Dict[str, Union[str, int]]:
        return {
            "account": self.account,
            "symbol": self.symbol,
            "quantity": self.quantity,
            "last_price": self.last_price,
            "exchange": self.exchange
        }

    def add_stock_info(self, stock_info: dict) -> Dict[str, Union[str, int]]:
        self.symbol = stock_info["symbol"]
        self.last_price = stock_info["last_price"]
        self.exchange = stock_info["exchange"]
        self.quantity = stock_info["quantity"]
        self.account = stock_info["account"]

        return self.to_dict()
    
class stock_portfolio:

    def __init__(self) -> None:

        self.stock_holdings = []

        return None

    def add_stock_holding(self, stock_info: dict) -> None:
        stock = stock_holding(stock_info["account"], 
                              stock_info["symbol"], 
                              stock_info["quantity"], 
                              stock_info["last_price"], 
                              stock_info["exchange"])
        self.stock_holdings.append(stock.to_dict())

        return None

    def to_json(self) -> None:
        with open("stock_holdings.json", "a") as file:
            json.dump(self.stock_holdings, file, indent=4)
        return None


if __name__ == "__main__":

    # Create a list to store the stock holdings
    stock_holdings = []

    # Add a sample stock holding
    stock_holdings.append({
        "account": "Brokerage Account",
        "symbol": "AAPL",
        "quantity": 10,
        "last_price": 150.25,
        "exchange": "NASDAQ"
    })


    # Write the stock holdings to a JSON file
    with open("stock_holdings.json", "w") as file:
        json.dump(stock_holdings, file, indent=4)
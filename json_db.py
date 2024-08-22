import json
from typing import Dict, Union, Type
from os.path import exists as file_exists

class stock_holding:

    '''
    Class to represent a stock holding in a portfolio

    Attributes:
        account: str
            Account in which the stock is held
        symbol: str
            Symbol of the stock
        quantity: int
            Quantity of the stock
        last_price: float
            Last price of the stock
        exchange: str
            Exchange on which the stock is traded
        type: str
            Type of the stock
        sector: str
            Sector of the stock
        industry: str
            Industry of the stock

    Methods:
        to_dict() -> Dict[str, Union[str, int, float]]:
            Convert the stock holding to a dictionary
        add_stock_info(stock_info: dict) -> None:
            Add stock information to the stock holding

    Description:
    The stock_holding class is used to represent a stock holding in a portfolio.
    '''

    def __init__(self, account: Union[str, None] = None,
                 symbol: Union[str, None] = None,
                 quantity:  Union[int, None] = None,
                 last_price:  Union[float, None] = None,
                 exchange:  Union[str, None] = None,
                 type: Union[str, None] = None,
                 sector: Union[str, None] = None,
                 industry: Union[str, None] = None) -> None:

        '''
        Constructor for the stock_holding class

        Parameters:
            account: Union[str, None]
                Account in which the stock is held
            symbol: Union[str, None]
                Symbol of the stock
            quantity: Union[int, None]
                Quantity of the stock
            last_price: Union[float, None]
                Last price of the stock
            exchange: Union[str, None]
                Exchange on which the stock is traded
            type: Union[str, None]
                Type of the stock
            sector: Union[str, None]
                Sector of the stock
            industry: Union[str, None]
                Industry of the stock

        Returns:
            None

        Description:
        The constructor initializes the account, symbol, quantity, last_price, exchange, type, sector, and industry attributes of the class.
        '''

        self.symbol = symbol
        self.type = type
        self.last_price = last_price
        self.exchange = exchange
        self.quantity = quantity
        self.account = account
        self.sector = sector
        self.industry = industry

        return None

    def to_dict(self) -> Dict[str, Union[str, int, float]]:

        '''
        Method to convert the stock holding to a dictionary

        Parameters:
            None

        Returns:
            Dict[str, Union[str, int, float]]:
                Dictionary representation of the stock holding

        Description:
        The method converts the stock holding to a dictionary and returns the dictionary.
        '''

        return {
            "account": self.account,
            "symbol": self.symbol,
            "quantity": self.quantity,
            "last_price": self.last_price,
            "exchange": self.exchange,
            "type": self.type,
            "sector": self.sector,
            "industry": self.industry
        }

    def add_stock_info(self, 
                        account: Union[str, None] = None,
                        symbol: Union[str, None] = None, 
                        quantity: Union[float, None] = None, 
                        last_price: Union[float, None] = None, 
                        exchange: Union[str, None] = None, 
                        sector: Union[str, None] = None, 
                        industry: Union[str, None] = None, 
                        type: Union[str, None] = None) -> None:

        '''
        Method to add stock information to the stock holding

        Parameters:
            account: Union[str, None]
                Account in which the stock is held
            symbol: Union[str, None]
                Symbol of the stock
            quantity: Union[float, None]
                Quantity of the stock
            last_price: Union[float, None]
                Last price of the stock
            exchange: Union[str, None]  
                Exchange on which the stock is traded
            sector: Union[str, None]
                Sector of the stock
            industry: Union[str, None]
                Industry of the stock
            type: Union[str, None]
                Type of the stock

        Returns:
            None

        Description:
        The method takes a dictionary containing stock information as input and adds the information to the stock holding.
        '''

        self.symbol = symbol
        self.type = type
        self.last_price = last_price
        self.exchange = exchange
        self.quantity = quantity
        self.account = account
        self.sector = sector
        self.industry = industry

        return None
    
class stock_portfolio:

    '''
        Class to represent a stock portfolio

        Attributes:
            stock_holdings: List[Dict[str, Union[str, int]]]
                List of stock holdings in the portfolio
            
        Methods:
            add_stock_holding(stock_info: dict) -> None:
                Add a stock holding to the portfolio
            to_json() -> None:
                Write the stock holdings to a JSON file
        
        Description:
            The stock_portfolio class is used to represent a stock portfolio.
            The class has a list of stock holdings as an attribute and methods to add a stock holding to the portfolio and write the stock holdings to a JSON file.
    '''

    def __init__(self) -> None:

        '''
            Constructor for the stock_portfolio class

            Parameters:
                None
            
            Returns:
                None
            
            Description:
                The constructor initializes the stock_holdings attribute as an empty list.
        '''
        if file_exists("stock_holdings.json") == False:  
                self.stock_holdings = []
        else:
            with open("stock_holdings.json", "r") as file:
                self.stock_holdings = json.load(file)
        return None

    def get_portfolio(self, account: str) -> Dict[str, Union[str, int]]:
        '''
            Method to get the stock holdings for an account

            Parameters:
                account: str
                    Account for which the stock holdings are to be retrieved

            Returns:
                Dict[str, Union[str, int]]
                    Stock holdings for the account

            Description:
                The method takes an account as input and returns the stock holdings for the account.
        '''
        if file_exists("stock_holdings.json") == True:
            portfolio = json.load(open("stock_holdings.json"))
            portfolio = [holding for holding in portfolio if holding["account"] == account]
        else:
            portfolio = []

        return portfolio
            
    def add_stock_holding(self, stock_info: dict) -> None:

        '''
            Method to add a stock holding to the portfolio

            Parameters:
                stock_info: dict
                    Dictionary containing stock information
            Returns:
                None
            
            Description:    
                The method takes a dictionary containing stock information as input and adds the stock holding to the portfolio.
        '''

        if file_exists("stock_holdings.json") == True:
            with open("stock_holdings.json", "r") as file:
                stock_holdings = json.load(file)
    
            for holding in stock_holdings:
                if holding["account"] == stock_info["account"] and holding["symbol"] == stock_info["symbol"]:
                    holding["quantity"] = stock_info["quantity"]
                    holding["last_price"] = stock_info["last_price"]
                    holding["exchange"] = stock_info["exchange"]
                    break
            else:
                stock_holdings.append(stock_info)
    
            self.stock_holdings = stock_holdings
        
        else:
            self.stock_holdings.append(stock_info)

        return None

    def to_json(self) -> None:
        
        '''
            Method to write the stock holdings to a JSON file

            Parameters:
                None
            
            Returns:
                None
            
            Description:
                The method writes the stock holdings to a JSON file named "stock_holdings.json".
        '''

        with open("stock_holdings.json", "w") as file:
            json.dump(self.stock_holdings, file, indent=4)

        return None


    
    def get_stock_holding(self, account: str, symbol: str) -> Dict[str, Union[str, int]]:

        '''
            Method to get information about a stock holding

            Parameters:
                account: str
                    Account in which the stock is held
                symbol: str
                    Symbol of the stock

            Returns:
                Dict[str, Union[str, int]]
                    Information about the stock holding

            Description:
                The method takes an account and a symbol as input and returns information about the stock holding.
        '''
        
        portfolio = self.get_portfolio(account)
        stock_holding = [holding for holding in portfolio if holding["symbol"] == symbol]

        return stock_holding


if __name__ == "__main__":

    # Create a stock portfolio
    portfolio = stock_portfolio()
    stock_information = stock_holding()

    # Add a stock holding to the portfolio
    stock_information.add_stock_info(account="Brokerage", 
                                     symbol="AAPL", 
                                     quantity=100, 
                                     last_price=150.0, 
                                     exchange="NASDAQ", 
                                     sector="Technology", 
                                     industry="Consumer Electronics", 
                                     type="Common Stock")
    
    stock_info = stock_information.to_dict()

    portfolio.add_stock_holding(stock_info)

    # Add another stock holding to the portfolio
    stock_information.add_stock_info(account="Retirement", 
                                     symbol="AMZN", 
                                     quantity=50, 
                                     last_price=3200.0, 
                                     exchange="NASDAQ", 
                                     sector="Technology", 
                                     industry="E-commerce", 
                                     type="Common Stock")
    
    stock_info = stock_information.to_dict()

    portfolio.add_stock_holding(stock_info)

    # Add one more stock holding to the portfolio
    stock_information.add_stock_info(account="Savings", 
                                     symbol="GOOGL", 
                                     quantity=75, 
                                     last_price=2500.0, 
                                     exchange="NASDAQ", 
                                     sector="Technology", 
                                     industry="Internet Services", 
                                     type="Common Stock")
    
    stock_info = stock_information.to_dict()

    portfolio.add_stock_holding(stock_info)

    # Write the stock holdings to a JSON file
    portfolio.to_json()

    # Get information about a specific stock holding
    stock_holding_info = portfolio.get_stock_holding("Brokerage", "AAPL")
    print(stock_holding_info)


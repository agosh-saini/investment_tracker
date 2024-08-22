import finnhub
from typing import List, Dict, Union, Type
import api

class investment_info:

    '''
        Class to get investment information from the Finnhub API

        Attributes:
            api_key: str
                API key to access the API
            client: finnhub.Client
                Client object to access the API
        
        Methods:
            get_market_status(exchange: str) -> Dict[str, Union[str, bool]]:
                Get the market status of an exchange
            company_news(symbol: str, _from: str, to: str) -> List[Dict[str, Union[str, int]]]:
                Get the news of a company
            peers(symbol: str) -> List[Dict[str, Union[str, int]]]:
                Get the peers of a company
            stock_insider_transactions(symbol: str, _from: str, to: str) -> List[Dict[str, Union[str, int]]]:
                Get the insider transactions of a company
            recomendations(symbol: str) -> List[Dict[str, Union[str, int]]]:
                Get the recommendations of a company
            get_stock_quote(symbol: str) -> Dict[str, Union[str, int]]:
                Get the quote of a stock
        
        Description:
            The investment_info class is used to get investment information from the Finnhub API.
            The class has methods to get the market status of an exchange, the news of a company, the peers of a company, the insider transactions of a company, the recommendations of a company, and the quote of a stock.
    '''

    def __init__(self, api_key: Type[str]) -> None:

        '''
            Constructor for the investment_info class
            
            Parameters:
                api_key: str
                    API key to access the API
            
            Returns:
                None

            Description:
                The constructor initializes the api_key and client attributes of the class.
                The api_key is the API key to access the API, and the client is a finnhub.Client object to access the API.
        '''

        self.api_key = api_key
        self.client = finnhub.Client(api_key=self.api_key)

        return None
    
    def get_market_status(self, exchange: Type[str]) -> Dict[str, Union[str, bool]]:

        '''
            Method to get the market status of an exchange

            Parameters:
                exchange: str
                    Exchange code
            
            Returns:
                status: Dict[str, Union[str, bool]]
            
            Description:
                The method calls the market_status method of the client object to get the market status of the exchange.
                The method returns the status of the market
        '''

        status = self.client.market_status(exchange=exchange)

        return status

    def company_news(self, symbol: Type[str], _from: Type[str], to: Type[str]) -> List[Dict[str, Union[str, int]]]:
        
        '''
            Method to get the news of a company

            Parameters:
                symbol: str
                    Symbol of the company
                _from: str
                    Start date of the news
                to: str
                    End date of the news
            
            Returns:
                news: List[Dict[str, Union[str, int]]]

            Description:
                The method calls the company_news method of the client object to get the news of the company.
                The method returns the news of the company
        '''

        news = self.client.company_news(symbol=symbol, _from=_from, to=to)

        return news
    
    def peers(self, symbol: Type[str]) -> List[Dict[str, Union[str, int]]]:

        '''
            Method to get the peers of a company

            Parameters:
                symbol: str
                    Symbol of the company
            
            Returns:
                peers: List[Dict[str, Union[str, int]]]

            Description:
                The method calls the company_peers method of the client object to get the peers of the company.
                The method returns the peers of the company
        '''

        peers = self.client.company_peers(symbol=symbol)

        return peers

    def stock_insider_transactions(self, symbol: Type[str], _from: Type[str], to: Type[str]) -> List[Dict[str, Union[str, int]]]:

        '''
            Method to get the insider transactions of a company

            Parameters:
                symbol: str
                    Symbol of the company
                _from: str
                    Start date of the transactions
                to: str
                    End date of the transactions
            
            Returns:
                trades: List[Dict[str, Union[str, int]]]

            Description:
                The method calls the stock_insider_transactions method of the client object to get the insider transactions of the company.
                The method returns the insider transactions of the company
        '''

        trades = self.client.stock_insider_transactions(symbol=symbol, _from=_from, to=to)

        return trades
    
    def recomendations(self, symbol: Type[str]) -> List[Dict[str, Union[str, int]]]:

        '''
            Method to get the recommendations of a company

            Parameters:
                symbol: str
                    Symbol of the company
            
            Returns:
                recomendations: List[Dict[str, Union[str, int]]]

            Description:
                The method calls the recommendation_trends method of the client object to get the recommendations of the company.
                The method returns the recommendations of the company
        '''

        recomendations = self.client.recommendation_trends(symbol=symbol)

        return recomendations

    def get_stock_quote(self, symbol: Type[str]) -> Dict[str, Union[str, int]]:

        '''
            Method to get the quote of a stock

            Parameters:
                symbol: str
                    Symbol of the stock
            
            Returns:
                quote: Dict[str, Union[str, int]]

            Description:
                The method calls the quote method of the client object to get the quote of the stock.
                The method returns the quote of the stock
        '''

        quote = self.client.quote(symbol=symbol)
        
        return quote
    
if __name__ == "__main__":
    # Example usage
    api_key = api.APIKeys.finhub_api_key
    tracker = investment_info(api_key)

    # Get market status
    exchange = "US"
    market_status = tracker.get_market_status(exchange)
    print("Market Status:", market_status)

    # Get company news
    symbol = "AAPL"
    start_date = "2022-01-01"
    end_date = "2022-01-31"
    news = tracker.company_news(symbol=symbol, _from=start_date, to=end_date)
    print("Company News:", news)

    # Get peers
    symbol = "AAPL"
    peers = tracker.peers(symbol=symbol)
    print("Peers:", peers)

    # Get insider transactions
    symbol = "AAPL"
    start_date = "2022-01-01"
    end_date = "2022-01-31"
    insider_transactions = tracker.stock_insider_transactions(symbol=symbol, _from=start_date, to=end_date)
    print("Insider Transactions:", insider_transactions)

    # Get recommendations
    symbol = "AAPL"
    recommendations = tracker.recomendations(symbol=symbol)
    print("Recommendations:", recommendations)

    # Get stock quote
    symbol = "AAPL"
    quote = tracker.get_stock_quote(symbol=symbol)
    print("Stock Quote:", quote)

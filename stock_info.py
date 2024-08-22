import finnhub
from typing import List, Dict, Union, Type
import api

class investment_info:
    def __init__(self, api_key: Type[str]) -> None:
        self.api_key = api_key
        self.client = finnhub.Client(api_key=self.api_key)
        return None
    
    def get_market_status(self, exchange: Type[str]) -> Dict[str, Union[str, bool]]:
        status = self.client.market_status(exchange=exchange)
        return status

    def company_news(self, symbol: Type[str], _from: Type[str], to: Type[str]) -> List[Dict[str, Union[str, int]]]:
        news = self.client.company_news(symbol=symbol, _from=_from, to=to)
        return news
    
    def peers(self, symbol: Type[str]) -> List[Dict[str, Union[str, int]]]:
        peers = self.client.company_peers(symbol=symbol)
        return peers

    def stock_insider_transactions(self, symbol: Type[str], _from: Type[str], to: Type[str]) -> List[Dict[str, Union[str, int]]]:
        trades = self.client.stock_insider_transactions(symbol=symbol, _from=_from, to=to)
        return trades
    
    def recomendations(self, symbol: Type[str]) -> List[Dict[str, Union[str, int]]]:
        recomendations = self.client.recommendation_trends(symbol=symbol)
        return recomendations

    def get_stock_quote(self, symbol: Type[str]) -> Dict[str, Union[str, int]]:
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

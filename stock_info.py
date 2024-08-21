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

    def get_company_profile_free(self, symbol: Type[str]=None, ISIN: Type[str]=None, cusip: Type[str]=None) -> Dict[str, Union[str, int]]:

        code_value = symbol if symbol is not None else ISIN if ISIN is not None else cusip

        if code_value is None:
            return ValueError("At least one of the parameters must be provided")

        profile = self.client.company_profile(symbol=code_value)
        return profile

    def company_news(self, symbol: Type[str], _from: Type[str], to: Type[str]) -> List[Dict[str, Union[str, int]]]:
        news = self.client.company_news(symbol=symbol, _from=_from, to=to)
        return news
    
    def peers(self, symbol: Type[str]) -> List[Dict[str, Union[str, int]]]:
        peers = self.client.peers(symbol=symbol)
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
    
    def country(self, symbol: Type[str]) -> Dict[str, Union[str, int]]:
        country = self.client.country(symbol=symbol)
        return country
    
if __name__ == "__main__":
    # Example usage
    api_key = api.APIKeys.finhub_api_key
    tracker = investment_info(api_key)
    quote = tracker.get_stock_quote('AAPL')
    profile = tracker.get_company_profile('AAPL')
    print(quote)
    print(profile)
import requests
import api
from typing import Type, Union, Dict

# need to fix urls for this

class ETFInfo:
    def __init__(self, base_url: Type[str], api_key: Type[str]) -> None:
        self.base_url = base_url
        self.api =  api_key
        return None
    
        
    def sector_weightings(self, symbol: Type[str]) -> Union[Dict[str, Union[str, int]], ValueError]:
        url = f"{self.base_url}/etf-sector-weightings/{symbol}?apikey={self.api}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            return ValueError("Invalid ETF symbol or API key")
    
    def country_weightings(self, symbol: Type[str]) -> Union[Dict[str, Union[str, int]], ValueError]:
        url = f"{self.base_url}/etf-country-weightings/{symbol}?apikey={self.api}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            return ValueError("Invalid ETF symbol or API key")
        

if __name__ == "__main__":
    # Example
    etf_info = ETFInfo(api.APIKeys.fmg_cloud_api_url, api.APIKeys.fmg_cloud_api_key)

    # Get sector weightings
    sectors = etf_info.sector_weightings("SPY")
    print(sectors)
    
    # Get country weightings
    countries = etf_info.country_weightings("SPY")
    print(countries)
    
    # Add more examples here
    # ...
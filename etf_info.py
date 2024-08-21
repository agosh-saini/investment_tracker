import requests
import api
from typing import Type, Union, Dict

# need to fix urls for this

class ETFInfo:
    def __init__(self, base_url: Type[str], api_key: Type[str]) -> None:
        self.base_url = base_url
        self.api_key =  api_key
        return None
    
    def get_etf_holders(self, symbol: Type[str]) -> Union[Dict[str, Union[str, int]], ValueError]:
        url = f"{self.base_url}/etf-holders/{symbol}?apikey={self.api}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            return ValueError("Invalid ETF symbol or API key")
        
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
    api_key = api.APIKeys.fmg_cloud_api_key
    base_url = api.APIKeys.fmg_cloud_api_url
    etf = ETFInfo(base_url, api_key)
    etf_info = etf.get_etf_info("SPY")
    print(etf_info)
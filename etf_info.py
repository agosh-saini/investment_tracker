import requests
import api
from typing import Type, Union, Dict

class ETFInfo:

    '''
        Class to get ETF information from the Financial Modeling Prep API

        Attributes:
            base_url: str
                Base URL for the API
            api_key: str
                API key to access the API
        Methods:
            sector_weightings(symbol: str) -> Union[Dict[str, Union[str, int]], ValueError]:
                Get the sector weightings of an ETF
            country_weightings(symbol: str) -> Union[Dict[str, Union[str, int]], ValueError]:
                Get the country weightings of an ETF
            
        Description:
            The ETFInfo class is used to get information about an ETF from the Financial Modeling Prep API.
            The class has two methods, sector_weightings and country_weightings, which return the sector and country weightings of an ETF, respectively.
            The methods take the ETF symbol as an argument and return a dictionary with the weightings.
            If the ETF symbol is invalid or the API key is invalid, the methods return a ValueError
    '''

    def __init__(self, base_url: Type[str], api_key: Type[str]) -> None:
        
        '''
            Constructor for the ETFInfo class

            Parameters:
                base_url: str
                    Base URL for the API
                api_key: str
                    API key to access the API
            
            Returns:
                None
            
            Description:
                The constructor initializes the base_url and api_key attributes of the class.
                The base_url is the base URL for the API, and the api_key is the API key to access the API.
        
        '''
        
        self.base_url = base_url
        self.api =  api_key
        return None
    
    def get_quote(self, symbol: Type[str]) -> Dict[str, Union[str, int]]:
        '''
            Method to get the quote of an ETF

            Parameters:
                symbol: str
                    Symbol of the ETF

            Returns:
                Union[Dict[str, Union[str, int]], ValueError]
                    A dictionary with the quote of the ETF, or a ValueError if the ETF symbol or API key is invalid
            
            Description:
                The get_quote method makes a request to the Financial Modeling Prep API to get the quote of an ETF.
                The method takes the ETF symbol as an argument and returns a dictionary with the quote.
                If the ETF symbol is invalid or the API key is invalid, the method returns a ValueError.
        '''
        url = f"{self.base_url}/quote-short/{symbol}?apikey={self.api}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            return ValueError(f'Status code: {response.status_code}. Invalid ETF symbol, API key or API URL')

        
    def sector_weightings(self, symbol: Type[str]) -> Dict[str, Union[str, int]]:

        '''
            Method to get the sector weightings of an ETF

            Parameters:
                symbol: str
                    Symbol of the ETF

            Returns:
                Union[Dict[str, Union[str, int]], ValueError]
                    A dictionary with the sector weightings of the ETF, or a ValueError if the ETF symbol or API key is invalid
            
            Description:
                The sector_weightings method makes a request to the Financial Modeling Prep API to get the sector weightings of an ETF.
                The method takes the ETF symbol as an argument and returns a dictionary with the sector weightings.
                If the ETF symbol is invalid or the API key is invalid, the method returns a ValueError.        
        '''

        url = f"{self.base_url}/etf-sector-weightings/{symbol}?apikey={self.api}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            return ValueError(f'Status code: {response.status_code}. Invalid ETF symbol, API key or API URL')
    
    def country_weightings(self, symbol: Type[str]) -> Dict[str, Union[str, int]]:
        '''
            Method to get the country weightings of an ETF

            Parameters: 
                symbol: str
                    Symbol of the ETF
            
            Returns:
                Union[Dict[str, Union[str, int]], ValueError]
                    A dictionary with the country weightings of the ETF, or a ValueError if the ETF symbol or API key is invalid
            
            Description:
                The country_weightings method makes a request to the Financial Modeling Prep API to get the country weightings of an ETF.
                The method takes the ETF symbol as an argument and returns a dictionary with the country weightings.
                If the ETF symbol is invalid or the API key is invalid, the method returns a ValueError.
        '''
        url = f"{self.base_url}/etf-country-weightings/{symbol}?apikey={self.api}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            return ValueError(f'Status code: {response.status_code}. Invalid ETF symbol, API key or API URL')
        

if __name__ == "__main__":
    # Example
    etf_info = ETFInfo(api.APIKeys.fmg_cloud_api_url, api.APIKeys.fmg_cloud_api_key)

    # Get quote
    quote = etf_info.get_quote("SPY")
    print(quote)

    # Get sector weightings
    sectors = etf_info.sector_weightings("SPY")
    print(sectors)
    
    # Get country weightings
    countries = etf_info.country_weightings("SPY")
    print(countries)
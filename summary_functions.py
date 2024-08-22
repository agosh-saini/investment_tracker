import pandas as pd
import numpy as np



from api import APIKeys
from json_db import stock_holding, stock_portfolio
from etf_info import ETFInfo
from stock_info import investment_info


from typing import List, Dict, Union, Type
from datetime import datetime

class SummaryFunctions:
    def __init__(self):
        self.api_key = APIKeys()
        self.etf_info = ETFInfo(self.api_key.fmg_cloud_api_key, self.api_key.fmg_cloud_api_url)
        self.stock_info = investment_info(self.api_key.finhub_api_key)
        self.stock_holding = stock_holding()
        self.stock_portfolio = stock_portfolio()

    def get_stock_holding(self, account: str, symbol: str) -> Dict[str, Union[str, int]]:
        '''
            Get information about a stock holding
            
            Parameters:
                account: str
                    Account in which the stock is held
                symbol: str
                    Symbol of the stock
            
            Returns:
                Dict[str, Union[str, int]]
                    Information about the stock holding
        '''
        
        stock_holding = self.stock_holding.get_stock_holding(account, symbol)

        return stock_holding

    def summarize_portfolio(self, account: str) -> Dict[str, Union[str, int]]:
        '''
            Summarize the portfolio
            
            Parameters:
                account: str
                    Account for which the portfolio is to be summarized
            
            Returns:
                Dict[str, Union[str, int]]
                    Summary of the portfolio
        '''
        
        portfolio = self.stock_portfolio.get_portfolio(account)

        return portfolio

    
    def get_all_stock_values(self, symbol: str) -> Dict[str, Union[str, float]]:
        '''
            Get information about a stock
            
            Parameters:
                symbol: str
                    Symbol of the stock
            
            Returns:
                Dict[str, Union[str, float]]
                    Information about the stock
        '''

        stock_info = {
                        "quote": self.investment_info.get_stock_quote(symbol),
                        "recommendations": self.investment_info.recomendations(symbol),
                        "insider_transactions": self.investment_info.get_insider_transactions(symbol),
                        "company_profile": self.investment_info.company_news(symbol),
                        "peers": self.investment_info.get_peers(symbol)
                        }
                               
        return stock_info
    
    def get_etf_info(self, symbol: str) -> Dict[str, Union[str, float]]:
        '''
            Get information about an ETF
            
            Parameters:
                symbol: str
                    Symbol of the ETF
            
            Returns:
                Dict[str, Union[str, float]]
                    Information about the ETF, Country, Sector
        '''

        etf_info = {
                        "quote": self.etf_info.get_quote(symbol),
                        "country": self.etf_info.sector_weightings(symbol),
                        "sector": self.etf_info.country_weightings(symbol)
                        }
        
        return etf_info

    




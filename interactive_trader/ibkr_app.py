
import pandas as pd
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.common import *
from ibapi.contract import *
from ibapi.order import *
from ibapi.order_state import OrderState
from datetime import datetime

# This is the main app that we'll be using for sync and async functions.
class ibkr_app(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.error_messages = pd.DataFrame(columns=[
            'reqId', 'errorCode', 'errorString'
        ])
        self.next_valid_id = None
        self.current_time = None
        self.historical_data = pd.DataFrame(
            columns=['date', 'open', 'high', 'low', 'close', 'volume',
                     'bar_count', 'average']
        )
        self.historical_data_end = None
        self.contract_details = None
        self.contract_details_end = None
        self.matching_symbols = None
        self.order_status = pd.DataFrame(
            columns=['orderId', 'status', 'filled', 'remaining', 'avgFillPrice',
                     'permId', 'parentId', 'lastFillPrice', 'clientId',
                     'whyHeld', 'mktCapPrice']
        )
        self.order_id_open = ""
        self.contract_open = ""
        self.order_open = ""
        self.order_state_open = ""
        self.contract_completed = ""
        self.order_completed = ""
        self.order_state_completed = ""


    def error(self, reqId:TickerId, errorCode:int, errorString:str):
        self.error_messages = pd.concat(
            [self.error_messages, pd.DataFrame({
                "reqId": [reqId],
                "errorCode": [errorCode],
                "errorString": [errorString]
            })])

    def managedAccounts(self, accountsList:str):
        self.managed_accounts = [i for i in accountsList.split(",") if i]

    def nextValidId(self, orderId:int):
        self.next_valid_id = orderId

    def currentTime(self, time:int):
        self.current_time = datetime.fromtimestamp(time)

    def historicalData(self, reqId:int, bar:BarData):
        self.historical_data = pd.concat(
            [
                self.historical_data,
                pd.DataFrame(
                    {
                        'date': [bar.date],
                        'open': [bar.open],
                        'high': [bar.high],
                        'low': [bar.low],
                        'close': [bar.close],
                    }
                )
            ],
            ignore_index=True
        )

    def historicalDataEnd(self, reqId:int, start:str, end:str):
        self.historical_data_end = reqId

    def contractDetailsEnd(self, reqId: int):
        self.contract_details_end = reqId

    def contractDetails(self, reqId:int, contractDetails:ContractDetails):
        self.contract_details = pd.DataFrame({
            "con_id": [contractDetails.contract.conId],
            "symbol": [contractDetails.contract.symbol],
            "long_name": [contractDetails.longName],
            "industry": [contractDetails.industry],
            "category": [contractDetails.category],
            "subcategory": [contractDetails.subcategory],
            "sec_type": [contractDetails.contract.secType],
            "stock_type": [contractDetails.stockType],
            "exchange": [contractDetails.contract.exchange],
            "primary_exchange": [contractDetails.contract.primaryExchange],
            "currency": [contractDetails.contract.currency],
            "local_symbol": [contractDetails.contract.localSymbol],
            "market_name": [contractDetails.marketName],
            "min_tick": [contractDetails.minTick],
            "order_types": [contractDetails.orderTypes],
            "valid_exchanges": [contractDetails.validExchanges],
            "price_magnifier": [contractDetails.priceMagnifier],
            "time_zone_id": [contractDetails.timeZoneId],
            "trading_hours": [contractDetails.tradingHours],
            "liquid_hours": [contractDetails.liquidHours]
        })

    def symbolSamples(self, reqId:int,
                      contractDescriptions:ListOfContractDescription):
        df = pd.DataFrame(
            columns=[
                'con_id', 'symbol', 'sec_type', 'primary_exchange', 'currency'
            ]
        )
        for contract_description in contractDescriptions:
            df = pd.concat([
                df,
                pd.DataFrame({
                    "con_id": [contract_description.contract.conId],
                    "symbol": [contract_description.contract.symbol],
                    "sec_type": [contract_description.contract.secType],
                    "primary_exchange": [
                        contract_description.contract.primaryExchange
                    ],
                    "currency": [contract_description.contract.currency]
                })
            ],
                ignore_index=True
            )
        self.matching_symbols = df

    def orderStatus(self, orderId:OrderId , status:str, filled:float,
                    remaining:float, avgFillPrice:float, permId:int,
                    parentId:int, lastFillPrice:float, clientId:int,
                    whyHeld:str, mktCapPrice: float):
        self.order_status = pd.concat(
            [
                self.order_status,
                pd.DataFrame({
                    'order_id': [orderId],
                    'status': [status],
                    'filled': [filled],
                    'remaining': [remaining],
                    'avg_fill_price': [avgFillPrice],
                    'perm_id': [permId],
                    'parent_id': [parentId],
                    'last_fill_price': [lastFillPrice],
                    'client_id': [clientId],
                    'why_held': [whyHeld],
                    'mkt_cap_price': [mktCapPrice]
                })
            ],
            ignore_index=True
        )
        self.order_status.drop_duplicates(inplace=True)

    def openOrder(self, orderId:OrderId, contract:Contract, order:Order,
                  orderState:OrderState):
        # self.order_status = pd.concat(
        #     [
        #         self.order_status,
        #         pd.DataFrame({
        #             'order_id': [orderId],
        #             'status': [orderState.status],
        #             'filled': [filled],
        #             'remaining': [remaining],
        #             'avg_fill_price': [avgFillPrice],
        #             'perm_id': [permId],
        #             'parent_id': [parentId],
        #             'last_fill_price': [lastFillPrice],
        #             'client_id': [clientId],
        #             'why_held': [whyHeld],
        #             'mkt_cap_price': [mktCapPrice]
        #         })
        #     ],
        #     ignore_index=True
        # )
        self.order_id_open = orderId
        self.contract_open = contract
        self.order_open = order
        self.order_state_open = orderState

    def openOrderEnd(self):
        print('openOrder')

    def completedOrder(self, contract:Contract, order:Order,
                       orderState:OrderState):
        self.contract_completed = contract
        self.order_completed = order
        self.order_state_completed = orderState






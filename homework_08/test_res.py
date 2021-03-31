# -*- coding: utf-8 -*-
# @Time   : 2021/3/20 18:53
# @Author : guoccf
# @File   : test_res.py
import json


class TestRes:
    def test_res(self):
        res_text = """
        {
            "data": {
                "pid": -1,
                "category": 1,
                "stocks": [{
                    "symbol": "SH600519",
                    "name": "贵州茅台",
                    "type": 11,
                    "remark": "",
                    "exchange": "SH",
                    "created": 1616236073339
                }, {
                    "symbol": "BABA",
                    "name": "阿里巴巴",
                    "type": 0,
                    "remark": "",
                    "exchange": "NYSE",
                    "created": 1616235003209
                }, {
                    "symbol": "01810",
                    "name": "小米集团-W",
                    "type": 30,
                    "remark": "",
                    "exchange": "HK",
                    "created": 1616234992167
                }]
            },
            "error_code": 0,
            "error_description": ""
        }
        """
        res_text1 = """
        {
            "data": {
                "items": [{
                    "market": {
                        "status_id": 8,
                        "region": "CN",
                        "status": "休市",
                        "time_zone": "Asia/Shanghai",
                        "time_zone_desc": null
                    },
                    "quote": {
                        "symbol": "SH600519",
                        "code": "600519",
                        "exchange": "SH",
                        "name": "贵州茅台",
                        "type": 11,
                        "sub_type": "ASH",
                        "status": 1,
                        "current": 2010.0,
                        "currency": "CNY",
                        "percent": -2.88,
                        "chg": -59.7,
                        "timestamp": 1616137200000,
                        "time": 1616137200000,
                        "lot_size": 100,
                        "tick_size": 0.01,
                        "open": 2035.0,
                        "last_close": 2069.7,
                        "high": 2043.0,
                        "low": 1992.23,
                        "avg_price": 2015.474,
                        "volume": 3578077,
                        "amount": 7.211521835E9,
                        "turnover_rate": 0.28,
                        "amplitude": 2.45,
                        "market_capital": 2.524957578E12,
                        "float_market_capital": 2.524957578E12,
                        "total_shares": 1256197800,
                        "float_shares": 1256197800,
                        "issue_date": 998841600000,
                        "lock_set": 0,
                        "current_year_percent": 0.6,
                        "high52w": 2627.88,
                        "low52w": 948.9967,
                        "limit_up": 2276.67,
                        "limit_down": 1862.73,
                        "volume_ratio": 0.88,
                        "eps": 35.49,
                        "pe_ttm": 56.64,
                        "pe_forecast": 55.982,
                        "pe_lyr": 61.276,
                        "navps": 118.18,
                        "pb": 17.008,
                        "dividend": 17.025,
                        "dividend_yield": 0.847,
                        "profit": 4.120647101443E10,
                        "profit_four": 4.457871959021E10,
                        "profit_forecast": 4.5102805282E10,
                        "pledge_ratio": 0.0,
                        "goodwill_in_net_assets": null,
                        "timestamp_ext": null,
                        "current_ext": null,
                        "volume_ext": null,
                        "traded_amount_ext": null,
                        "no_profit": null,
                        "no_profit_desc": null,
                        "weighted_voting_rights": null,
                        "weighted_voting_rights_desc": null,
                        "is_registration": null,
                        "is_registration_desc": null,
                        "is_vie": null,
                        "is_vie_desc": null,
                        "security_status": null
                    },
                    "others": {
                        "cyb_switch": true
                    },
                    "tags": []
                }, {
                    "market": {
                        "status_id": 8,
                        "region": "US",
                        "status": "休市",
                        "time_zone": "America/New_York",
                        "time_zone_desc": null
                    },
                    "quote": {
                        "symbol": "BABA",
                        "code": "BABA",
                        "exchange": "NYSE",
                        "name": "阿里巴巴",
                        "type": 0,
                        "sub_type": "1536",
                        "status": 1,
                        "current": 239.79,
                        "currency": "USD",
                        "percent": 1.4211,
                        "chg": 3.36,
                        "timestamp": 1616184600001,
                        "time": 1616184600001,
                        "lot_size": 1,
                        "tick_size": 0.01,
                        "open": 239.66,
                        "last_close": 236.43,
                        "high": 241.6,
                        "low": 236.8838,
                        "avg_price": 239.7051,
                        "volume": 15959658,
                        "amount": 3.8256997376083E9,
                        "turnover_rate": 0.59,
                        "amplitude": 1.99,
                        "market_capital": 6.50099129094E11,
                        "float_market_capital": null,
                        "total_shares": 2711118600,
                        "float_shares": null,
                        "issue_date": 1411056000000,
                        "lock_set": 1,
                        "current_year_percent": 3.03,
                        "high52w": 319.32,
                        "low52w": 169.95,
                        "variable_tick_size": "0.0001 1 0.01",
                        "volume_ratio": 0.96,
                        "eps": 9.019075878884514,
                        "pe_ttm": 26.587,
                        "pe_lyr": 28.3183,
                        "navps": 53.098843193584564,
                        "pb": 4.515917598759924,
                        "dividend": null,
                        "dividend_yield": null,
                        "psr": 6.79,
                        "short_ratio": null,
                        "inst_hld": null,
                        "beta": null,
                        "timestamp_ext": 1616198399198,
                        "current_ext": 240.15,
                        "percent_ext": 0.1501,
                        "chg_ext": 0.36,
                        "contract_size": 100,
                        "pe_forecast": 20.352,
                        "profit_forecast": 3.194281003077648E10,
                        "profit": 2.2956846358287376E10,
                        "profit_four": 2.4451784370055153E10,
                        "pledge_ratio": null,
                        "goodwill_in_net_assets": 31.309914722734167,
                        "shareholder_funds": 1.4395726114943237E11
                    },
                    "others": {
                        "cyb_switch": true
                    },
                    "tags": []
                }, {
                    "market": {
                        "status_id": 8,
                        "region": "HK",
                        "status": "休市",
                        "time_zone": "Asia/Shanghai",
                        "time_zone_desc": null
                    },
                    "quote": {
                        "symbol": "01810",
                        "code": "01810",
                        "exchange": "HK",
                        "name": "小米集团-W",
                        "type": 30,
                        "sub_type": "256",
                        "status": 1,
                        "current": 26.25,
                        "currency": "HKD",
                        "percent": 0.19,
                        "chg": 0.05,
                        "timestamp": 1616141288000,
                        "time": 1616141288000,
                        "lot_size": 200,
                        "tick_size": 0.05,
                        "open": 25.8,
                        "last_close": 26.2,
                        "high": 27.1,
                        "low": 25.55,
                        "avg_price": 26.4406,
                        "volume": 237278094,
                        "amount": 6.27369446126E9,
                        "turnover_rate": 1.16,
                        "amplitude": 5.92,
                        "market_capital": 6.61535151428E11,
                        "float_market_capital": 5.38341582476E11,
                        "total_shares": 25201339102,
                        "float_shares": 20508250761,
                        "issue_date": 1531065600000,
                        "lock_set": 1,
                        "current_year_percent": -20.93,
                        "high52w": 35.9,
                        "low52w": 9.2,
                        "variable_tick_size": "0.001 0.25 0.005 0.5 0.01 10.00 0.02 20.00 0.05 100.00 0.1 200.00 0.2 500.00 0.5 1000.00 1.00 2000.00 2.00 5000.00 5.00",
                        "volume_ratio": 0.64,
                        "eps": 0.6351,
                        "pe_ttm": 41.3317,
                        "pe_forecast": 37.7664,
                        "pe_lyr": 58.9164,
                        "navps": 4.7462,
                        "pb": 5.5307,
                        "dividend": null,
                        "dividend_yield": null,
                        "psr": 2.374,
                        "profit_forecast": 1.75165019064E10,
                        "profit": 1.1228370935599998E10,
                        "profit_four": 1.60055127566E10,
                        "shareholder_funds": 1.196122038332265E11
                    },
                    "others": {
                        "cyb_switch": true
                    },
                    "tags": []
                }],
                "items_size": 3
            },
            "error_code": 0,
            "error_description": ""
        }
        """

        data = json.loads(res_text1)
        # print(data)
        print(data["data"]["items"][0]["quote"]["name"])
        print(data["data"]["items"][1]["quote"]["name"])
        print(data["data"]["items"][2]["quote"]["name"])

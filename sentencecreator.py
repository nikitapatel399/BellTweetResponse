# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 16:21:48 2019

@author: Nikita
"""

import pandas as pd
    
def dictcompile():
    
    startlist = ["is there a ", "don't like ", "problems with ", "issues with ", "bad ", "compaint about ", "not working ", "broken ", "lost ", "he "]
    
    device = ["update", "ios", "pi", "SIM", "sim", "P20", "iphone", "iphone X", "iphone XS", "apple", "iphone 6", "samsung galaxy", "s4", "s6", "s7", "s8", 
              "s9", "s10", "note", "note 5", "note 8", "note 9", "huawei", "mate10", "LG", "android", "router", "modem", "button", "phone", "device"]
    
    service = ["outage", "down", "data", "fibe", "tv", "wifi", "LTE", "3g", "4g", "2g", "calling not working", "texts", "calls", "no service", "no bars", "disconnected", "not connected", "disconnect", "connection", "connect"]
    
    internet = ["internet", "outage", "wifi","ethernet", "internet", "websites", "apps", "facebook", "instagram", "netflix", "router", "modem", "connection", "connect", "down"]
    
    billings = ["money", "scam", "account", "bill", "payment", "charges", "credit card", "debit card", "card", "money", "expensive", "charged", "roam", "accounts",
                "transactions", "expensive", "$", "overcharge", "charged", "waste", "afford", "broke"] 
    
    technician = ["tree", "lawn", "grass", "driving", "parking", "tech", "technician", "van", "loitering", "digging", "truck", "safety", "pole", "wire", "schedule", "cable", "no show", "didn't show", "never came", "didn't come", "waited", "bush", "ran over"]
    
    support_complaint = ["rogers", "switching", "telus", "days", "hours", "wait", "poor customer support", "trash", "called", "wasted time", "bullshit", "shit", "unsatisfied", 
                         "waste", "stupid", "ridiculous", "unbelievable"]
    
    tv = ["HBO", "fibe tv", "tv", "netflix", "Crunch", "crunchtv", "hulu", "channel", "channels", "television", "remote", "bellfibe", "fibe", "movie", "record", "recording", "recap", "live", "remote", "battery", "remote control", "button"]
    
    thanks = ["dm", "satisfied", "satisfaction", "thx", "thank you", "helped", "happy", "good", "nice", "assisted", "thank u", "thnx", "ok", "okay", "better", "resolved", "in control", "fixed"]
    
    def listmaker(alist):
        newlist = []
        for word in startlist:
            for complaint in alist:
                newlist.append(word + complaint)
        return(newlist)
    
    device = listmaker(device)
    service = listmaker(service)
    internet = listmaker(internet)
    billings = listmaker(billings)
    technician = listmaker(technician)
    support_complaint = listmaker(support_complaint)
    tv = listmaker(tv)
    internet = listmaker(internet)
    thanks = listmaker(thanks)
    
    def labelcolumn(data, label):
        df = pd.DataFrame(data)
        df['label'] = label
        return df
    
    
    device = labelcolumn(device, 'device')
    service = labelcolumn(service, 'service')
    internet = labelcolumn(internet, 'internet')
    billings = labelcolumn(billings, 'billings')
    technician = labelcolumn(technician, 'technician')
    support_complaint = labelcolumn(support_complaint, 'support_complaint')
    tv = labelcolumn(tv, 'tv')
    internet = labelcolumn(internet, 'internet')
    thanks = labelcolumn(thanks, 'thanks')
    
    dfmain = pd.concat([device,service,internet,billings,technician,support_complaint,tv,internet,thanks])
    dfmain = dfmain.reset_index()
    dfmain = dfmain.drop('index', axis=1)
    
    dfmain = dfmain.rename(columns={0: 'message'})
    
    return(dfmain)
    
#data = dictcompile()
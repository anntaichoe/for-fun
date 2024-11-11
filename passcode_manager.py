#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 21:17:32 2020

@author: Diane
"""
passcode = {'account1': 'password1', 'account2': 'password2', 'account3': 'password3'}

def mypasscode():
    while True:
        account = input("請出入您的帳號: ").lower()
        for a,p in passcode.items():
            if account == a:
                print("密碼: ", p)
        if account not in passcode.keys():
            print(f"資料庫查詢不到 {account} 的帳號。請再試一次。")
        answer = input("按 'y' 繼續，或是按任何盤離開: ")
        if answer == "y":
            continue
        else:
            print("再見!")
            break
        return
mypasscode()
        
        
        

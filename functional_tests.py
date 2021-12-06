# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 13:00:16 2021

@author: Leinen

Environment: Python 3.6, Django 1.11, selenium 3
"""


from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
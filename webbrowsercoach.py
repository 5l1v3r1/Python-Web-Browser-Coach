#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webbrowser

star = '*********************************************************************'

webbrowser_ico = """
#########################################################
#       Web Browser Coach - GH0ST S0FTWARE       #
######################################################### 
#                       CONTACT                         #
#########################################################
#              DEVELOPER : İSMAİL TAŞDELEN              #                       
#        Mail Address : pentestdatabase@gmail.com       #
# LINKEDIN : https://www.linkedin.com/in/ismailtasdelen #
#           Whatsapp : + 90 534 295 94 31               #
#########################################################
"""

print webbrowser_ico

print star

site = raw_input('WEP SITE ADRESI : ')

webbrowser.open('http://'+ site)

print star

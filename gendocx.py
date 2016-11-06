#! /usr/bin/python
# -*- coding: utf-8 -*-

import string
import sys, uno

local = uno.getComponentContext()
resolver = local.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", local)
context = resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
desktop = context.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", context)
url = "file:////home/iderkun/PycharmProjects/untitled/1.doc"
document = desktop.loadComponentFromURL(url, "_blank", 0, ())
print(document.CharacterCount)
search = document.createSearchDescriptor()
#What to search for
search.SearchString = 'http://tea-san.ru/robots.txt'
#Found string
found = document.findFirst( search )

while found:
    found.String = str.replace( found.String,'http://tea-san.ru/robots.txt' , 'qw' )
    found = document.findNext( found.End, search)
#Save
document.store()
#document.dispose()
sys.exit()
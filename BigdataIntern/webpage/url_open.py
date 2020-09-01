'''
Created on 2020. 9. 1.

@author: jihye
'''




from urllib.request import urlopen

f = urlopen('http://hanbit.co.kr')
#(type(f)) # type : http.client.HTTPResponse


#print(f.read()) # Http's Content


#print(f.status)


print(f.getheader('Content-Type')) # 'Content-Type' : encoding 







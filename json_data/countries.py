from pygal.i18n import COUNTRIES

''' 
    COUNTRIES字典：键和值分别为两个字母的国别码、国家名
'''
for country_code in sorted(COUNTRIES.keys()):
    print(country_code,COUNTRIES[country_code])
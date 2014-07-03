#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author		: 陳勁龍
#Student ID	: F74005018
#Description	: Calculate average sale price per m^2 of the every county in Taiwan in year 100 and 101

import sys
import urllib
import json

county_set = [u'基隆市',u'新北市',u'臺北市',u'桃園縣',u'新竹縣',u'新竹市',u'宜蘭縣',u'苗栗縣',u'臺中市',u'彰化縣',u'南投縣',u'花蓮縣',u'雲林縣',u'嘉義縣',u'嘉義市',u'臺南市',u'澎湖縣',u'高雄市',u'臺東縣',u'屏東縣']
url = 'http://www.datagarage.io/api/5365dee31bc6e9d9463a0057?selector=%E4%BA%A4%E6%98%93%E5%B9%B4%E6%9C%88%3E=10001%20AND%20%E4%BA%A4%E6%98%93%E5%B9%B4%E6%9C%88%3C=10112&fields=%E5%96%AE%E5%83%B9%E6%AF%8F%E5%B9%B3%E6%96%B9%E5%85%AC%E5%B0%BA,%E7%B8%BD%E5%83%B9%E5%85%83,%E4%BA%A4%E6%98%93%E5%B9%B4%E6%9C%88,%E5%9C%9F%E5%9C%B0%E5%8D%80%E6%AE%B5%E4%BD%8D%E7%BD%AE%E6%88%96%E5%BB%BA%E7%89%A9%E5%8D%80%E9%96%80%E7%89%8C'
try:
	data = json.load(urllib.urlopen(url))
except IOError as e:
	print 'I/O Error({0}): {1}'.format(e.errno, e.strerror)
	sys.exit()
except ValueError:
	print 'Decoding JSON has failed'
	sys.exit()
if data == []:
	print 'Decoded JSON is empty'
	sys.exit()

info = dict()
i_prices = 0
i_matches = 1
i_mean = 2		# Mean of house prices/m^2
i_income = 3
for county in county_set:
	info[county] = dict()
	info[county][100] = [0, 0, 0, 0]	#i_prices, i_matches, i_mean, i_income
	info[county][101] = [0, 0, 0, 0]	#i_prices, i_matches, i_mean, i_income

for datum in data:
	for county in county_set:
		if county.encode('utf-8') in datum[u'土地區段位置或建物區門牌'].encode('utf-8'):
			year = datum[u'交易年月']/100
			info[county][year][i_prices] += datum[u'單價每平方公尺']
			info[county][year][i_matches] += 1
			break

for y in (100, 101):
	for county in county_set:
		if info[county][y][i_matches] != 0:
			info[county][y][i_mean] = info[county][y][i_prices]/info[county][y][i_matches]

f = open('./income.txt', 'r')
for line in f:
	if line == '\n':
		break;
	if line[0] == '#':
		continue
	income = line.split(' ')
	if info.get(income[0].decode('utf-8')) is not None:
		info[income[0].decode('utf-8')][int(income[1])][i_income] = int(income[2])

# Draw table
print '-----------------------------------------------------------------------------------'
print 'COUNTY YEAR PRICES(/m^2) INCOME INCOME/PRICES INCOME_GROWTH_RATE PRICES_GROWTH_RATE'
print '-----------------------------------------------------------------------------------'
for y in (100, 101):
	for county in county_set:
		if info[county][y][i_matches] != 0:
			info[county][y][i_mean] = info[county][y][i_prices]/info[county][y][i_matches]
			print u'{0}\t{1}\t{2}\t{3}\t{4}'.format(county, y, info[county][y][i_mean], info[county][y][i_income], float(info[county][y][i_income])/info[county][y][i_mean]),
			# Calculate income growth rate 
			if info[county].get(y-1) is not None:
				print u'\t{0}'.format(float(info[county][y][i_income]-info[county][y-1][i_income])/info[county][y-1][i_income]),
				# Calculate housing prices' growth rate 
				if info[county][y-1][i_matches] != 0:
					print u'\t{0}'.format(float(info[county][y][i_prices]-info[county][y-1][i_prices])/info[county][y-1][i_prices])
				else:
					print ''
			else:
				print ''


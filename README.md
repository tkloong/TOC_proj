TOC project
===========

What is this?
-------------
This is a program which parse the housing prices from 'http://www.datagarage.io/datasets/ktchuang/realprice/A' and get the average housing prices in each Taiwan county. Besides, we read a file named 'income.txt' to get the average annual income in each Taiwan county.

What are our motivation?
------------------------
We are curious about in Taiwan, house prices in which area is being pushed high. Thus, we are more likely to find out which area is suitable to buy houses for living.

How to execute?
---------------
python TOC_proj.py

How do we analysis?
-------------------
At first, we are going to use CPI of each area to compare with the housing prices. Through dividing CPI by housing prices, we can conclude that houses in which area has more CP value.

But the open data of CPI of each county is incomplete. We soon focus on the data of average annual income of citizen. The open data that provided by goverment is from year 1995 to 2012. So we compare these data with housing prices in 2011 and 2012.

We define a term called "民衆負擔能力"(housing affordability), equals to average annual income divide housing prices. The larger the value, the higher the affordability to buy house in that county.

Result
------
-----------------------------------------------------------------------------------
COUNTY YEAR PRICES(/m^2) INCOME INCOME/PRICES INCOME_GROWTH_RATE PRICES_GROWTH_RATE
-----------------------------------------------------------------------------------
新北市	100	128659	1116342	8.67675016905 
臺北市	100	192118	1537890	8.00492405709 
桃園縣	100	25312	1183732	46.7656447535 
新竹縣	100	93164	1372358	14.730561161 
臺中市	100	55757	1100346	19.7346700863 
花蓮縣	100	36495	920602	25.2254281408 
新北市	101	84851	1101389	12.9802712991 	-0.0133946407105 	-0.0407163948778
臺北市	101	215063	1570778	7.30380400162 	0.0213851445812 	6.27631644011
桃園縣	101	52853	1238698	23.4366639547 	0.0464344969976 	5.26419287295
新竹縣	101	78652	1367712	17.3894115852 	-0.00338541401005 	-0.155770169968
新竹市	101	105604	1439066	13.627002765 	-0.0274445401862 
苗栗縣	101	37837	1012306	26.7543938473 	-0.00181236589676 
臺中市	101	52136	1067060	20.4668559153 	-0.0302504848475 	4.50646555589
雲林縣	101	28240	824211	29.1859419263 	0.00786643807977 
臺南市	101	40258	927231	23.0322171991 	-0.0223032255956 

Difficulties
------------
The housing prices in 2011 and 2012 is incomplete, and the open data of average annual income is published until 2012. We hope that the open data of average annual income is updated so that we have more data to do statistics.


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

How do we analyse?
-------------------
At first, we are going to use CPI of each area to compare with the housing prices. Through dividing CPI by housing prices, we can conclude that houses in which area has more CP value.

But the open data of CPI of each county is incomplete. We soon focus on the data of average annual income of citizen. The open data that provided by goverment is from year 1995 to 2012. So we compare these data with housing prices in 2011 and 2012.

We define a term called "民衆負擔能力"(housing affordability), equals to average annual income divide housing prices. The larger the value, the higher the affordability to buy house in that county.

Difficulties
------------
The housing prices in 2011 and 2012 is incomplete, and the open data of average annual income is published until 2012. We hope that the open data of average annual income is updated so that we have more data to do statistics.


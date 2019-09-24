
# Sales prediction
# 9/17/2019
# CTI-110 P2T1 - Sales Prediction
# Kabin Yang
#

#profit + 23% of sales

##Prompt the user for input total sales called sales
##assign the input to a car caled sales
##calculate the profit by sales * .23
####Display profit 


sales = float(input('Enter predictied sales amount: '))
      
profit = sales * 0.23

print ('The profit is $',format(profit, ',.2f'),'.',sep='')

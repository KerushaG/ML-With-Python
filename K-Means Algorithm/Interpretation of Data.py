#Data Science, Algorithms and Advanced Software Engineering, Task 17.3
#Kerusha Govender, 05.07.2019
#[Response to questions.]
##########################################################################################################################################################

#17.2.1.Run k-means using 3 clusters on the 1953 and 2008 datasets separately. What do you see?
#Take note of how the clusters change from 1953 to 2008.
#You will need to pay attention not only to which countries are in clusters together but also to the LifeExpectancy and BirthRates for those clusters.
#------------------------------------------------------------------------------------------------------------------------------------------------------
#Between the 1953 and 2008 graphs:
#In 2008 the life expectancy is higher and has a tighter cluster than in 1953.
#The third cluster is also more spread out in its data than in 1952.
#In general the life expectancy seems to have increased from 1953 - 2008.
#Numbers in three clusters:
#The third cluster increased by a significant difference in 2008, but for the first two clusters there are slight differences.
#Means in clusters:
#Birth rate means are higher in 1953 clusters than 2008.
#The life expectancy means are higher in 2008 than 1953.
#------------------------------------------------------------------------------------------------------------------------------------------------------
#Next, run the algorithm with 4 clusters on dataBoth.csv.
#Which countries are moving up clusters? #not sure what this means
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#How does (2008)South Africa” compare to “(1953)United States”?
#2008 SA is in cluster 3 with US 1953 which has:
#The BirthRate mean for cluster 2 is: 27.564415540540537
#The Life Expectancy mean for cluster 2 is: 61.79611324324324
#There's so many reasons could explain this gap, and I think its mainly around socio-economic development, in which the US was and is obviously ahead of the game.
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#Are there any 2008 countries that are in a cluster that is made up mostly of 1953 countries? Try and explain why.
#Yes, and this basically indicates not much change in socio-economic state possibly for political reasons:
#['(2008)Afghanistan']
#['(1953)Afghanistan']
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Are there any 1953 countries that are in a cluster that is made up of mostly 2008 countries? Try and explain why
#Yes there's about 7 countries which are considered top developed countries, and have good stats in general for the health and wealth of their countries, political
#stability etc, which one can also tell in comparison to how ahead they were compared to countries in 1953

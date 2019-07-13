#Data Science, Algorithms and Advanced Software Engineering, Task 14
#Kerusha Govender, 30.06.2019
#Introduction to Machine Learning

####################################################################

#14.1.
##Firsly there is a distinction between Artificial Intelligence and Machine Learning (ML). Artificial Intelligence is focused on mimicking the human mind, but to do so it
##needs learning capabilities, which is what ML is focused on. ML is the creation of software that is capable of learning, and is closer to data mining and statistics.
##The idea is that if a program can improve its performance on a given set of tasks as compared to past experiences, it has learned. It does this by extracting
##knowledge from data and feeding back an answer to a question. ML works by feeding data to an algorithm, which then develops relationships and associations of that
##data and overtime is able to predict or answer a question to a new unknown input. Eg, e-mail sent to inbox or spam. The outcome is a classification of the input, the
##ways in which you measure the classification is through features according to which data is given meaning, and you teach the model by feeding it data, the training
##process. The more data, the better the model and the higher the accuracy of the outcome. ML is more relevant today because of the large volumes of data produceed, more
##than can be dealt with manually, so ML helps process data and also helps maximise classification accuracy with input that may be more complex and not easily identifiable.
##Examples of ML is used to optimize google search, where they have bunches of algorithms that help customise and produce insightful results, predictive and searching
##pricing modelling in Uber and other businesses and lastly help make medical diagnoses. It's becoming a must in tech businesses/services.

#14.2.
##Supervised Learning is one group of algorithms that you can use to teach a system to learn and predict accurate results. You feed the system data that is labelled. As
##in you give the system data with input, its features and the correct associated output values or put simply input/out pairs. So for example, Facebook uses supervised
##learning to do facial recognition. Everytime you tag someone, overtime it begins to remember their face and then can predict who that person is without you needing
##to tag, because it begins associating the name with the features. Examples of models:
##- K-nearest Neighbour
##- Decision Trees
##- Regression Algoritms
##- Bayesian Algorithms

#14.3.
##Unsupervised learning is another group of algorithms that is used in ML. The idea here is to feed the system data, but wihout labels. In other words, the system will
##not give you labelled definitive outcomes. What it does is finds patterns in the data, and organizes them in clusters. When given new input, it is meant to assess
##that data and place it among the groups of clusters. An example is fraud detection. It tracks data,lets say transactions, but it doesn not associate data with
##fraud or no fraud, etc. Instead it identifies anomalies and possible outliers as a way to detect something shady. Examples of models:
##- K-Means
##- Hierarchical Clustering


#14.4.
##One of the aspects of ML and AI that's interesting is how its used to enhance business services and customer experiences, and ML algoritms plays a big role in
##producing customised responses having taken various variables into account, I have already mentioned Google search and Uber, but I was interested in how Netlfix works,
##because they have grown very popular and use Python extensively. So the goal of Netflix is to predict what viewers will watch before they watch it. They work on
##algorithms to produce the perfect reccommendation. They do not just rely on historical data but have algorithms in place to monitor on-going interactions and they apply
##behavorial metrics. The approach is three pronged. 1) They collect viewer data, implicit which is the liking of content and explicit which is like binge watching.
##2) They tag shows beyond just genres - they have people watch the shows and come up with more indepth tags. 3) The data and tags are combined to feed into algorithms
##to predict what viewers will want to watch. So these algorithms find patterns that lead to someone watching something. These reccommendation algorithms work,
##because Netflix says alot of people watch stuff from reccommendations, which is customised for each viewer. The imaging and marketing on the profile is also
##customised. Netflix is capatilizing on this data to vastly and continuously improve userability, the code they write, the acquisition of content they get, their
##original productions, marketing strategies, etc. They are also heavily involved in research and development. They bring together diverse teams to not just further
##research on ML but actually apply it to a real product/service/user experience.

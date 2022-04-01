'''
This is because, this is a text-classification problem. When a spam classifier looks at a mail, 
it searches for potential words that it has seen in the previous spam emails. If it finds a majority of those 
words, then it labels it as 'Spam'.
For training dataset the model is getting 99% of accuracy on test data set we are getting 98% of accuracy. 
For evaluating any model accuracy alone cannot be an efficient way to estimate the model is accurate or not. 
Let me give you an example. Let’s say we are predicting whether someone will default for 
any bank organization or not.
'''






import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn import svm
from sklearn.model_selection import GridSearchCV

##Step1: Load Dataset
dataframe = pd.read_csv("spam.csv")
print(dataframe.describe())

##Step2: Split in to Training and Test Data

x = dataframe["EmailText"]
y = dataframe["Label"]

x_train,y_train = x[0:4457],y[0:4457]
x_test,y_test = x[4457:],y[4457:]

##Step3: Extract Features
cv = CountVectorizer()  
features = cv.fit_transform(x_train)

##Step4: Build a model
tuned_parameters = {'kernel': ['rbf','linear'], 'gamma': [1e-3, 1e-4],
                     'C': [1, 10, 100, 1000]}

model = GridSearchCV(svm.SVC(), tuned_parameters)

model.fit(features,y_train)

print(model.best_params_)
#Step5: Test Accuracy
print(model.score(cv.transform(x_test),y_test))




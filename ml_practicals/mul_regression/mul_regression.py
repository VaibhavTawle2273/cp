
# PROGRAMME FOR MULTIPLE LINEAR REGRESSION

# Packages imported from different libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
get_ipython().run_line_magic('matplotlib', 'inline')



# Loading CSV dataset using pandas
dataset = pd.read_csv('winequality-red.csv')


# Display the shape of dataset
dataset.shape

# Show dataset
dataset.describe()


# Function to check whether any data is NULL
dataset.isnull().any()


# Filling NULL values to 0
dataset = dataset.fillna( method ='ffill')


# Assigning values to X & y
X = dataset[['fixed acidity', 'volatile acidity', 'citric acid','residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates','alcohol']]. values
y = dataset['quality'].values



# Plotting graph for quality
plt.figure( figsize =(15 ,10) )
plt.tight_layout()
seabornInstance.displot(dataset ['quality'])


# Splitting training & testing data in 8:2 ratio
X_train,X_test,y_train,y_test = train_test_split(X , y ,test_size =0.2 ,random_state =0)


# Importing model and training it for train data
regressor = LinearRegression()
regressor.fit( X_train , y_train)


# Genrating dataframe using pandas
coeff_df = pd.DataFrame( regressor.coef_ , dataset.columns[0:11] , columns =['Coefficient'])
coeff_df


# Saving predicted data for test dataset
y_pred = regressor.predict( X_test )



# Generating list for training & testing data
df = pd.DataFrame({'Actual': y_test ,'Predicted': y_pred })
df1 = df.head(25)
df1



# Graph showing difference between actual & predicted data
df1.plot( kind = 'bar' , figsize =(10 ,8) )
plt.grid( which = 'major' , linestyle = '-' , linewidth = '0.5' , color = 'green')
plt.grid( which = 'minor' , linestyle = ':' , linewidth = '0.5' , color = 'black')
plt.show()




# Performance measure
print ('Mean Absolute Error : ' , metrics.mean_absolute_error( y_test , y_pred ) )
print ('Mean Squared Error :' , metrics.mean_squared_error( y_test , y_pred ) )
print ('Root Mean Squared Error :' , np.sqrt ( metrics.mean_squared_error( y_test ,y_pred ) ) )






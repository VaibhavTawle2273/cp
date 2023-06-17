# PROGRAMME FOR SIMPLE LINEAR REGRESSION

# Packages imported from different libraries
import pandas as pd
import numpy as np
import matplotlib . pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
get_ipython().run_line_magic('matplotlib', 'inline')

# Loading CSV dataset using pandas
dataset = pd.read_csv('weather.csv')

# Display the shape of dataset
dataset.shape

# Show dataset
dataset.describe()


# Ploting two attributes of dataset
dataset.plot(x ='MinTemp' , y ='MaxTemp', style ='o')
plt.title('MinTemp vs MaxTemp')
plt.xlabel('MinTemp')
plt.ylabel('MaxTemp')
plt.show()


# Plot graph for MaxTemp
plt.figure( figsize =(15 ,10) )
plt.tight_layout()
seabornInstance.displot( dataset['MaxTemp'])

# Assigning MinTemp values to X & MaxTemp values to Y
X = dataset['MinTemp'].values.reshape( -1 ,1)
y = dataset['MaxTemp'].values.reshape( -1 ,1)

# Splitting train & test data in 8:2 ratio
X_train , X_test , y_train , y_test = train_test_split(X , y , test_size =0.2 ,random_state =0)

# importing LinearRegression model in regressor
regressor = LinearRegression ()
regressor.fit( X_train , y_train ) # training the algorithm

#To retrieve the intercept
print( regressor.intercept_ )

#For retrieving the slope
print ( regressor.coef_ )

# Finding predicted values for X_test data
y_pred = regressor.predict( X_test )

# Comparing the actual output values for X_test with the predicted values
df = pd.DataFrame({ 'Actual ': y_test.flatten() , 'Predicted ': y_pred.flatten() })
df

# Ploting actual & predicted values for intial 25 values
df1 = df.head (25)
df1.plot( kind ='bar', figsize =(16 ,10) )
plt.grid( which ='major', linestyle ='-', linewidth ='0.5', color ='green')
plt.grid( which ='minor', linestyle =':', linewidth ='0.5', color ='black')
plt.show()

# Ploting straight line with the test data
plt.scatter( X_test , y_test , color ='gray')
plt.plot( X_test , y_pred , color ='red', linewidth =2)
plt.show()

# Printing different errors
print('Mean Absolute Error :', metrics.mean_absolute_error( y_test , y_pred ) )
print('Mean Squared Error :', metrics.mean_squared_error ( y_test , y_pred ) )
print('Root Mean Squared Error :', np.sqrt ( metrics.mean_squared_error ( y_test ,y_pred ) ) )

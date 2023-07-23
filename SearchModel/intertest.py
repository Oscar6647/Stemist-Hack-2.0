"""
#Decision tree model

import pickle
import numpy as np
with open ('Ometeotl.pkl', 'rb') as file:
    model = pickle.load(file)
test_data = np.array([[1, 1, 1, 1], [4,4,4,4]], dtype=int)
predictions = model.predict(test_data)
print("predicted classes: ")
print(predictions)
"""

#checking for transalation pls ignore this

"""
import pickle

# Replace 'path/to/your/model.pkl' with the actual file path of your saved model.
with open('Ometeotl.pkl', 'rb') as file:
    model = pickle.load(file)

# Check if the model has the 'feature_names_' attribute (specific to scikit-learn DecisionTreeClassifier).
if hasattr(model, 'feature_names_'):
    feature_names = model.feature_names_

    # Print the feature names.
    print("Feature Names:")
    print(feature_names)
else:
    print("The model does not have feature names.")
"""

#neeeds dictionary to translate predicted classes and what the input translates too.

#The following is code to test new Forest PICKLE VERSION

import pickle
import pandas as pd
with open ('SearchModel\EduHack_RandomForest.pkl', 'rb') as file:
    model = pickle.load(file)
test_data = pd.DataFrame({"Categoría": [1], "Subcategoria": [3], "Edad de Estudiantes ": [9], "Tiempo de clase": [40]})
predictions = model.predict(test_data)
print("predicted classes: ")
print(predictions)

#JOBLIB VERSION

import joblib
import pandas as pd
with open ('SearchModel\EduHack2.joblib', 'rb') as file:
    model = joblib.load(file)
test_data = pd.DataFrame({"Categoría": [1], "Subcategoria": [3], "Edad de Estudiantes ": [9], "Tiempo de clase": [40]})
predictions = model.predict(test_data)
print("predicted classes_joblib: ")
print(predictions)
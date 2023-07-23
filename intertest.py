import pickle
import numpy as np
with open ('Ometeotl.pkl', 'rb') as file:
    model = pickle.load(file)
test_data = np.array([[1, 1, 1, 1], [4,4,4,4]], dtype=int)
predictions = model.predict(test_data)
print("predicted classes: ")
print(predictions)
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
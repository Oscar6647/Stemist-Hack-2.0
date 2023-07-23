#JOBLIB VERSION

import joblib
import pandas as pd
with open ('SearchModel\EduHack2.joblib', 'rb') as file:
    model = joblib.load(file)
test_data = pd.DataFrame({"Categoría": [1], "Subcategoria": [3], "Edad de Estudiantes ": [9], "Tiempo de clase": [40]})
predictions = model.predict(test_data)
print("predicted classes_joblib: ")
print(predictions)
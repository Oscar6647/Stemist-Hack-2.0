""""#JOBLIB VERSION

import joblib
import pandas as pd
with open ('SearchModel\EduHack2.joblib', 'rb') as file:
    model = joblib.load(file)
test_data = pd.DataFrame({"Categoría": [1], "Subcategoria": [3], "Edad de Estudiantes ": [9], "Tiempo de clase": [40]})
predictions = model.predict(test_data)
print("predicted classes_joblib: ")
print(predictions) """

import joblib
import pandas as pd

# Load the model from the joblib file
with open('SearchModel/EduHack2.joblib', 'rb') as file:
    model = joblib.load(file)


category_mapping = {
    "Biology": 1,
    "Physics": 2,
    "Math":3,
    "Spanish":4
}

Biosubject_mapping = {
    "Human Body": 1,
    "Food Chain": 2,
    "Ecosystems": 3
}

Physubject_mapping = {
    "Matter":1,
    "Movement":2,
    "Law of Physics":3
}

Mathsubject_mapping = {
    "Addition and Substraction": 1,
    "Multiplication and Division" : 2,
    "Fractions": 3
}

Spasubject_mapping = {
    "Spelling": 1,
    "Reading": 2,
    "Writting": 3
}

# Function to preprocess the input data
def preprocess_input(input_line):
    # Replace this with your actual preprocessing steps
    # Convert the inputs to the appropriate data types and format them as a DataFrame
    categoria, subcategoria, edad_estudiantes, tiempo_clase = input_line.split(",")
    categoria = category_mapping[categoria]
    if categoria == 1:
        subcategoria = Biosubject_mapping[subcategoria]
    elif categoria == 2:
        subcategoria = Physubject_mapping[subcategoria]
    elif categoria == 3:
        subcategoria = Mathsubject_mapping [subcategoria]
    else:
        subcategoria = Spasubject_mapping[subcategoria]

    # Convert the other inputs to integers
    edad_estudiantes = int(edad_estudiantes)
    tiempo_clase = int(tiempo_clase)

    test_data = pd.DataFrame({
        "Categoría": [categoria],
        "Subcategoria": [subcategoria],
        "Edad de Estudiantes ": [edad_estudiantes],
        "Tiempo de clase": [tiempo_clase]
    })
    return test_data

# Function to receive inputs and make predictions
def predict_from_terminal():
    print("Enter the inputs separated by spaces (Categoría Subcategoria Edad_de_Estudiantes Tiempo_de_clase):")
    input_line = input()

    # Preprocess the input data
    test_data = preprocess_input(input_line)

    # Make predictions using the model
    predictions = model.predict(test_data)

    print("Predicted classes (joblib):")
    print(predictions)

if __name__ == "__main__":
    predict_from_terminal()

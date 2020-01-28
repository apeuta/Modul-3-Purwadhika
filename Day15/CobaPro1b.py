import joblib

model = joblib.load("modelJoblib")

#prediksi SL SW PL PW
SL = int(input("Please input Sepal Lenght (cm) : "))
SW = int(input("Please input Sepal Width (cm) : "))
PL = int(input("Please input Petal Lenght (cm) : "))
PW = int(input("Please input Petal Width (cm) : "))
print(f"Prediksi model adalah spesies {model.predict([[SL, SW, PL, PW]]) [0]}")
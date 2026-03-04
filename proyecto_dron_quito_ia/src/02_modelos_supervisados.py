# -*- coding: utf-8 -*-

import pandas as pd
import os
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
from sklearn.metrics import ConfusionMatrixDisplay,RocCurveDisplay

os.makedirs("figures",exist_ok=True)

data = pd.read_csv("data/simulated/dataset_drone_quito.csv")

y = data["resultado_entrega"]

X = data.drop(columns=[
"id_vuelo",
"fecha_salida",
"fecha_llegada",
"resultado_entrega"
])

num_cols = [
"distancia_km",
"peso_kg",
"dim_l_cm",
"dim_a_cm",
"dim_h_cm",
"bateria_inicio",
"bateria_fin",
"temperatura",
"obstaculos",
"trafico_aereo"
]

cat_cols = [
"ruta",
"clima",
"viento"
]

preprocess = ColumnTransformer(

transformers=[
("num",StandardScaler(),num_cols),
("cat",OneHotEncoder(handle_unknown="ignore"),cat_cols)
]

)

X_train,X_test,y_train,y_test = train_test_split(
X,y,test_size=0.25,random_state=42
)

modelos = {

"logreg":LogisticRegression(max_iter=2000),

"arbol":DecisionTreeClassifier(max_depth=6),

"svm":SVC(kernel="rbf",probability=True),

"mlp":MLPClassifier(hidden_layer_sizes=(32,16),max_iter=1200)

}

for nombre,modelo in modelos.items():

    pipe = Pipeline([

    ("prep",preprocess),
    ("model",modelo)

    ])

    pipe.fit(X_train,y_train)

    pred = pipe.predict(X_test)

    acc = accuracy_score(y_test,pred)
    prec = precision_score(y_test,pred)
    rec = recall_score(y_test,pred)
    f1 = f1_score(y_test,pred)

    print("\nModelo:",nombre)

    print("Accuracy:",acc)
    print("Precision:",prec)
    print("Recall:",rec)
    print("F1:",f1)

    disp = ConfusionMatrixDisplay.from_estimator(pipe,X_test,y_test)

    plt.title("Confusion Matrix "+nombre)

    plt.savefig("figures/cm_"+nombre+".png")

    plt.close()

    RocCurveDisplay.from_estimator(pipe,X_test,y_test)

    plt.title("ROC "+nombre)

    plt.savefig("figures/roc_"+nombre+".png")

    plt.close()
# -*- coding: utf-8 -*-

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

train = [

("estado","ESTADO"),

("donde estas","ESTADO"),

("trayecto","ESTADO"),

("bateria","BATERIA"),

("nivel bateria","BATERIA"),

("carga","CARGA"),

("peso","CARGA"),

("sensores","SENSORES"),

("novedades","SENSORES"),

("cancelar","CANCELAR"),

("abortar","CANCELAR")

]

X = [t[0] for t in train]

y = [t[1] for t in train]

modelo = Pipeline([

("tfidf",TfidfVectorizer()),

("clf",LogisticRegression())

])

modelo.fit(X,y)

estado_dron = {

"trayecto":"Ruta B hacia Quito Norte",

"bateria":85,

"carga":18,

"max_carga":40,

"viento":"medio",

"lluvia":False

}

def responder(intent):

    if intent=="ESTADO":

        return "El dron se encuentra en "+estado_dron["trayecto"]

    if intent=="BATERIA":

        return "Nivel de bateria "+str(estado_dron["bateria"])+"%"

    if intent=="CARGA":

        p = estado_dron["carga"]/estado_dron["max_carga"]*100

        return "Carga "+str(estado_dron["carga"])+" kg ("+str(round(p,1))+"%)"

    if intent=="SENSORES":

        return "Sensores: viento "+estado_dron["viento"]

    if intent=="CANCELAR":

        return "Mision cancelada, retornando a sucursal cercana"

    return "No se entiende el comando"

print("Chat dron iniciado (escribe salir para terminar)")

while True:

    msg = input("Operador: ")

    if msg=="salir":

        break

    intent = modelo.predict([msg])[0]

    print("Dron:",responder(intent))
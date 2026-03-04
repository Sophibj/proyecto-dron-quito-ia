class DronFSM:

    def __init__(self):
        self.estado = "ENCENDIDO"

    def actualizar(self, bateria, lluvia, viento, obstaculo):

        if self.estado == "ENCENDIDO":
            print("Dron encendido, verificando batería")
            if bateria >= 80:
                self.estado = "LISTO_DESPEGUE"
            else:
                self.estado = "RECARGANDO"

        elif self.estado == "LISTO_DESPEGUE":
            print("Dron listo para despegar")
            self.estado = "NAVEGANDO"

        elif self.estado == "NAVEGANDO":

            if lluvia == "LLUVIA_FUERTE":
                self.estado = "RETORNAR"

            elif viento == "MUY_ALTO":
                self.estado = "RETORNAR"

            elif bateria < 30:
                self.estado = "RETORNAR"

            elif obstaculo == 1:
                self.estado = "EVITAR_OBSTACULO"

            else:
                self.estado = "ENTREGA"

        elif self.estado == "EVITAR_OBSTACULO":
            print("Evitando obstáculo")
            self.estado = "NAVEGANDO"

        elif self.estado == "ENTREGA":
            print("Entrega realizada")
            self.estado = "RETORNO_BASE"

        elif self.estado == "RETORNAR":
            print("Retornando a sucursal más cercana")
            self.estado = "RETORNO_BASE"

        elif self.estado == "RETORNO_BASE":
            print("Regresando a base")

        print("Estado actual:", self.estado)

# Simulación de funcionamiento

dron = DronFSM()

dron.actualizar(bateria=85, lluvia="SOLEADO", viento="BAJO", obstaculo=0)
dron.actualizar(bateria=75, lluvia="SOLEADO", viento="BAJO", obstaculo=1)
dron.actualizar(bateria=70, lluvia="LLUVIA_FUERTE", viento="MEDIO", obstaculo=0)
#Herencia

# Clase base
class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def mostrar_info(self):
        print(f"\n🚗 DATOS DEL VEHÍCULO 🚗\nMarca: {self.marca}\nModelo: {self.modelo}\nAño: {self.anio}")

# Clase hija Coche (completa esta parte)
class Coche(Vehiculo):
    def __init__(self, marca, modelo, anio, puertas):
        super().__init__(marca, modelo, anio)  # Llamamos al constructor de la clase padre
        self.puertas = puertas

    def mostrar_info(self):
        super().mostrar_info()  # Llamamos al método mostrar_info() de Vehiculo
        print(f"Puertas: {self.puertas}")

# Clase hija Moto (completa esta parte)
class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio, tipo_moto):
        super().__init__(marca, modelo, anio)
        self.tipo_moto = tipo_moto

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de moto: {self.tipo_moto}")

# 📌 Probando
coche_1 = Coche('Toyota', 'Corolla', 2020, 4)
moto_1 = Moto('Yamaha', 'R1', 2023, 'Deportiva')

coche_1.mostrar_info()
moto_1.mostrar_info()

import random as r
import vegas, determinista


class Retador:
    
    posLlegada = 0

    def __init__(self, tiempo_llegada,  tiempo_tarda, tiempo_salida, id=None):
        if not id is None:
            Retador.posLlegada += 1
            self.posLlegada = Retador.posLlegada
        else:
            self.posLlegada = 0
        self.tiempo_llegada = tiempo_llegada
        self.tiempo_tarda = tiempo_tarda
        self.tiempo_salida = tiempo_salida


class Evento:
    def __init__(self, tiempo_ocurrencia, tipo, entidad):
        self.tiempo_ocurrencia = tiempo_ocurrencia
        self.tipo = tipo
        self.entidad = entidad


class Simulacion:
    
    list_retadores = []
    listaEventosFuturos = []
    historico_eventos = []
    reloj = 0
    atendidos = 0
    cola = 0
    cola_max = 0
    maestro_ocupado = False

    def __init__(self, num_retadores, numero_reinas, tiempo_entre_llegadas, desv_tiempo_llegadas):
        self.num_retadores = num_retadores
        self.numero_reinas = numero_reinas
        self.tiempo_entre_llegadas = tiempo_entre_llegadas
        self.desv_tiempo_llegadas = desv_tiempo_llegadas

    def llegada(self,  evento):
        if self.maestro_ocupado:
            self.cola += 1
            self.cola_max = max(self.cola, self.cola_max)            
        else:
            # Si el maestro esta libre, se ocupa para simular la atencion a un retador, se verifica que el reloj se mayor que 0 para ignore el evento previo al primer retador
            self.maestro_ocupado = True
            
        self.list_retadores.append(evento.entidad)

    def salida(self,  evento):
        if self.cola > 0:
            self.cola -= 1
            self.actualizarlistaEventosFuturos(evento, False)
        self.atendidos += 1
        if self.cola == 0:
            self.actualizarlistaEventosFuturos(evento,  False)
            self.maestro_ocupado = False
    
    def solucion(self, numero_reinas):
        exito = False
        solucion = []
        n_iter_n_queens = 0
        algoritmo = r.randint(0, 1)
        if algoritmo == 0:
            return vegas.maestroVegas(numero_reinas, exito, solucion, n_iter_n_queens)
        else:
            return determinista.maestroDeterminista(numero_reinas, n_iter_n_queens)

    def generarSimulacion(self):
        if not self.num_retadores == len(self.list_retadores):
            min_tiempo_entre_llegadas = self.tiempo_entre_llegadas-self.desv_tiempo_llegadas
            max_tiempo_entre_llegadas = self.tiempo_entre_llegadas+self.desv_tiempo_llegadas
            tiempo_entre_llegadas = r.randint(min_tiempo_entre_llegadas, max_tiempo_entre_llegadas)
            tiempo_tarda = self.solucion(self.numero_reinas)
            print("Tarda: ")
            print tiempo_tarda
            if Retador.posLlegada > 0:
                tiempo_llegada = self.list_retadores[-1].tiempo_llegada + \
                    tiempo_entre_llegadas
                timepo_salida = max(self.list_retadores[-1].tiempo_salida, tiempo_llegada) + \
                    tiempo_tarda
            else:
                tiempo_llegada = tiempo_entre_llegadas
                timepo_salida = tiempo_llegada + tiempo_tarda

            retador = Retador( tiempo_llegada, tiempo_tarda, timepo_salida,0)
            evento_futuro = Evento(tiempo_llegada,  "L", retador)
            self.actualizarlistaEventosFuturos(evento_futuro,  True)

            if self.reloj == 0:
                evento_ocurrido = Evento(
                    self.reloj,  "L", Retador(0, 0, 0, None))
                self.actualizarHistoricoEventos(evento_ocurrido)

            self.llegada(evento_futuro)
            self.actualizarlistaEventosFuturos(self.listaEventosFuturos[0],  False)
            self.generarSimulacion()
        elif len(self.listaEventosFuturos) == 0:
            return
        else:
            self.salida(self.listaEventosFuturos[0])
            self.generarSimulacion()

    def actualizarlistaEventosFuturos(self, evento,  es_futuro):
        if not es_futuro:
            self.reloj = self.listaEventosFuturos[0].tiempo_ocurrencia
            self.listaEventosFuturos.pop(0)
            self.actualizarHistoricoEventos(evento)
        else:
            if evento.tipo == "L":
                for evento_aux in self.listaEventosFuturos:
                    if evento_aux.tiempo_ocurrencia > evento.tiempo_ocurrencia:
                        indice = self.listaEventosFuturos.index(evento_aux)
                        self.listaEventosFuturos.insert(indice, evento)
                        break
                if evento not in self.listaEventosFuturos:
                    self.listaEventosFuturos.append(evento)
                evento_salida = Evento(
                    evento.entidad.tiempo_salida, "S", evento.entidad)
                self.listaEventosFuturos.append(evento_salida)
            else:
                self.listaEventosFuturos.append(evento)

    def actualizarHistoricoEventos(self, evento_ocurrido):
        registro = []
        listaEventosFuturos_actual = self.listaEventosFuturos[:]
        cola_actual = self.cola
        cola_max_actual = self.cola_max
        atendidos_actual = self.atendidos
        estado_servidor = self.maestro_ocupado
        registro.append(evento_ocurrido)  # 0
        registro.append(listaEventosFuturos_actual)  # 1
        registro.append(cola_actual)  # 2
        registro.append(cola_max_actual)  # 3
        registro.append(atendidos_actual)  # 4
        registro.append(estado_servidor)  # 5
        self.historico_eventos.append(registro)  # 6
        

if __name__ == "__main__":
    start = Simulacion(10, 8, 30, 7)
    start.generarSimulacion()
    

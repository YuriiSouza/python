import threading #biblioteca que impolementa threads
import time

recurso_disponivel = False
cv = threading.Condition()

#metedo que implementa a thread produtor
def produtor():
    global recurso_disponivel
    while True:
        with cv:
            recurso_disponivel = True
            print("Produtor: recurso Produzido!")
            cv.notify_all() #notifica os consumidores
        time.sleep(1)

def consumidor(id):
    global recurso_disponivel
    while True:
        with cv:
            while not recurso_disponivel:
                cv.wait()
            #consome o recurso
            print("consumidor", id, ": Recurso consumido!")
            recurso_disponivel = False
            
        #aguarda um tempo antes de consumir novamente
        time.sleep(0.5)
        

def main():
    consumers = []
    t1 = threading.Thread(target=produtor)
    
    quantConsumer = int(input("Quantidade de usuários: "))
    
    for n in range(0, quantConsumer):
        t = threading.Thread(target=consumidor, args=(n+1,))#cons1
        consumers.append(t)
            
    t1.start()
    for cons in consumers:
        cons.start()
    
    t1.join()
    for cons in consumers:
        cons.join()
    
if __name__ == "__main__":
    main()
    
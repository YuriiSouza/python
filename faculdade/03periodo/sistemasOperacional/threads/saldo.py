import threading
#dicionario para armazenar os saldos das contas
saldos = { "conta A": 1000, "conta B": 1500}

semaforo = threading.Semaphore()
#funcao para transferencia bancaria
def transferencia_bancaria(valor, conta_origem, conta_destino):
    global saldos
    #bloqueia o acessso aos salfos das contas
    semaforo.acquire()
    #atualiza o saldo das contas e transfere os calores
    try:
        if saldos[conta_origem] >= valor:
            saldos[conta_origem] -= valor
            saldos[conta_destino] += valor
            print(f"Transferencia de R${valor:.2f} da {conta_origem} para {conta_destino}")
        else:
            print(f"Saldo insuficiente na {conta_origem}")
    finally:
        #libera semaforo
        semaforo.release()
    
        
def main():
    while True:
        print(f"Saldo da Conta A: {saldos['conta A']:.2f}")
        print(f"Saldo da Conta B: {saldos['conta B']:.2f}")
        try:
            valorAB = float(input("valor de A para B: "))
        except:
            print("valor invalido")
            
        thread1 = threading.Thread(target=transferencia_bancaria, args=(valorAB,"conta A", "conta B"))
        
        try:
            valorBA = float(input("valor de B para A: "))
        except:
            print("valor invalido")
            
        thread2 = threading.Thread(target=transferencia_bancaria, args=(valorBA, "conta B", "conta A"))
        #inicia as threads
        thread1.start()
        thread2.start()
    
        #espera ate qie as threads terminem
        thread1.join()
        thread2.join()
        #imprimem os saldos atualizados
        
        print(f"Saldo final da Conta A: {saldos['conta A']:.2f}")
        print(f"Saldo final da Conta B: {saldos['conta B']:.2f}")
        
        
        continuar = str(input("deseja fazer mais uma transferencia?")).lower()
        
        if 'n' in continuar:
            break
        
    
    
#executar o programa
if __name__ == '__main__':
    main()
    
import time

class Task:
    def __init__(self, name, duration):
        self.name = name
        self.durantion = duration
        
        
class MonoProgramingSimulator:
    def __init__(self):
        #file de processos para execucao
        self.task_queue = []
    #adiciona o novo processo para 
    def add_task(self, task):
        self.task_queue.append(task)
    #execut os processos da fila
    
    def run(self):
        while self.task_queue:
            current_task = self.task_queue.pop(0)
            print(f"Executanto: {current_task.name}")
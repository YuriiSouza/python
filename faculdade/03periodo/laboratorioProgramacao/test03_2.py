import unittest
from exec03_2 import *

class Test(unittest.TestCase):
    def test_record():
        # Preparação
        expected_data = [[30, 'M', 3000.0, 2], [25, 'F', 2500.0, 1], [40, 'M', 4000.0, 3]]
        
        # Execução
        actual_data = record(3)

        # Verificação
        assert actual_data == expected_data, f"Esperado: {expected_data}, Obtido: {actual_data}"

        print("Todos os testes passaram com sucesso!")

    # Executar o teste
    test_record()
    
test = Test()

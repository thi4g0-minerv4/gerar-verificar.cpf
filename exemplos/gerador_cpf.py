## Importação da classe----
import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from CPFValidaClass import CPFValida
## Importação da classe----

input('\n\n\n\nO código a seguir contém loop infinito, pressione ENTER para continuar\n')

while True:
    new_cpf = CPFValida().gerar_cpf()
    print(CPFValida().formatar_cpf(new_cpf))


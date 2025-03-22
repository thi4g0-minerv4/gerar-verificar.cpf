## Importação da classe----
import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from CPFValidaClass import CPFValida
## Importação da classe----

# Uso da classe CPFValida

# Criar uma instância (Argumento único: CPF)
meu_cpf = CPFValida('54705438892')

# verificar_cpf(justify: bool) -> Retorna True se o CPF for válido, False caso contrário
if meu_cpf.verificar_cpf(justify=True): # justify: bool (envia o motivo do erro, caso seja válido envia 'Tudo certo com o CPF'. O valor padrão é False)
    print(f'CPF {meu_cpf.cpf} válido')
else:
    print('CPF inválido')


# O CPF formatado fica salvo no atributo cpf_formated
print(meu_cpf.cpf_formated)

# estado_emitido(siglas: bool) -> Retorna uma lista com os estados possíveis onde o CPF pode ter sido emitido.
estados = meu_cpf.estado_emitido(siglas=True) # siglas: bool (Caso True retorna as siglas dos estados, caso False, retorna o nome dos estados. O valor padrão é True)
# print(estados) # Retornará ['SP']
if 'SP' in estados:
    print('Seu CPF foi emitido no estado de São Paulo')
else:
    pass
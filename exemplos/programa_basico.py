## Importação da classe----
import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from CPFValidaClass import CPFValida
## Importação da classe----


def questionario():

    cpf_user = input('Digite seu CPF no terminal:   ')

    cpf_user_validate = CPFValida(cpf_user)

    if cpf_user_validate.verificar_cpf(justify=False):
        pass
    else:
        print('CPF inválido, reenvie seu CPF\n')
        questionario()
        return

    estados_sigla= cpf_user_validate.estado_emitido(siglas=True)
    estados_nome= cpf_user_validate.estado_emitido(siglas=False)
    if len(estados_sigla) <=1:
        input(f'CPF válido. Você é de {estados_sigla[0]}, não é?  ')
        print('Legal!')
    else:
        resposta = int(input(f'CPF válido. De qual desses estados você é: \n{ "\n".join([f"{i+1}. {item}" for i, item in enumerate(estados_nome)])}\nDigite o número correspondente ao estado: '))
        print(f'Que legal, eu já fui para {estados_sigla[resposta - 1]} e gostei muito!')

questionario()
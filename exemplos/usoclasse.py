# ---------------------- importando a classe ---------------------- #
import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from CPFValidaClass import CPFValida

# ----------------------| CPFVALIDA |---------------------- #

# criando uma instância
cpf_classe = CPFValida('752-83122581')

# ---------------------- atributos classe ---------------------- #
"""
Os atributos são gerados automaticamente pelo metódo construtor.
Os atributos refletem informações que podem ser obtidas pelos metódos da classe.
Caso o parametro cpf não seja passado retornam None.
"""
print(cpf_classe.cpf_input)       # 752-83122581 -> CPF passado
print(cpf_classe.cpf)             # 75283122581 -> CPF número  / Com esse atributo serão realizados os metódos e a definição dos outros atributos 
print(cpf_classe.cpf_formatado)    # 752.831.225-81 -> CPF formatado
print(cpf_classe.cpf_valido)      # True -> Se o CPF é válido ou não
print(cpf_classe.estados)         # ['BA', 'SE'] -> Array com os possíveis estados de emissão

# ---------------------- métodos classe  ---------------------- #

cpf_class = CPFValida()

# --- método: formatar_cpf() ---
"""
formatar_cpf(cpf: str) -> str (Formata desde que não tenha caracteres inválidos e caracteres suficientes / mesmo se for inválido.)

-cpf (str): CPF a ser formatado. Padrão: self.cpf
"""
cpf = '56008293703'
print(cpf_class.formatar_cpf(cpf)) # 560.082.937-03


# --- método: verificar_cpf() ---
"""
verificar_cpf(cpf: str) -> bool (True se for válido. False se for inválido.)

-cpf (str): CPF a ser verificado (Padrão: self.cpf).
"""
if cpf_class.verificar_cpf(cpf=cpf):
    print(f'CPF {cpf_class.formatar_cpf(cpf)} válido')
else:
    print(f'CPF {cpf_class.formatar_cpf(cpf)} inválido')


# --- método: estado_emitido() ---
"""
estado_emitido(cpf: str, siglas: bool = True) -> list

-cpf (str): CPF cujo estado de emissão será identificado. (Só aceita CPF's válidos. Padrão: self.cpf)
-siglas (bool): Se True, retorna a sigla do estado. Se False, retorna o nome completo. (Padrão: True.)
"""
estados = cpf_class.estado_emitido(cpf=cpf, siglas=False)
print(f'Possível estado de emissão: {', '.join(estados)}')  # São Paulo

# --- método: gerar_cpf() ---
"""
gerar_cpf() -> str

Gera e retorna um CPF válido aleatório.
"""
novo_cpf = cpf_class.gerar_cpf()
print(f'CPF gerado: {novo_cpf}')
print(f'O CPF gerado é válido? {cpf_class.verificar_cpf(cpf=novo_cpf)}')  # Sempre True
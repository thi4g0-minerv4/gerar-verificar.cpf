# ---------------------- importando a classe ---------------------- #
import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from CPFValidaClass import CPFValida

# ----------------------| CPFVALIDA |---------------------- #

# criando uma instância
meu_cpf = CPFValida(cpf='54705438832')

# ---------------------- atributos classe ---------------------- #
"""
Os atributos são gerados automaticamente pelo metódo construtor.
Os atributos refletem informações que podem ser obtidas pelos metódos da classe.
Caso o parametro cpf não seja passado retornam None.
"""
print(meu_cpf.cpf)             # 54705438892 -> CPF passado
print(meu_cpf.cpf_formated)    # 547.054.388-92 -> CPF formatado
print(meu_cpf.cpf_valido)      # True -> Se o CPF é válido ou não
print(meu_cpf.estados)         # ['SP'] -> Array com os possíveis estados de emissão

# ---------------------- métodos classe  ---------------------- #

cpf_tool = CPFValida()

# --- método: formatar_cpf() ---
"""
formatar_cpf(cpf: str) -> str 

-cpf (str): CPF a ser formatado (Só aceita CPF's válidos. Padrão: self.cpf).
"""
cpf = '56008293703'
print(cpf_tool.formatar_cpf(cpf)) # 560.082.937-03


# --- método: verificar_cpf() ---
"""
verificar_cpf(cpf: str, justify: bool = False) -> bool

-cpf (str): CPF a ser verificado (Padrão: self.cpf).
-justify (bool): Se True, retorna a justificativa da validade/invalidez. (Padrão: False.)
"""
cpf = '54705438892'
if cpf_tool.verificar_cpf(cpf=cpf, justify=True):
    print(f'CPF {cpf_tool.formatar_cpf(cpf)} válido')
else:
    print(f'CPF {cpf_tool.formatar_cpf(cpf)} inválido')


# --- método: estado_emitido() ---
"""
estado_emitido(cpf: str, siglas: bool = True) -> list

-cpf (str): CPF cujo estado de emissão será identificado. (Só aceita CPF's válidos. Padrão: self.cpf)
-siglas (bool): Se True, retorna a sigla do estado. Se False, retorna o nome completo. (Padrão: True.)
"""
estados = cpf_tool.estado_emitido(cpf=cpf, siglas=False)
print(f'Possível estado de emissão: {', '.join(estados)}')  # ['São Paulo']

# --- método: gerar_cpf() ---
"""
gerar_cpf() -> str

Gera e retorna um CPF válido aleatório.
"""
novo_cpf = cpf_tool.gerar_cpf()
print(f'CPF gerado: {novo_cpf}')
print(f'O CPF gerado é válido? {cpf_tool.verificar_cpf(cpf=novo_cpf)}')  # Sempre True
#  Gerar e Validar CPF com Python (E mais...) 🪪 


## Descrição 📍

Classe CPFValida, que realiza: <strong>Validação</strong>, <strong>Geração</strong> e <strong>Formatação</strong> de um CPF, além de retornar os possíveis <strong>estados de emissão</strong>.

### Utilidades Gerais ⚙️
<ul>
    <li>Verificar validade de qualquer CPF.</li>
    <li>Invalida CPF's como 111.111.111-11 e 222.222.222-22.</li>
    <li>Pode gerar milhões CPF's de forma otimizada.</li>
    <li>Busca o estado de emissão do CPF.</li>
    <li>Formata qualquer CPF para forma padrão.</li>
    <li>Facilita no uso da API da Receita Federal.</li>
</ul>

#
## Importação 🔃

Importe da seguinte forma:

```bash
from CPFValidaClass import CPFValida
```
*Nenhum Biblioteca necessária
<br>
<br>

## Uso 💻

### Criando instância <code>CPFValida</code>:</strong>

A classe recebe um único parâmetro, que é o CPF em si. (Que é opcional. Padrão: None)
```bash
# Criando instância a partir da classe
meu_cpf = CPFValida('54705438892') # Exemplo com CPF válido
meu_cpf2 = CPFValida('547.054.388-92') # Também podem ser passados com a formatação completa. O funcionamento continua o mesmo
cpf_do_bob = CPFValida('nao lembro') # CPF inválido podem ser usados sem problemas na definição de classe
```
#


### Atributos:

Os atributos são gerados automaticamente pelo método construtor.
Os atributos refletem informações que podem ser obtidas pelos metódos da classe.
Caso o parametro cpf não seja passado retornam ```None```.
#
<strong>```self.cpf```:</strong> Recebe o valor do CPF passado (```str```) <br>
<strong>```self.cpf_formated```:</strong> Armazena o CPF formatado (```str```). Caso o CPF seja inválido recebe o valor ```None```<br>
<strong>```self.cpf_valido```:</strong> Se o CPF é válido ou não (```bool```)<br>
<strong>```self.estados```:</strong> Array com os possíveis estados de emissão (```list```). Caso o CPF seja inválido recebe o valor ```None```<br><br>

<small>Você pode encontrar mais exemplos do uso da classe na pasta ```exemplos```. </small>


#

### Métodos:
Métodos acessíveis pela classe. O parâmetro ```cpf: str``` caso não passado será por padrão ```self.cpf```.
#
<br>
<strong>Método <code>formatar_cpf(cpf: str)</code>:</strong>

Formata CPF para forma padrão.
```bash
# --- método: formatar_cpf() ---
"""
formatar_cpf(cpf: str) -> str 

-cpf (str): CPF a ser formatado (Só aceita CPF's válidos. Padrão: self.cpf).
"""
cpf = '56008293703'
print(cpf_tool.formatar_cpf(cpf)) # 560.082.937-03

```
<br>
<strong>Método <code>verificar_cpf(cpf: str, justify: bool)</code>:</strong>


Verifica se o CPF é válido, retornando True ou False
```bash
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

```
<br>
<strong>Método <code>estado_emitido(siglas: bool)</code>:</strong>

Envia um array com os estados possíveis de emissão do CPF.

```bash
# --- método: estado_emitido() ---
"""
estado_emitido(cpf: str, siglas: bool = True) -> list

-cpf (str): CPF cujo estado de emissão será identificado. (Só aceita CPF's válidos. Padrão: self.cpf)
-siglas (bool): Se True, retorna a sigla do estado. Se False, retorna o nome completo. (Padrão: True.)
"""
estados = cpf_tool.estado_emitido(cpf=cpf, siglas=False)
print(f'Possível estado de emissão: {', '.join(estados)}')  # ['São Paulo']
```
<br>
<strong>Método <code>gerar_cpf()</code>:</strong>

Gera um CPF válido.

```bash
# --- método: gerar_cpf() ---
"""
gerar_cpf() -> str

Gera e retorna um CPF válido aleatório.
"""
novo_cpf = cpf_tool.gerar_cpf()
print(f'CPF gerado: {novo_cpf}')
print(f'O CPF gerado é válido? {cpf_tool.verificar_cpf(cpf=novo_cpf)}')  # Sempre True
```


<br>

<small>Você pode encontrar mais exemplos do uso da classe na pasta ```exemplos```. Como: gerador infinito de CPFs, programa básico de verificação e o código e a documentação do uso da classe. </small>


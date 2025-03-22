#  Verificar CPF e Retornar Estados com Python 🪪


## Descrição 📍

Classe CPFValida, que recebe um único parâmetro, sendo o CPF. Dentro da classe temos dois métodos: verificar_cpf, que retorna True caso o CPF seja válido e estado_emitido, que retorna um array com os estados aonde o CPF pode ter sido emitido. 

## Importação 🔃

Importe da seguinte forma:

```bash
from CPFValidaClass import CPFValida
```

<br>

#
### 💻 Uso: 

<strong>Criando instância <code>CPFValida</code>:</strong>

A classe recebe um único parâmetro, que é o CPF em si.
```bash
# Criando instância a partir da classe
meu_cpf = CPFValida('54705438892') # Exemplo com CPF válido
meu_cpf = CPFValida('547.054.388-92') # Também podem ser passados com a formatação completa. O funcionamento continua o mesmo 
cpf_do_bob = CPFValida('nao lembro') # CPF inválido podem ser usados sem problemas na definição de classe
```

<br>
<strong>Método <code>verificar_cpf(justify: bool)</code>:</strong>

Verifica se o CPF é válido, retornando True ou False
```bash
# verificar_cpf(justify: bool) -> Retorna True se o CPF for válido, False caso contrário
if meu_cpf.verificar_cpf(justify=True): # justify: bool (envia o motivo da invalidação, caso seja válido envia uma mensagem de confirmação. O valor padrão é False)
    print(f'CPF {meu_cpf.cpf} válido') 
else:
    print('CPF inválido')
```
<br>
<strong>Método <code>estado_emitido(siglas: bool)</code>:</strong>

Envia um array com os estados possíveis de emissão do CPF.

```bash
# estado_emitido(siglas: bool) -> Retorna uma lista com os estados possíveis onde o CPF pode ter sido emitido.
estados = meu_cpf.estado_emitido(siglas=True) # siglas: bool (Caso True retorna as siglas dos estados, caso False, retorna o nome dos estados. O valor padrão é True)
# print(estados) # Retornará ['SP']

estados_nome = meu_cpf.estado_emitido(siglas=False)
# print(estados_nome) # Retornará ['São Paulo']

if 'SP' in estados:
    print('Seu CPF foi emitido no estado de São Paulo')
else:
    pass
```
<br>
<strong>Atributos:</strong>

<strong><code>```self.cpf```</code>:</strong> Recebe o valor do CPF inserido(Deve ser do tipo ```str```) <br>
<strong><code>```self.cpf_formated```</code>:</strong> Armazena o CPF formatado. Caso o CPF seja inválido recebe o valor ```None```


<small>Você pode encontrar mais exemplos do uso da classe na pasta ```exemplos```. </small>


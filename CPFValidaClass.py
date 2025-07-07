import random ## PARA gerar_cpf()

## CLASSE CPF VALIDA
class CPFValida:

    def __init__(self, cpf: str = None):

        self.cpf_input = cpf
        
        if cpf:
            self.cpf = self.__clear_cpf(self.cpf_input) ## ATRIBUTO PRINCIPAL

            self.cpf_valido = self.verificar_cpf(self.cpf)
            self.cpf_formatado = self.formatar_cpf(self.cpf)
            self.estados = self.estado_emitido(self.cpf)
        else:
            self.cpf = None
            self.cpf_valido = None
            self.cpf_formatado = None
            self.estados = None

    def gerar_cpf(self) -> str:

        numeros =[random.randint(0,9) for _ in range(9)] ## GERA PRIMEIRO 9 NÚMEROS

        primeiro_comparador = self.__calcular_comparador(numeros) ## CALCULA 10° COM BASE NELES
        numeros.append(primeiro_comparador)

        segundo_comparador = self.__calcular_comparador(numeros) ## CALCULA 11° COM BASE NELES
        numeros.append(segundo_comparador)
        return ''.join(map(str, numeros))

    def verificar_cpf(self, cpf: str = None) -> bool:

        cpf = self.__clear_cpf(cpf or self.cpf)

        if not cpf.isdigit(): return False  ## VERIFICAÇÃO CARACTERES INVALIDOS 
            
        if len(cpf) != 11: return False  ## VERIFICA QUANTIDADE CHAR
        
        if cpf in ["00000000000", "11111111111", "22222222222", "33333333333", "44444444444", "55555555555", "66666666666", "77777777777", "88888888888", "99999999999"]: return False ## VERIFICA PREVIAMENTE CPFs INVÁLIDOS

        ## DIVIDE O CPF EM PARTES PARA REALIZAR O CÁLCULO
        verificadores, numeros_calculo = list(cpf[9:]), list(cpf[:9])
        comparador_0  =self.__calcular_comparador(numeros_calculo) 
        
        if not comparador_0 == int(verificadores[0]): return False ## VERIFICA SE OS COMPARADORES SÃO IGUAIS OS NUMEROS VERIFICADORES

        numeros_calculo.append(comparador_0)
        comparador_1 = self.__calcular_comparador(numeros_calculo)
        
        if not comparador_1 == int(verificadores[1]): return False
        
        numeros_calculo.append(comparador_1) ## NUMEROS CALCULO = CPF
        
        return True

    def estado_emitido(self, cpf: str =None, siglas: bool = True) ->list:

        cpf = self.__clear_cpf(cpf or self.cpf)

        if not self.verificar_cpf(cpf): return None ## VERIFICA CPF

        if siglas:
            estados = {
                '1': ['DF', 'GO', 'MS', 'MT', 'TO'],
                '2': ['AC', 'AM', 'AP', 'PA', 'RO', 'RR'],
                '3': ['CE', 'MA', 'PI'],
                '4': ['AL', 'PB', 'PE', 'RN'],
                '5': ['BA', 'SE'],
                '6': ['MG'],
                '7': ['ES', 'RJ'],
                '8': ['SP'],
                '9': ['PR', 'SC'],
                '0': ['RS'],
            }
        else:
            estados = {
                '1': ['Distrito Federal', 'Goiás', 'Mato Grosso do Sul', 'Mato Grosso', 'Tocantins'],
                '2': ['Acre', 'Amazonas', 'Amapá', 'Pará', 'Rondônia', 'Roraima'],
                '3': ['Ceará', 'Maranhão', 'Piauí'],
                '4': ['Alagoas', 'Paraíba', 'Pernambuco', 'Rio Grande do Norte'],
                '5': ['Bahia', 'Sergipe'],
                '6': ['Minas Gerais'],
                '7': ['Espírito Santo', 'Rio de Janeiro'],
                '8': ['São Paulo'],
                '9': ['Paraná', 'Santa Catarina'],
                '0': ['Rio Grande do Sul'],
            }

        digito_verificador = cpf[8] ## DIGITO QUE ARMAZENA O CPF
        return estados.get(digito_verificador)

    def formatar_cpf(self, cpf: str = None):
        cpf = self.__clear_cpf(cpf or self.cpf)

        if len(cpf) == 11 and cpf.isdigit():
            cpf_formatado = f'{cpf[:3]}.{cpf[3: 6:]}.{cpf[6: 9:]}-{cpf[9:]}'
            return cpf_formatado
        else: 
            return None

    @staticmethod
    def __calcular_comparador(numeros_calculo):
        soma_total = sum(int(d) * (len(numeros_calculo) + 1 - i) for i, d in enumerate(numeros_calculo))
        comparador = 11 - soma_total % 11
        return 0 if comparador in [10, 11] else comparador
    @staticmethod
    def __clear_cpf(cpf: str):
        return cpf.replace('-', '').replace('.', '')
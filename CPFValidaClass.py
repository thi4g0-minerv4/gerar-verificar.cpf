## CLASSE
class CPFValida:

    def __init__(self, cpf: str):
        self.cpf = cpf
        self.cpf_formated = self.__cpf_format()

    def verificar_cpf(self, justify: bool = False):
        ## VERIFICAÇÃO CARACTERES INVALIDOS (a-z)
        for char in self.cpf:
            if not char.isdigit() and char not in ['-', '.']:
                if justify:
                    print('O CPF possui caracteres inválidos.')
                return False      
            
        ## ANALISA O FORMATO DO CPF, E SE NECESSARIO FORMATA PARA APENAS NUMEROS
        if self.cpf.isdigit():
            cpf = self.cpf
            pass # Passa para proxima etapa de verificação
        else:
            if len(self.cpf) != 14: # Precisa possuir a estrutura 000.000.000-00 aqui
                if justify:
                    print('Formato do CPF é inválido.')
                return False
            ## FORMATA CPF PARA A OTIMIZAÇAO DO RESTANTE DA VERIFICAÇÃO
            if self.cpf[3]== '.' and self.cpf[7]== '.' and self.cpf[11]== '-': 
                cpf = self.cpf.replace('.', '').replace('-','') # Cria nova variável exclusiva para a verificação, sem modificar a original
            else:
                if justify:
                    print('Formato do CPF é inválido.')
                return False
            
        ## VERIFICA QUANTIDADE CHAR
        if len(cpf) != 11:
            if justify:
                print('Um CPF válido deve ter 11 digitos (Não inclui caracteres especiais: . e -).')
            return False 
        ## DIVIDE O CPF EM PARTES PARA REALIZAR O CALCULO
        verificadores = list(cpf[9:])
        numeros_calculo = list(cpf[:9])
        comparador_0 = self.__calcular_comparador(numeros_calculo)
        ## VERIFICA SE OS COMPARADORES SAO IGUAIS OS NUMEROS VERIFICADORES
        if comparador_0 == int(verificadores[0]):
            numeros_calculo.append(comparador_0)
        else:
            if justify:
                print('O primeiro digito verificador não condiz. Verifique se o CPF foi digitado corretamente.')
            return False
        
        
        comparador_1 = self.__calcular_comparador(numeros_calculo)
        
        if comparador_1 == int(verificadores[1]):
            numeros_calculo.append(comparador_1)
        else:
            if justify:
                print('O segundo digito verificador não condiz. Verifique se o CPF foi digitado corretamente.')
            return False

        if justify:
            print(f'Tudo certo com o CPF: {self.cpf_formated}')
        return True


    def estado_emitido(self, siglas: bool = True):
        ## Verifica o CPF, caso seja inválido retorna None
        if not self.verificar_cpf():
        
        ## Formata o CPF para verificar o estado de forma mais otimizada
        if self.cpf.isdigit():
            cpf = self.cpf
            pass 
        else:
            cpf = self.cpf.replace('.', '').replace('-','')

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

        return estados.get(cpf[8])

    def __cpf_format(self):
        if self.cpf.isdigit():
            if self.verificar_cpf():
                format_cpf = f'{self.cpf[:3]}.{self.cpf[3: 6:]}.{self.cpf[6: 9:]}-{self.cpf[9:]}'
                return format_cpf
            else:
                return None
        else:
            if self.verificar_cpf():
                return self.cpf
            else:
                return None
    
    @staticmethod
    def __calcular_comparador(numeros_calculo):
        soma_total = sum(int(d) * (len(numeros_calculo) + 1 - i) for i, d in enumerate(numeros_calculo))
        comparador = 11 - soma_total % 11
        return 0 if comparador in [10, 11] else comparador

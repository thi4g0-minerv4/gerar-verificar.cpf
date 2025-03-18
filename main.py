def calcular_comparador(numeros_calculo):
    
    limitador = len(numeros_calculo) + 1
    lista_soma = []

    for d in numeros_calculo:
        result = int(d) * limitador
        lista_soma.append(result)
        limitador -= 1
    

    soma_total = sum(lista_soma)
    resto = soma_total % 11
    if resto == 10 or resto == 11:
        comparador = 0
    else:
        comparador = 11 - resto
    return comparador



def verificar_cpf(cpf: str, justify: bool = False):

    if not cpf.isdigit():
        if justify:
            print('O CPF deve ter apenas números')
        return False
    if len(cpf) != 11:
        if justify:
            print('Um CPF válido deve ter 11 digitos')
        return False
    

    verificadores = list(cpf[9:])

    numeros_calculo = list(cpf[:9])

    comparador_0 = calcular_comparador(numeros_calculo)
    
    if comparador_0 == int(verificadores[0]):
        numeros_calculo.append(comparador_0)
    else:
        if justify:
            print('O primeiro digito verificador não condiz. Verifique se o CPF foi digitado corretamente.')
        return False
    
    
    comparador_1 = calcular_comparador(numeros_calculo)
    
    if comparador_1 == int(verificadores[1]):
        numeros_calculo.append(comparador_1)
    else:
        if justify:
            print('O segundo digito verificador não condiz. Verifique se o CPF foi digitado corretamente.')
        return False

    cpf_verificado = numeros_calculo

    (cpf_verificado)
    return True



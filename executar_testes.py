def executar_testes():
    procedimentos = ler_dados_xml("dados_teste.xml")
    
    for procedimento in procedimentos:
        driver = abrir_calculadora()
        nome_procedimento = procedimento['nome']
        
        if nome_procedimento == "Adicao":
            for caso in procedimento['casos']:
                teste_adicao(driver, caso['valor1'], caso['valor2'], caso['resultado_esperado'])
        
        elif nome_procedimento == "Subtracao":
            for caso in procedimento['casos']:
                teste_subtracao(driver, caso['valor1'], caso['valor2'], caso['resultado_esperado'])
        
        elif nome_procedimento == "Multiplicacao":
            for caso in procedimento['casos']:
                teste_multiplicacao(driver, caso['valor1'], caso['valor2'], caso['resultado_esperado'])
        
        elif nome_procedimento == "Divisao":
            for caso in procedimento['casos']:
                teste_divisao(driver, caso['valor1'], caso['valor2'], caso['resultado_esperado'])
        
        elif nome_procedimento == "Exponenciacao":
            for caso in procedimento['casos']:
                teste_exponenciacao(driver, caso['valor1'], caso['valor2'], caso['resultado_esperado'])
        
        driver.quit()



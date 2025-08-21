def calcular(VP, VN, FP, FN):
    """
    Calcula as métricas de avaliação de aprendizado.
    
    Parâmetros:
        VP: Verdadeiros Positivos
        VN: Verdadeiros Negativos
        FP: Falsos Positivos
        FN: Falsos Negativos
    
    Retorna:
        Um dicionário com as métricas calculadas.
    """
    # Cálculo das métricas
    acuracia = (VP + VN) / (VP + VN + FP + FN)
    precisao = VP / (VP + FP) if (VP + FP) != 0 else 0
    sensibilidade = VP / (VP + FN) if (VP + FN) != 0 else 0  # recall
    especificidade = VN / (VN + FP) if (VN + FP) != 0 else 0
    f_score = (2 * precisao * sensibilidade) / (precisao + sensibilidade) if (precisao + sensibilidade) != 0 else 0

    # Criar dicionário
    return {
        "Acurácia": acuracia,
        "Precisão": precisao,
        "Sensibilidade (Recall)": sensibilidade,
        "Especificidade": especificidade,
        "F-Score": f_score,
    }

# Exemplo de matriz de confusão (valores arbitrários)
VP = 75  # Verdadeiros Positivos
VN = 60  # Verdadeiros Negativos
FP = 15  # Falsos Positivos
FN = 30  # Falsos Negativos

# Calcular métricas
metricas = calcular(VP, VN, FP, FN)

# Exibir resultados
print("Métricas de Avaliação:")
for metrica, valor in metricas.items():
    print(f"{metrica}: {valor:.2f}")

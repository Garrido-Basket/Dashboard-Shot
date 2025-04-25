# analytics/porcentaje_tiro.py

def calcular_porcentaje_tiro(tiros_acertados: int, tiros_intentados: int) -> float:
    """
    Devuelve el porcentaje de tiro dado el número de tiros acertados y tiros intentados.
    """
    if tiros_intentados == 0:
        return 0.0
    return (tiros_acertados / tiros_intentados) * 100

# Ejemplo de uso:
if __name__ == "__main__":
    print(calcular_porcentaje_tiro(8, 10))  # Debería imprimir 80.0
def brincadeira(numero: int) -> int | str:
    print("Entrei na brincadeira!")
    if numero < 3 or numero == 4:
        return numero
    if numero % 3 == 0:
        return "queijo"
    if numero > 4:
        return "goiabada"

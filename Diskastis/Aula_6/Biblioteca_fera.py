def pedestal_m(n):
    if n == 1:
        return 1
    
    return 2 * pedestal_m(n - 1) + 1

qtd_livro = int(input())
qtd_movimentos = (2 ** qtd_livro) - 1

print(f"Bela moveu os {qtd_livro} livros em {qtd_movimentos} movimentos para o Pedestal de Marfim.")
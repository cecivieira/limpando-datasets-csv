import pandas as pd

class LimparConjuntoDados:
    def __init__(self, arquivo, titulo):
        self.arquivo = arquivo
        self.titulo = titulo
        self.colunasRemover = []

    
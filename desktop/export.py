# export.py
import csv

def generate_packing_list(tecidos: list[Tecido], filename: str):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Ordem", "Lote", "Produto", ..., "Largura"])
        for tecido in tecidos:
            writer.writerow([tecido.ordem, tecido.lote, ..., tecido.largura])
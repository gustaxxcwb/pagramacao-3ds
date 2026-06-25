class Veiculo:
    def __init__(self, consumo_km_l, preco_combustivel):
        self.consumo_km_l = consumo_km_l
        self.preco_combustivel = preco_combustivel

    def calcular_custo_viagem(self, distancia):
        return (distancia / self.consumo_km_l) * self.preco_combustivel

def calcular_custo_total_frota(veiculos):
    distancia = 200
    custo_total = 0
    
    for veiculo in veiculos:
        custo_total += veiculo.calcular_custo_viagem(distancia)
        
    return custo_total

# Exemplo de uso:
# veiculo1 = Veiculo(consumo_km_l=10, preco_combustivel=5.50)
# veiculo2 = Veiculo(consumo_km_l=15, preco_combustivel=5.50)
# frota = [veiculo1, veiculo2]
# print(f"Custo total: R$ {calcular_custo_total_frota(frota):.2f}")

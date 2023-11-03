class Resultado:
  def __init__(self, cliente, cobertura, capital, premio_mensal, premio_anual):
    self.cliente = cliente
    self.cobertura = cobertura
    self.capital = capital
    self.premio_mensal = premio_mensal
    self.premio_anual = premio_anual

  def __str__(self):
    return f"{self.cobertura};{self.capital};{self.premio_mensal};{self.premio_anual}"

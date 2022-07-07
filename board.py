import random
import time

# jogadores
jogadores = dict()

jogadores = {"impulsivo": {"jogador": "impulsivo", "saldo": 300, "posicao": 0},
             "exigente": {"jogador": "exigente", "saldo": 300, "posicao": 0},
             "cauteloso": {"jogador": "cauteloso", "saldo": 300, "posicao": 0},
             "aleatorio": {"jogador": "aleatorio", "saldo": 300, "posicao": 0}}

# dado
dado = random.sample(range(1, 6), k=1)

# propriedades
propriedades = dict()

propriedades = {
    "Copacabana": {
        "propriedade": "Copacabana",
        "aluguel": random.sample(range(10, 50), k=1),
        "venda": random.sample(range(60, 100), k=1),
        "vendido": 0,
        "proprietario:": str
    },
    "Leblon": {
        "propriedade": "Leblon",
        "aluguel": random.sample(range(10, 50), k=1),
        "venda": random.sample(range(60, 100), k=1),
        "vendido": 0,
        "proprietario:": str,
    },
    "Ipanema": {
        "propriedade": "Ipanema",
        "aluguel": random.sample(range(10, 50), k=1),
        "venda": random.sample(range(60, 100), k=1),
        "vendido": 1,
        "proprietario:": str,
    },
    "Gávea": {
        "propriedade": "Gávea",
        "aluguel": random.sample(range(10, 50), k=1),
        "venda": random.sample(range(60, 100), k=1),
        "vendido": 0,
        "proprietario:": str,
    },
    "Jardim Botânico": {
        "propriedade": "Jardim",
        "aluguel": random.sample(range(10, 50), k=1),
        "venda": random.sample(range(60, 100), k=1),
        "vendido": 0,
        "proprietario:": str,
    },
    "Lagoa": {
        "propriedade": "Lago",
        "aluguel": random.sample(range(10, 50), k=1),
        "venda": random.sample(range(60, 100), k=1),
        "vendido": 1,
        "proprietario:": str,
    },
    "Leme": {
        "propriedade": "Leme",
        "aluguel": random.sample(range(10, 50), k=1),
        "venda": random.sample(range(60, 100), k=1),
        "vendido": 1,
        "proprietario:": str,
    },
    "Humaitá": {
        "propriedade": "Humaitá",
        "aluguel": random.sample(range(10, 50), k=1),
        "venda": random.sample(range(60, 100), k=1),
        "vendido": 1,
        "proprietario:": str,
    },
    "Botafogo": {
        "propriedade": "Botafogo",
        "aluguel": random.sample(range(10, 50), k=1),
        "venda": random.sample(range(60, 100), k=1),
        "vendido": 0,
        "proprietario:": str,
    },
    "Flamengo": {
        "propriedade": "Flamengo",
        "aluguel": random.sample(range(10, 50), k=1),
        "venda": random.sample(range(60, 100), k=1),
        "vendido": 0,
        "proprietario:": str,
    },
    "São Conrado": {
        "propriedade": "São Conrado",
        "aluguel": random.sample(range(10, 50), k=1),
        "venda": random.sample(range(60, 100), k=1),
        "vendido": 1,
        "proprietario:": str,
    },
    "Barra da Tijuca": {
        "propriedade": "Barra da Tijuca",
        "aluguel": random.sample(range(10, 50), k=1),
        "venda": random.sample(range(60, 100), k=1),
        "vendido": 0,
        "proprietario:": str,
    },
    "Recreio": {
        "propriedade": "Recreio",
        "aluguel": random.sample(range(10, 50), k=1),
        "venda": random.sample(range(60, 100), k=1),
        "vendido": 1,
        "proprietario:": str,
    },
    "Itaim Bibi": {
        "propriedade": "Itaim Bibi",
        "aluguel": random.sample(range(10, 50), k=1),
        "venda": random.sample(range(60, 100), k=1),
        "vendido": 0,
        "proprietario:": str,
    },
    "Bairro Ibirapuera": {
        "propriedade": "Bairro Ibirapuera",
        "aluguel": random.sample(range(10, 50), k=1),
        "venda": random.sample(range(60, 100), k=1),
        "vendido": 1,
        "proprietario:": str,
    },
    "Jardim Europa": {
        "propriedade": "Jardim Europa",
        "aluguel": random.sample(range(10, 50), k=1),
        "venda": random.sample(range(60, 100), k=1),
        "vendido": 1,
        "proprietario:": str,
    },
    "Jardim América": {
        "propriedade": "Jardim América",
        "aluguel": random.sample(range(10, 50), k=1),
        "venda": random.sample(range(60, 100), k=1),
        "vendido": 1,
        "proprietario:": str,
    },
    "Moema": {
        "propriedade": "Moema",
        "aluguel": random.sample(range(10, 50), k=1),
        "venda": random.sample(range(60, 100), k=1),
        "vendido": 0,
        "proprietario:": str,
    },
    "Vila Olímpia": {
        "propriedade": "Vila Olímpia",
        "aluguel": random.sample(range(10, 50), k=1),
        "venda": random.sample(range(60, 100), k=1),
        "vendido": 0,
        "proprietario:": str,
    },
    "Higienópolis": {
        "propriedade": "Higienópolis",
        "aluguel": random.sample(range(10, 50), k=1),
        "venda": random.sample(range(60, 100), k=1),
        "vendido": 1,
        "proprietario:": str,
    },
}

# tabuleiro
tabuleiro = dict()
tabuleiro = {
    1: "Copacabana",
    2: "Leblon",
    3: "Ipanema",
    4: "Gávea",
    5: "Jardim Botânico",
    6: "Lagoa",
    7: "Leme",
    8: "Humaitá",
    9: "Botafogo",
    10: "Flamengo",
    11: "São Conrado",
    12: "Barra da Tijuca",
    13: "Recreio",
    14: "Itaim Bibi",
    15: "Bairro Ibirapuera",
    16: "Jardim Europa",
    17: "Jardim América",
    18: "Moema",
    19: "Vila Olímpia",
    20: "Higienópolis",
}
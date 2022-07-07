import random
import time

class Jogadores:
   def __init__(self, jogador:dict, tabuleiro:dict, propriedade:dict):
       self.jogadores = jogador
       self.board = tabuleiro
       self.propriedades = propriedade

   def play(self):
       vencedores = []
       inicio = time.time()
       players = random.sample(["impulsivo", "exigente", "cauteloso", "aleatorio"], k=4)
       total_jogadas = 0
       turnos_stop = 0
       turnos = 0
       partidas = 0

       while partidas < 300:
           for x in players:

               total_jogadas = total_jogadas + 1
               turnos = turnos + 1
               dado = random.sample(range(1, 6), k=1)
               self.jogadores[x]["posicao"] = self.jogadores[x]["posicao"] + dado[0]

               #print(players)
                   ## soma + 100 de saldo virando dando a volta no tabuleiro.
               if self.jogadores[x]["posicao"] > 20 and self.jogadores[x]["saldo"] > 0:
                    self.jogadores[x]["posicao"] = self.jogadores[x]["posicao"] - 20
                    self.jogadores[x]["saldo"] = self.jogadores[x]["saldo"] + 100
                    print("\n")
                    print(f"Jogador {str(self.jogadores[x]['jogador']).upper()} deu a volta no tabuleiro e ganhou + 100 de saldo ")
                    print("Saldo total de:", self.jogadores[x]["saldo"])
                    print("\n")

               elif len(players) == 1:
                   self.jogadores["impulsivo"]["saldo"] = 300
                   self.jogadores["cauteloso"]["saldo"] = 300
                   self.jogadores["exigente"]["saldo"] = 300
                   self.jogadores["aleatorio"]["saldo"] = 300
                   players = random.sample(["impulsivo", "exigente", "cauteloso", "aleatorio"], k=4)
                   vencedores.append(self.jogadores[x]['jogador'])
                   partidas = partidas + 1

               elif turnos == 1000:
                   turnos_stop = turnos_stop + 1

               ## valida se o jogador tem saldo negativo.
               elif self.jogadores[x]["saldo"] <= 0:
                   print(f"O jogador {str(self.jogadores[x]['jogador']).upper()} perdeu porque seu saldo é de: {self.jogadores[x]['saldo']}")
                   players.remove(self.jogadores[x]["jogador"])


               elif self.jogadores[x]["saldo"] < self.propriedades[self.board[self.jogadores[x]["posicao"]]]["aluguel"][0] and self.propriedades[self.board[self.jogadores[x]["posicao"]]]["vendido"] == 0:
                    print(f"O jogador {str(self.jogadores[x]['jogador']).upper()} perdeu o jogo porque não possui condicōes de alugar a propriedade:", self.propriedades[self.board[self.jogadores[x]["posicao"]]]["propriedade"], "pelo valor de:", self.propriedades[self.board[self.jogadores[x]["posicao"]]]["aluguel"][0], "- saldo:", self.jogadores[x]["saldo"])
                    self.propriedades[self.board[self.jogadores[x]["posicao"]]]["vendido"] = 0
                    self.propriedades[self.board[self.jogadores[x]["posicao"]]]["proprietario"] = str

                    players.remove(self.jogadores[x]["jogador"])



               elif self.propriedades[self.board[self.jogadores[x]["posicao"]]]["vendido"] == 1 and self.jogadores[x]["saldo"] >= self.propriedades[self.board[self.jogadores[x]["posicao"]]]["aluguel"][0]:
                    self.jogadores[x]["saldo"] = self.jogadores[x]["saldo"] - self.propriedades[self.board[self.jogadores[x]["posicao"]]]["aluguel"][0]
                    print(f"O jogador {str(self.jogadores[x]['jogador']).upper()} parou na propriedade: ", self.propriedades[self.board[self.jogadores[x]["posicao"]]]["propriedade"])
                    print(f"O jogador {str(self.jogadores[x]['jogador']).upper()} alugou a propriedade: ", self.propriedades[self.board[self.jogadores[x]["posicao"]]]["propriedade"], "pelo valor de:",self.propriedades[self.board[self.jogadores[x]["posicao"]]]["aluguel"][0], "e o seu saldo é de: ", self.jogadores[x]["saldo"])

               ## jogador impulsivo
               elif self.jogadores[x]["jogador"] == "impulsivo" and self.propriedades[self.board[self.jogadores[x]["posicao"]]]["vendido"] == 0 and self.jogadores[x]["saldo"] >= self.propriedades[self.board[self.jogadores[x]["posicao"]]]["venda"][0]:
                    self.jogadores[x]["saldo"] = self.jogadores[x]["saldo"] - self.propriedades[self.board[self.jogadores[x]["posicao"]]]["venda"][0]
                    print(f"O jogador {str(self.jogadores[x]['jogador']).upper()} parou na propriedade: ", self.propriedades[self.board[self.jogadores[x]["posicao"]]]["propriedade"])
                    print(f"O jogador {str(self.jogadores[x]['jogador']).upper()} comprou a propriedade:", self.propriedades[self.board[self.jogadores[x]["posicao"]]]["propriedade"], "pelo valor de:",self.propriedades[self.board[self.jogadores[x]["posicao"]]]["venda"][0], "e o seu saldo agora é de:", self.jogadores[x]["saldo"])

               ## jogador exigente
               elif self.jogadores[x]["jogador"] == "exigente" and self.propriedades[self.board[self.jogadores[x]["posicao"]]]["vendido"] == 0 and self.jogadores[x]["saldo"] >= self.propriedades[self.board[self.jogadores[x]["posicao"]]]["venda"][0] and self.propriedades[self.board[self.jogadores[x]["posicao"]]]["venda"][0] > 50:
                    self.jogadores[x]["saldo"] = self.jogadores[x]["saldo"] - self.propriedades[self.board[self.jogadores[x]["posicao"]]]["venda"][0]
                    self.propriedades[self.board[self.jogadores[x]["posicao"]]]["vendido"] = 1
                    self.propriedades[self.board[self.jogadores[x]["posicao"]]]["proprietario"] = self.jogadores[x]["jogador"]

                    print(f"O jogador {str(self.jogadores[x]['jogador']).upper()} parou na propriedade: ", self.propriedades[self.board[self.jogadores[x]["posicao"]]]["propriedade"])
                    print(f"O jogador {str(self.jogadores[x]['jogador']).upper()} comprou a propriedade:", self.propriedades[self.board[self.jogadores[x]["posicao"]]]["propriedade"], "pelo valor de:",self.propriedades[self.board[self.jogadores[x]["posicao"]]]["venda"][0], "e o seu saldo agora é de:", self.jogadores[x]["saldo"])

               ## jogador cauteloso
               elif self.jogadores[x]["jogador"] == "cauteloso" and self.propriedades[self.board[self.jogadores[x]["posicao"]]]["vendido"] == 0 and self.jogadores[x]["saldo"] - self.propriedades[self.board[self.jogadores[x]["posicao"]]]["venda"][0] > 80:
                    self.jogadores[x]["saldo"] = self.jogadores[x]["saldo"] - self.propriedades[self.board[self.jogadores[x]["posicao"]]]["venda"][0]
                    self.propriedades[self.board[self.jogadores[x]["posicao"]]]["vendido"] = 1
                    self.propriedades[self.board[self.jogadores[x]["posicao"]]]["proprietario"] = self.jogadores[x]["jogador"]

                    print(f"O jogador {str(self.jogadores[x]['jogador']).upper()} parou na propriedade: ", self.propriedades[self.board[self.jogadores[x]["posicao"]]]["propriedade"])
                    print(f"O jogador {str(self.jogadores[x]['jogador']).upper()} comprou a propriedade:", self.propriedades[self.board[self.jogadores[x]["posicao"]]]["propriedade"], "pelo valor de:",self.propriedades[self.board[self.jogadores[x]["posicao"]]]["venda"][0], "e o seu saldo agora é de:", self.jogadores[x]["saldo"])

               ## jogador aleatorio
               elif self.jogadores[x]["jogador"] == "aleatorio" and self.propriedades[self.board[self.jogadores[x]["posicao"]]]["vendido"] == 0 and self.jogadores[x]["saldo"] >= self.propriedades[self.board[self.jogadores[x]["posicao"]]]["venda"][0] and random.sample(["compra", "nao compra"], k=1)[0] == "compra":
                    self.jogadores[x]["saldo"] = self.jogadores[x]["saldo"] - self.propriedades[self.board[self.jogadores[x]["posicao"]]]["venda"][0]
                    self.propriedades[self.board[self.jogadores[x]["posicao"]]]["vendido"] = 1
                    self.propriedades[self.board[self.jogadores[x]["posicao"]]]["proprietario"] = self.jogadores[x]["jogador"]

                    print(f"O jogador {str(self.jogadores[x]['jogador']).upper()} parou na propriedade: ", self.propriedades[self.board[self.jogadores[x]["posicao"]]]["propriedade"])
                    print(f"O jogador {str(self.jogadores[x]['jogador']).upper()} comprou a propriedade:", self.propriedades[self.board[self.jogadores[x]["posicao"]]]["propriedade"], "pelo valor de:",self.propriedades[self.board[self.jogadores[x]["posicao"]]]["venda"][0], "e o seu saldo agora é de:", self.jogadores[x]["saldo"])

               else:
                   None

           if partidas == 300:
               fim = time.time()
               turno_medio = turnos / partidas
               print("\n ############### ESTATÍSTICAS DO JOGO ###############")
               #print(f"O VENCEDOR JOGO: {str(self.jogadores[x]['jogador']).upper()}")
               print(f"TOTAL DE JOGOS: {partidas}")
               print(f"O TEMPO TOTAL DE TODAS PARTIDAS FOI DE: {fim - inicio}")
               print(f"MÉDIAS DE TURNOS POR PARTIDA: {turno_medio} ", "\n")
               print(f"PARTIDAS QUE TERMINAM POR TIME-OUT: {turnos_stop}")
               #print(f"Os vencedores foi: ", "\n", vencedores, "\n")
               print("CLASSIFICACOES \n")

               total_impulsivo = vencedores.count("impulsivo")
               total_exigente = vencedores.count("exigente")
               total_cauteloso = vencedores.count("cauteloso")
               total_aleatorio = vencedores.count("aleatorio")  

               print(f"Total de partidas vencidas por jogadores")
               print(f"Impulsivo: Qnt: {total_impulsivo} | Pct: {(total_impulsivo / 300) * 100}%")
               print(f"exigente: Qnt: {total_exigente} | Pct: {(total_exigente / 300) * 100}%")
               print(f"cauteloso: Qnt: {total_cauteloso} | Pct: {(total_cauteloso / 300) * 100}%")
               print(f"aleatorio: Qnt: {total_aleatorio} | Pct: {(total_aleatorio / 300) * 100}%")
               print("\n")

               valor_total = [total_impulsivo, total_exigente, total_cauteloso, total_aleatorio]

               totais = {"impulsivo": total_impulsivo,
                         "exigente":  total_exigente,
                         "cauteloso": total_cauteloso,
                         "aleatorio": total_aleatorio}

               for x in totais:
                   if totais[x] == max(valor_total):
                       print(f"O COMPORTAMENTO QUE MAIS VENCE É: {x} | total de: {max(valor_total)} partidas")

               break
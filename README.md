# Chess.com Rating Evolution Tracker

Script simples em Python para gerar um gráfico de evolução de rating no Chess.com baseado no **número total de partidas jogadas**, em vez das datas do calendário.

## Motivação

O gráfico original da plataforma utiliza a linha do tempo (datas). Quando o jogador passa meses sem jogar, a visualização da evolução fica distorcida por causa dos longos intervalos em branco. 

Ao mudar o eixo X para a **quantidade sequencial de partidas**, fica mais fácil identificar:
* A evolução real por volume de jogo e experiência.
* Platôs de aprendizado e quedas bruscas (*tilt*).
* O progresso contínuo sem a interferência de períodos de pausa.

## Pré-requisitos

Instale as dependências com o pip:

```bash
pip install requests pandas matplotlib

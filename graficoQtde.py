#username = "pedro0250631"
import requests
import pandas as pd
import matplotlib.pyplot as plt

username = "pedro0250631"
headers = {"User-Agent": "MeuGraficoChess/1.0 (contato: seu_email@example.com)"}

# 1. Buscar a lista de TODOS os meses gravados no histórico do jogador
archives_url = f"https://api.chess.com/pub/player/{username}/games/archives"
response = requests.get(archives_url, headers=headers).json()
archives = response.get("archives", [])

games_data = []

print(f"Total de meses encontrados: {len(archives)}")

# 2. Iterar por todos os meses para coletar as partidas
for index, archive in enumerate(archives, 1):
    print(f"Processando mês {index}/{len(archives)}...")
    
    res = requests.get(archive, headers=headers).json()
    for game in res.get("games", []):
        # Filtre por modalidade: 'blitz', 'rapid', 'bullet', etc.
        if game.get("time_class") == "bullet":
            is_white = game["white"]["username"].lower() == username.lower()
            player_info = game["white"] if is_white else game["black"]
            
            games_data.append({
                "end_time": game["end_time"],  # Guardado para ordenar cronologicamente
                "rating": player_info["rating"]
            })

# 3. Processar os dados e plotar
if games_data:
    # Ordena as partidas do início da conta até a mais recente
    df = pd.DataFrame(games_data).sort_values("end_time").reset_index(drop=True)

    # Cria a coluna com a contagem ordinal de partidas (1, 2, 3, ...)
    df["partida_num"] = range(1, len(df) + 1)

    plt.figure(figsize=(12, 6))
    
    # Plota Numero da Partida (X) vs Rating (Y)
    plt.plot(df["partida_num"], df["rating"], color="#7fa650", linewidth=1)
    
    plt.title(f"Evolução de Rating por Partidas (Blitz) - {username}")
    plt.xlabel("Quantidade de Partidas Jogadas")
    plt.ylabel("Rating")
    plt.grid(True, linestyle="--", alpha=0.5)
    
    plt.tight_layout()
    plt.show()
else:
    print("Nenhuma partida encontrada para a modalidade selecionada.")
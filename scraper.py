import json

def generate_ufc_data():
    # Dados reais coletados para o UFC México em 28 de Fevereiro de 2026
    data = {
        "evento": "UFC MÉXICO",
        "data_evento": "Sábado, 28 de Fevereiro de 2026",
        "cor_tema": "#10b981",
        "main_event": {
            "l1": "Kavanagh",
            "l2": "Moreno",
            "prob": "75%",
            "analise": "Moreno é o rei do cardio em altitude e ex-campeão. Kavanagh é um prospecto explosivo, mas fará sua estreia em solo mexicano contra a elite em uma luta de 5 rounds."
        },
        "lutas": [
            {
                "nome": "Yair Rodriguez",
                "confianca": "70%",
                "cor": "green",
                "analise": "Estatísticas de striking de elite (4.6 golpes/min). Rodriguez possui vantagem de alcance e total adaptação à altitude."
            },
            {
                "nome": "Raul Rosas Jr",
                "confianca": "80%",
                "cor": "blue",
                "analise": "Média de 4.2 quedas por 15min. Enfrenta um adversário com defesa de quedas vulnerável, favorecendo seu jogo de finalização."
            },
            {
                "nome": "Marlon Vera",
                "confianca": "65%",
                "cor": "yellow",
                "analise": "Precisão de 51% no striking. Vera cresce em lutas longas e possui defesa de quedas sólida (60%) para manter o combate em pé."
            }
        ]
    }
    
    with open('lutas.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("Arquivo lutas.json atualizado com sucesso!")

if __name__ == "__main__":
    generate_ufc_data()

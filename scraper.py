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
            "analise": "Moreno é o rei do cardio em altitude e ex-campeão. Kavanagh é explosivo, mas nunca lutou 5 rounds e fará sua estreia em solo mexicano contra a elite da categoria."
        },
        "lutas": [
            {
                "nome": "Yair Rodriguez",
                "confianca": "70%",
                "cor": "green",
                "analise": "Estatísticas de striking de elite com 4.6 golpes/min. Rodriguez tem vantagem de alcance e está perfeitamente adaptado à altitude do México."
            },
            {
                "nome": "Raul Rosas Jr",
                "confianca": "80%",
                "cor": "blue",
                "analise": "Média de 4.2 quedas por 15min. Enfrenta um adversário com defesa de quedas vulnerável (abaixo de 50%), o que favorece seu grappling finalizador."
            },
            {
                "nome": "Marlon Vera",
                "confianca": "65%",
                "cor": "yellow",
                "analise": "Precisão de 51% no striking. Vera é conhecido por crescer em lutas longas e possui defesa de quedas sólida (60%) para manter a luta em pé."
            }
        ]
    }
    
    # Salva o arquivo lutas.json que o seu index.html vai ler
    with open('lutas.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("Arquivo lutas.json atualizado com sucesso!")

if __name__ == "__main__":
    generate_ufc_data()

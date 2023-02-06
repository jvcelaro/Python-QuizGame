questions = {
    "Quem é o maior campeão do campeonato brasileiro? ": "C",
    "Quem é o maior vencedor da Europa league? ": "B",
    "Quem é o maior artilherio da seleção brasileiro de todos os tempos? ": "D",
    "Quando foi a primeira copa do mundo? ": "E",
    "Quantas Copas a seleção brasileira ja participou? ": "C",
    "Quantas champions tem o Real Madrid? ": "B",
    "Qual jogador Ganhou a bola de ouro em 2014? ": "A",
    "Quem é o maior artilheiro da champions?": "E",
    "Quais times brasileiros tem mundial? ": "C",
    "Qual o jogador mais bem pago do mundo em 2022?": "A"
}

options = [["A. Santos", "B. Corinthians", "C. Palmeiras", "D. São Paulo", "E. Flamengo"],
           ["A. Inter de Milão", "B. Sevilla", "C. Juventus",
               "D. Atlético de Madrid", "E. Liverpool "],
           ["A. Neymar", "B. Fenêmeno", "C. Kaká",
               "D. Pelé", "E. Ronaldinho Gaúcho"],
           ["A. 1934", "B. 1936", "C. 1932", "D. 1940", "E. 1930"],
           ["A. 18", "B. 19", "C. 20", "D. 21", "E. 22"],
           ["A. 13", "B. 14", "C. 12", "D. 15", "E. 11"],
           ["A. Cristiano Ronaldo", "B. Lionel Messi",
               "C. Manuel Neuer", "D. Karim Benzema", "E. Eden Hazard"],
           ["A. Robert Lewandowski", "B. Lionel Messi", "C. Karim Benzema",
               "D. Thomas Müller", "E. Cristino Ronaldo"],
           ["A. São Paulo, Corinthians, Santos, Flamengo, Grêmio", "B. São Paulo, Corinthians, Santos, Flamengo, Internacional", "C. São Paulo, Corinthians, Santos, Flamengo, Internacional e Grêmio",
               "D. São Paulo, Corinthians, Flamengo, Internacional e Grêmio", "E. São Paulo, Corinthians, Santos, Fluminense Internacional e Grêmio"],
           ["A. Kylian Mbappé", "B. Lionel Messi", "C. Cristinao Ronaldo", "D. Neymar", "E. Karim Benzema"]]

explanation = [["O Palmeiras conquistou o Campeonato Brasileiro pela 11ª vez, se isolando ainda mais como o maior campeão do torneio. Após 35 rodadas, a equipe de Abel Ferreira não pode mais ser alcançada."],
               ["Maior vencedor do torneio, o Sevilla acumula 6 títulos da competição, nos respectivos anos de 2005–06, 2006–07, 2013–14, 2014–15, 2015–16 e 2019–20."],
               ["Na lista dos maiores goleadores com a camisa do Brasil há o Rei Pelé em primeiro lugar. O lendário jogador do Santos conquistou três dos cinco títulos mundiais do Brasil (em 1958, 1962 e na histórica Copa de 1970). Ele é o goleador máximo do país com 77 gols anotados em partidas oficiais."],
               ["Copa do Mundo FIFA de 1930 foi a primeira edição deste evento esportivo, que passou a ser organizado quadrienalmente pela Federação Internacional de Futebol. A competição foi disputada no Uruguai, entre 13 a 30 de julho"],
               ["São cinco títulos mundiais (1958, 1962, 1970, 1994 e 2002), dois vice-campeonatos (1950 e 1998), dois terceiros lugares (1938 e 1978) e dois quartos lugares (1974 e 2014) em um total de 20 participações."],
               ["O clube com mais títulos na Champions League é o Real Madrid, que ganhou a competição 14 vezes."],
               ["A Gala da Bola de Ouro efetuada em Zurique, coroou de novo Cristiano Ronaldo como melhor jogador do mundo. O madridista mais uma vez teve reconhecimento pelo seu fantástico futebol em 2014, no qual marcou 61 golos (56 com o conjunto merengue) e conquistou a Champions, Mundial de Clubes, Supertaça da Europa e Taça do Rei."],
               ["Cristiano Ronaldo, o maior artilheiro da história da Liga dos Campeões e recordista 7 vezes melhor marcador da competição."],
               ["São Paulo, Corinthians, Santos, Flamengo, Internacional e Grêmio possuem, juntos, dez taças conquistadas em três formatos diferentes do torneio."],
               ["Kylian Mbappé Com 23 anos e jogando no Paris Saint-Germain, o francês Kylian Mbappé é hoje o jogador mais bem pago do futebol mundial com um ganho estimado de US$ 128 milhões entre salário e bônus na temporada de 2022-2023, segundo ranking da Forbes."]
               ]


def new_game():

    points = 0
    question_numb = 1

    for key in questions:

        print("-------------------------")
        print(key)

        for i in options[question_numb-1]:
            print(i)

        userchoice = input("Enter (A, B, C, D ou E): ").upper()
        answer = questions.get(key)
        points += check_answer(answer, userchoice)

        if answer != userchoice:

            print("ERRADO!")
            for x in explanation[question_numb-1]:
                print(x)

        question_numb += 1

    display_score(points)

# -------------------------


def check_answer(answer, userchoice):

    if answer == userchoice:
        print("CORRETO!")
        return 1
    else:
        return 0

# -------------------------


def display_score(points):
    print("-------------------------")
    print("RESULTADO")
    print("-------------------------")

    result = points * 10
    print("Your score is:", result, "%")

# -------------------------


def play_again():

    playagain = input("Do you want to play again? (yes or no): ").upper()

    if playagain == "YES":
        new_game()
    else:
        return False

# -------------------------


new_game()

play_again()


print("Obrigado!")

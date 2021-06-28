from survey import AnonymousSurvey

""" Define uma pergunta e cria a pesquisa. """
question = "Qual idioma você fala além do português? "
my_survey = AnonymousSurvey(question)

""" Mostra a pergunta e armazena as respostas. """
my_survey.show_question()
print("Digite 'q' para sair ")
print('-----------------------------------------')
while True:
    response = input("Idioma: ")
    if response == 'q':
        break
    my_survey.store_response(response)

""" Exibe resultado da pesquisa. """
print('-----------------------------------------')
print("Obrigado por participar da pesquisa. ")
print('-----------------------------------------')
my_survey.show_results()

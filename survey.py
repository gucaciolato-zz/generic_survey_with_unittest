class AnonymousSurvey():
    """ Coleta respostas anônimas para uma pesquisa. """

    def __init__(self, question):
        """ Armazena pergunta e prepara para armazenar respostas. """

        self.question = question
        self.responses = []

    def show_question(self):
        """ Mostra a pergunta da pesquisa. """

        print(self.question)

    def store_response(self, new_response):
        """ Armazena uma única resposta da pequisa. """

        self.responses.append(new_response)

    def show_results(self):
        """ Mostra todas as respostas dadas. """

        print("Respostas da pesquisa: ")
        for response in self.responses:
            print("- " + response)
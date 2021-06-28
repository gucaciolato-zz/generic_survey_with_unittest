import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """ Teste para a classe AnonymousSurvey """

    def test_store_single_response(self):
        """ Testa se uma única resposta é armazanada de forma apropriada. """

        question = "Qual idioma você fala? "
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('Inglês')

        self.assertIn('Inglês', my_survey.responses)


unittest.main()

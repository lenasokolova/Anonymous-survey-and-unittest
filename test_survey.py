import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Testy dla klasy AnonymousSurvey"""

    def test_store_single_response(self):
        """Sprawdzanie, czy pojedyncza odpowiedź jest prawidłowo przechowywana."""
        question = "What is your native language?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('english')

        self.assertIn('english', my_survey.responses)

    def test_store_three_responses(self):
        """Sprawdzenie, czy trzy pojedyncze odpowiedzi są prawidłowo przechowywane."""
        question = "What is your native language?"
        my_survey = AnonymousSurvey(question)
        responses = ['englsh', 'spanish', 'polish']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)


if __name__ == '__main__':
    unittest.main()
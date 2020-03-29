class AnonymousSurvey():
    """Przechowuje anonimowe odpowiedzi na pytania w ankiecie."""

    def __init__(self,question):
        """Przechowuje pytania i przygotowuje do przechowywania odpowiedzi."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Wyświetla pytania z ankiety."""
        print(self.question)

    def store_response(self, new_response):
        """Przechowuje pojedynczą odpowiedź na pytania z ankiety."""
        self.responses.append(new_response)

    def show_results(self):
        """Wyświetla wszystkie udzielone odpowiedzi."""
        print("Oto wyniki ankiety:")
        for response in self.responses:
            print('- ', response)



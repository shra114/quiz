#contains necessary classes and functions required for the app.
class InputQuestion:
    def __init__(self):

    def take_inputs(self):
        print ("Enter the Question")
        self.question = input()
        self.options = []
        self.answer_option = 1
        iterator = 0
        while(1):
            print ("Enter option",iterator+1)
            self.options.append(input())
            print("Are the options done?")
            iterator+=1
            if(input()=="yes"):
                break
        self.get_answer()

    def show_question(self):
        print ("Question:", self.question)

    def show_options(self):
        for i in range(len(self.options)):
            print ("Option"+str(i+1),self.options[i])

    def get_answer(self):
        self.show_question()
        self.show_options()
        print ("Which option is right?")
        self.answer_option = int(input())

    def run_quiz(self):
        self.show_question()
        self.show_options()
        print ("Which option is right?")
        answer_option = int(input())
        return (answer_option==self.answer_option)



name_question  = InputQuestion()
place_question  = InputQuestion()
name_question.take_inputs()
place_question.take_inputs()

name_question.run_quiz()
place_question.run_quiz()

class Quiz:
    def __init__(self):
        print("Hi")

    def create_quiz(self, config_yml):
        return  None

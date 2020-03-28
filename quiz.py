from functions import *
from random import randrange

def get_str_bw_here(str_in, start, end):
    str1 = get_str_bw(str_in, start, end)[0]
    str1 = remove_things_from_str(str1, [start, end])
    return str1


#contains necessary classes and functions required for the app.
class Question:
    def __init__(self):
        self.question = ""
        self.options = []
        self.answer_option = 1

    def take_inputs(self):
        print ("Enter the Question")
        self.question = input()
        iterator = 0
        while(1):
            print ("Enter option",iterator+1)
            self.options.append(input())
            print("Are the options done?")
            iterator+=1
            if(input()=="yes"):
                break
        self.get_answer()

    def read_from_file(self,file_path):
        str_in = parse_file_as_str(file_path)
        self.question = get_str_bw_here(str_in,"Question: " , "Total options: ")
        total_options = int(get_str_bw_here(str_in,"Total options: ","\n").strip())
        for i in range()
        return None


    def write_to_file(self,dir_path):
        dir_path = dir_path.strip()
        cmd_call("mkdir -p "+dir_path)
        cmd_call("touch "+dir_path+"/0.txt")
        ls_out=get_lsout(dir_path)
        ls_out.sort()
        next_file = str(int(ls_out[-1].replace(".txt",""))+1)+".txt"
        str_out = "Question: "+self.question+"\n"
        str_out+="Total options: "+str(len(self.options))+"\n"
        for i in range(len(self.options)):
            str_out += "Option"+str(i+1)+": "+self.options[i]+"\n"
        str_out+="Answer option: "+str(self.answer_option)+"\n"
        write_str_to_file_with_mode(str_out, dir_path+"/"+next_file , "w", print_log=True)

        return  None

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
        print ("\n")

    def run_quiz(self):
        print("\n\n----Running quiz----\n\n")
        self.show_question()
        self.show_options()
        print ("Which option is right?")
        answer_option = int(input())
        return (answer_option==self.answer_option)



name_question  = Question()
place_question  = Question()
#name_question.take_inputs()
#name_question.write_to_file("personal")

#place_question.take_inputs()
#place_question.write_to_file("personal")


class Quiz:
    def __init__(self):
        print("Hi")

    def create_questions(self, dir_path):
        return  None

    def run_quiz(self,dir_path):
        ls_out=get_lsout(dir_path)
        ls_out.sort()
        if("0.txt" in ls_out):
            ls_out.remove("0.txt")
        print ("Total question in the directory :", len(ls_out))
        points = 0
        num = int(input("How many question to ask?"))
        if(num > len(ls_out)):
            num = len(ls_out)

        random= num<len(ls_out)
        while(num!=0):
            num=num-1
            if(random):
                question = ls_out[ randrange(len(ls_out))]
            else:
                question = ls_out[0]
            ls_out.remove(question)
            question_obj = Question()
            question_obj.read_from_file(dir_path+"/"+question)
            points += int(question_obj.run_quiz())
        print("Points = ",points)
        return points







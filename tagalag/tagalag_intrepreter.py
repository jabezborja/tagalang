import os


ERRORS = [
    'Hindi ko alam yung Sintax mo pre. Baka namalikmata kalang?',
    'Wala naman yatang ganyang baryabol?'
]

class Interpreter:
    def __init__(self, program_file):
        self.program_file = program_file
        self.programlines = None
        self.is_code_running = True
        self.base_dir = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__)))
        self.baryabol_shortmemory = ""
        self.baryabolcontent_shortmemory = ""
        self.baryabols = {}
        self.line_count = 0

    def interpret(self):
        os.system('color 7')
        with open('../%s' % self.program_file) as program:
            for line in program.readlines():
                self.line_count += 1

                self.programlines = program.readlines
                if self.is_code_running:
                    self.check(line)

    def check(self, line):
        ## PRINTS ##
        if 'iPrint' in line:
            if line[-2] == "'":
                to_be_print = line[14:-1]

                # Remove " ' " Suffix (Error)
                if "'" in to_be_print:
                    to_be_print = to_be_print.replace("'", "")
                print(to_be_print)

            else:
                curr_baryabol = line[13:]
                if self.baryabols:
                    if '\n' in curr_baryabol:
                        curr_baryabol = curr_baryabol.replace("\n", "")
                    if curr_baryabol in self.baryabols:
                        baryabol_found = self.baryabols[curr_baryabol]

                        # Remove " ' " Prefix (Error)
                        if "'" in baryabol_found:
                            baryabol_found = baryabol_found.replace("'", "")

                        print(baryabol_found)
                    else:
                        self.raiseError(
                            "Wala naman yatang ganyang baryabol '%s'?" % curr_baryabol)
                else:
                    self.raiseError(
                        "Wala naman yatang ganyang baryabol '%s'?" % curr_baryabol)

        ## FOR GETTING THE BARYABOL ##
        elif 'baryabol' in line:
            baryabol_word_count = 0
            run_count = 0
            substring_count = 1
            line_arr = list(line)

            activate_baryabol_collector = False
            activate_baryabolcontent_collector = False
            activate_baryabol_collector_input = False
            collecting_baryabol_name = False
            collecting_baryabol_content = False

            for word in line_arr:

                ## GETTING THE BARYABOL NAME ##
                if run_count == 0:
                    collecting_baryabol_name = True

                if collecting_baryabol_name:
                    if word == ">":
                        activate_baryabol_collector = True

                    if activate_baryabol_collector:
                        if not line_arr[baryabol_word_count-1] == ">":
                            self.baryabol_shortmemory += line_arr[baryabol_word_count]
                        else:
                            self.baryabol_shortmemory += line_arr[baryabol_word_count]
                        if line_arr[baryabol_word_count+1] == "=":
                            collecting_baryabol_name = False

                ## GETTING THE BARYABOL VALUE ##
                if run_count == 0:
                    collecting_baryabol_content = True

                if collecting_baryabol_content:

                    ## CHECKING IF IT'S A STRING ##
                    if word == "(":
                        activate_baryabol_collector_input = True
                    ## CHECKING IF IT'S AN INPUT ##
                    elif word == "'":
                        activate_baryabolcontent_collector = True

                    ## IF IT'S A STRING ##
                    if activate_baryabolcontent_collector:
                        if not line_arr[baryabol_word_count-1] == "'":
                            self.baryabolcontent_shortmemory += line_arr[baryabol_word_count]
                        else:
                            self.baryabolcontent_shortmemory += line_arr[baryabol_word_count]
                        if line_arr[baryabol_word_count+1] == "'":
                            collecting_baryabol_content = False

                    ## IF IT'S AN INPUT ##
                    if activate_baryabol_collector_input:
                        for i in line_arr:
                            substring_count += 1
                            if i == "'":
                                break

                        if line[substring_count:-2] == "'" or "\"":
                            to_be_input = line[substring_count-1:-3]
                        elif line[substring_count:-3] == "'" or "\"":
                            to_be_input = line[substring_count-1:-3]
                        self.baryabolcontent_shortmemory = input(to_be_input)
                        activate_baryabol_collector_input = False
                        collecting_baryabol_content = False

                run_count += 1
                baryabol_word_count += 1

            ## FOR REMOVING THE '>' PREFIX IN BARYABOLS ##
            if '>' in self.baryabol_shortmemory:
                listed_baryabol = list(self.baryabol_shortmemory)
                listed_baryabol.pop(0)

            listed_baryabolcontent = list(self.baryabolcontent_shortmemory)

            self.baryabol_shortmemory = ''
            self.baryabolcontent_shortmemory = ''

            ## Storing the Baryabol Name ##
            for bar in listed_baryabol:
                self.baryabol_shortmemory += bar

            ## Storing the Baryabol Value ##
            for con in listed_baryabolcontent:
                self.baryabolcontent_shortmemory += con

            self.saveBaryabols()

        ## 'KUNG' statements ##
        elif 'kung' in line:
            is_true = False
            get_condition_content = False
            condition_content = ''
            start_expression = False
            is_baryabol = False
            condition = ''
            expression = ''
            getting_first_ex = False
            getting_second_ex = False
            first_ex = ''
            second_ex = ''
            method = None

            ## GET EXPRESSION ##
            for word in line:
                if word == "(":
                    start_expression = True

                if start_expression:
                    condition += word

                    if word == ")":
                        start_expression = False

                if word == "{":
                    get_condition_content = True

                    ## Getting the Embedded code in the 'Kung Statement' ##
                    if is_true and get_condition_content:
                        pass

            if condition in self.baryabols:
                is_baryabol = True

            ## FOR HANDLING NONE BARYABOLS ##
            if not is_baryabol:
                run_count = 0
                for ex in condition:
                    if getting_first_ex:
                        first_ex += ex
                    if getting_second_ex:
                        second_ex += ex

                        ## REMOVE PREFIXES ##
                        if ")" in second_ex:
                            second_ex = second_ex.replace(")", "")
                        if " " in second_ex:
                            second_ex = second_ex.replace(" ", "")
                            
                    if ex == " ":
                        getting_first_ex = False
                    if ex == ")":
                        getting_second_ex = False
                    else:
                        if run_count == 0:
                            getting_first_ex = True
                        elif run_count == 5:
                            getting_second_ex = True

                    run_count += 1

                try:
                    int(first_ex) + int(second_ex)
                    method = "int"
                except:
                    first_ex + second_ex
                    method = "str"

            ## FOR HANDLING BARYABOLS ##
            else:
                pass

            ## Handling Expressions ##
            if "==" in condition:
                if method == "int":
                    ## If the condition is finding the diff of integers ##
                    if int(first_ex) == int(second_ex):
                        is_true = True
                elif method == "str":

                    if first_ex == second_ex:
                        is_true = True

        ## IGNORE SPACES ##
        elif '\n' in line:
            pass

        ## COMMENTS ##
        elif '!?' in line:
            pass

        elif 'os' in line:
            pass

        ## UNKNOWN SYNTAX ##
        else:
            self.raiseError(
                "Hindi ko alam yang sintax mo pre! Baka namalikmata kalang!?")

    ## SAVE 'BARYABOLS' INTO A MEMORY ##
    def saveBaryabols(self):
        self.baryabols[self.baryabol_shortmemory] = self.baryabolcontent_shortmemory

        self.baryabol_shortmemory = ''
        self.baryabolcontent_shortmemory = ''

    def raiseError(self, error):
        os.system('color 4')
        print("\nMerong Error: %s" % error)
        print(">>> sa %s" % self.program_file)
        print(">>> banda sa LINE: %s" % self.line_count)
        quit()

print("Info: What is the name of the .tag program. Make sure that the Program is sitting in the main\ntagalag file location and make sure that there is .tag extension\n")
c = Interpreter(input(".tag extension to open: "))
os.system("cls")
c.interpret()
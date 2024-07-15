# Anhuelen - Take In
# Version 1.0
# Anhuelen is an input managment module. Use it to prompt users 
# neatly for input and handle returned results

class Anhuelen:
    RESET     = '\033[0m'

    # Colors ('Bright' variants for readability)
    RED       = '\033[91m' 
    GREEN     = '\033[92m'
    YELLOW    = '\033[93m'
    BLUE      = '\033[94m'
    MAGENTA   = '\033[95m'
    CYAN      = '\033[96m'
    
    # Statuses
    ALERT     = '\033[31m'
    WARNING   = '\033[33m'
    GRAYOUT   = '\033[37m'
    
    # Indicators
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'

    # Cursor movement
    CURSUP    = "\033[A"
    CURSDOWN  = '\033[B'
    CURSNEXT  = '\033[C'
    CURSBACK  = '\033[D'

    header = ''

    def __init__(self, header='underline'):
        header = header.lower()
        if header == 'underline':
            self.header = self.UNDERLINE
        elif header == 'bold':
            self.header = self.BOLD
        elif header == 'red':
            self.header = self.RED
        elif header == 'green':
            self.header = self.GREEN
        elif header == 'yellow':
            self.header = self.YELLOW
        elif header == 'blue':
            self.header = self.BLUE
        elif header == 'magenta':
            self.header = self.MAGENTA
        elif header == 'cyan':
            self.header = self.CYAN
        else:
            self.header = self.RESET

    # Prints a title or header. change first value to prefered styling to indicate
    def title(self, text):
        print(f"{self.header}{text}{self.RESET}")

    # Takes a question and predetermined answer and displays them
    def inform(self, question, answer='N/A'):
        if answer != 'N/A':
            print(f"{self.RESET}{question}: {self.BLUE}{answer}{self.RESET}")
        else:
            print(f"{self.RESET}{question}: {self.GRAYOUT}{answer}{self.RESET}")

    # Takes a question and default answer, allows user to accept default with [Enter]
    # or to type a new answer. Returns that answer either way
    def prompt(self, question, answer=''):
        print(f"{self.RESET}{question}: {self.GRAYOUT}{answer}{self.RESET}", end='\b'*len(str(answer)))
        new_answer = input(f"{self.GREEN}")

        if new_answer == '' and answer != '':
            print(f"{self.CURSUP}", end='')
            print(f"{self.CURSNEXT}"*(len(question) + 2), end='')
            print(f"{answer}{self.RESET}")
            return answer

        erase_extra = len(answer) - len(new_answer)
        if erase_extra > 0:
            print(f"{self.CURSUP}", end='')
            print(f"{self.CURSNEXT}"*(len(question) + 2 + len(new_answer)), end='')
            print(" "*erase_extra)

        return new_answer
import model_NY as model
import model_before_NY as before
import view

value = None

def callMainMenu():
    view.printMainMenu()

def callNewYearModel():
    days = model.new_year_time()
    view.printResult(days, 'дней осталось до Нового Года')

def callBeforeNY():
    days = before.before_NY()
    view.printResult(days, 'дней прошло в этом году')

def initValues():
    global value
    value = view.getValues()

def buttonClick():
    global value
    if value == '1':
        callNewYearModel()
    elif value == '2':
        callBeforeNY()
    else:
        view.errorMessage()
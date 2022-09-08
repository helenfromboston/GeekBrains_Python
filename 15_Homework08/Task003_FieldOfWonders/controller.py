import module00 as q
import module01 as n
import module02 as a
import module03 as g
import view

value = None

def call_menu():
    view.print_menu(n.q_num())

def init_value():
    global value
    value = view.get_value()

def q_choice():
    global value
    value = int(value)
    if value in range(1, 2 + 1):
        view.q_print(q.q_extract(value))
    else:
        view.error_message()
        init_value()
        q_choice()

def q_guess():
    global value
    answer = a.answer(value)
    hidden = view.hidden_a(answer, '*')
    view.hidden_a_print(hidden)
    while hidden != answer:
        init_value()
        hidden = g.g_check(value, answer, hidden)
        view.hidden_a_print(hidden)
    view.winner_print()
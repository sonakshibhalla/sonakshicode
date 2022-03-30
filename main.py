import numbers
import factorial
import fibonacci
import infodb
import tennis
import tree
import facclass
import factorsimp
import factorsclass
import palindrome


border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"

patterns_menu = [
    ["Tree", tree.pattern],
    ["Tennis Animation", tennis.tennis],
    
]


numbers_menu = [
    ["Number Pad", numbers.numpad],
    ["Number Swap", numbers.numswap],
    ["Info", infodb.information],
        
]

functions_menu = [
    ["Factorial Class", facclass.facclass],
    ["Factors Imperative", factorsimp.factorsimp],
    ["Factors Class", factorsclass.factorsclass],
    ["Palindrome", palindrome.palindrome],
    ["Factorial", factorial.factorial],
    ["Fibonacci", fibonacci.fibonacci]
    
]


def menu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    except TypeError:
        print(f"Not callable {action}")
    # end validation try

    menu(banner, options)  # recursion, start menu over again



def _patterns_menu():
    title = "Patterns"
    menu(title, patterns_menu)

def _numbers_menu():
    title = "Numbers"
    menu(title, numbers_menu)

def _functions_menu():
    title = "Math Functions"
    menu(title, functions_menu)

def driver():
    title = "Main Menu"
    menu_list = [["Patterns", _patterns_menu],
                 ["Numbers", _numbers_menu],
                 ["Math Functions", _functions_menu]]
    menu(title, menu_list)


if __name__ == "__main__":
    driver()


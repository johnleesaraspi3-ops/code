# ACCOUNT INFORMATION
registered = False
saved_full_name = ""
saved_username = ""
saved_password = ""

# LEARNING PROGRESS
module1_viewed = False
module2_viewed = False
module3_viewed = False
module4_viewed = False
module5_viewed = False
module6_viewed = False
module7_viewed = False
module8_viewed = False

module1_completed = False
module2_completed = False
module3_completed = False
module4_completed = False
module5_completed = False
module6_completed = False
module7_completed = False
module8_completed = False

module1_score = 0
module2_score = 0
module3_score = 0
module4_score = 0
module5_score = 0
module6_score = 0
module7_score = 0
module8_score = 0

module1_attempts = 0
module2_attempts = 0
module3_attempts = 0
module4_attempts = 0
module5_attempts = 0
module6_attempts = 0
module7_attempts = 0
module8_attempts = 0


# MAIN PORTAL
while True:
    print("\n============================================================")
    print("             PROGRAMMING LEARNING PORTAL")
    print("============================================================")
    print("Learn Python step by step")
    print("\n1. Log In")
    print("2. Register")
    print("3. Exit")

    main_choice = input("\nSelect an option: ")

    while main_choice != "1" and main_choice != "2" and main_choice != "3":
        print("Invalid choice. Please try again.")
        main_choice = input("Select an option: ")

    #REGISTER
    if main_choice == "2":
        print("\n======================= REGISTER =========================")

        full_name = input("Full Name: ")
        username = input("Username: ")
        password = input("Password: ")
        confirm_password = input("Confirm Password: ")

        if full_name == "" or username == "" or password == "" or confirm_password == "":
            print("\nAll fields are required.")
        elif registered == True:
            print("\nAn account is already registered for this session.")
        elif password != confirm_password:
            print("\nPasswords do not match. Please register again.")
        else:
            saved_full_name = full_name
            saved_username = username
            saved_password = password
            registered = True
            print("\nRegistration successful!")
            print("You can now log in using your username and password.")

        input("\nPress ENTER to return to the main menu...")

    #LOG IN
    elif main_choice == "1":
        print("\n======================== LOG IN ==========================")

        if registered == False:
            print("No account is registered yet. Please register first.")
            input("\nPress ENTER to return to the main menu...")
        else:
            login_username = input("Username: ")
            login_password = input("Password: ")

            if login_username == saved_username and login_password == saved_password:
                print("\nLogin successful!")
                print(f"Welcome, {saved_full_name}!")

                login_active = True

                #DASHBOARD
                while login_active == True:
                    print("\n============================================================")
                    print("                       DASHBOARD")
                    print("============================================================")
                    print(f"Welcome, {saved_full_name}!")
                    print("\n1. Modules")
                    print("2. My Profile")
                    print("3. View Progress")
                    print("4. Log Out")

                    dashboard_choice = input("\nSelect an option: ")

                    while dashboard_choice != "1" and dashboard_choice != "2" and dashboard_choice != "3" and dashboard_choice != "4":
                        print("Invalid choice. Please try again.")
                        dashboard_choice = input("Select an option: ")

                    #MODULES MENU
                    if dashboard_choice == "1":
                        print("\n==================== LEARNING MODULES ====================")
                        print("1. Introduction to Programming")
                        print("2. Python Basic Syntax")
                        print("3. Variables, Constants, and Data Types")
                        print("4. Arithmetic Operators and Expressions")
                        print("5. Basic Input and Output in Python")
                        print("6. Conditional Statements")
                        print("7. Logical Operators")
                        print("8. Introduction to Iteration and Loops")
                        print("0. Back to Dashboard")

                        module_choice = input("\nSelect a module: ")

                        while module_choice != "0" and module_choice != "1" and module_choice != "2" and module_choice != "3" and module_choice != "4" and module_choice != "5" and module_choice != "6" and module_choice != "7" and module_choice != "8":
                            print("Invalid choice. Please try again.")
                            module_choice = input("Select a module: ")

                        if module_choice == "1":
                            module1_viewed = True
                            print("\n============================================================")
                            print("             MODULE 1: INTRODUCTION TO PROGRAMMING")
                            print("============================================================")
                            print("\n1. What is a Programming Language?")
                            print("A programming language is a special language used to give")
                            print("instructions to a computer so it can perform tasks.")
                            print("The PPT shows examples such as Python, C, C++, and JavaScript.")
                            print("\n2. What is Python Programming?")
                            print("Python is a high-level, interpreted, and general-purpose")
                            print("programming language. It is designed to be simple, readable,")
                            print("and easy to learn.")
                            print("\n3. Why Learn Python?")
                            print("- Simple and easy to learn for beginners.")
                            print("- Readable syntax that looks almost like English.")
                            print("- Versatile and used in many fields.")
                            print("- Has a large community with tutorials, libraries, and support.")
                            print("\n4. What Do You Need to Start Python Programming?")
                            print("- Python")
                            print("- A code editor or development environment")
                            print("Examples shown in the PPT:")
                            print("- PyCharm")
                            print("- Visual Studio Code")
                            print("- Jupyter Notebook / JupyterLab")

                        elif module_choice == "2":
                            module2_viewed = True
                            print("\n============================================================")
                            print("                  MODULE 2: PYTHON BASIC SYNTAX")
                            print("============================================================")
                            print("\n1. What is Python Syntax?")
                            print("Syntax means the set of rules used to write a correct")
                            print("Python program.")
                            print("\n2. Python is Case-Sensitive")
                            print("Uppercase and lowercase letters are different in Python.")
                            print("Example from the PPT:")
                            print('name = "John"')
                            print("print(name)")
                            print("\n3. Indentation")
                            print("Indentation means the spaces at the beginning of a line.")
                            print("Python uses indentation to define blocks of code.")
                            print("Example from the PPT:")
                            print("age = 18")
                            print("if age >= 18:")
                            print('    print("Adult")')
                            print("\n4. Print Statement")
                            print("The print() function displays information on the screen.")
                            print("Syntax: print(value)")
                            print("Example:")
                            print('print("Hello, World!")')
                            print("\n5. Printing Text and Numbers")
                            print("Text is written inside quotation marks.")
                            print("Numbers can be printed without quotation marks.")
                            print("Examples from the PPT:")
                            print('print("Hello, Maria!")')
                            print("print(100)")
                            print("print(25.5)")
                            print('print("100")')
                            print('print("25.5")')
                            print("\n6. Python Comments")
                            print("Comments are ignored by Python and are used to explain code.")
                            print("A single-line comment starts with #.")
                            print("Example:")
                            print("# This is a comment")
                            print('print("Hello")')

                        elif module_choice == "3":
                            module3_viewed = True
                            print("\n============================================================")
                            print("       MODULE 3: VARIABLES, CONSTANTS, AND DATA TYPES")
                            print("============================================================")
                            print("\n1. What is a Variable?")
                            print("A variable is a named storage location used to keep data")
                            print("in a program. Its value can change while the program runs.")
                            print("Examples of variable names shown in the PPT: a, b, c, age, name.")
                            print("\n2. Variable Naming Rules")
                            print("- A variable name can start with a letter or underscore.")
                            print("- It can contain letters, numbers, and underscores.")
                            print("- It cannot start with a number.")
                            print("- It cannot contain spaces or special characters.")
                            print("- Variable names are case-sensitive.")
                            print("\n3. Assigned Value to a Variable")
                            print("The assignment operator (=) gives a value to a variable.")
                            print("Example from the PPT:")
                            print('first_name = "John"')
                            print("\n4. Output Variables")
                            print("The print() function can display the value of a variable.")
                            print("The PPT shows that multiple variables can be separated by a comma.")
                            print("Example from the PPT:")
                            print('school = "Clark College"')
                            print("print(school)")
                            print('a = "I"')
                            print('b = "LOVE"')
                            print('c = "CCST"')
                            print("print(a, b, c)")
                            print("\nThe PPT also shows joining strings using +:")
                            print('x = "I "')
                            print('y = "LOVE "')
                            print('z = "CCST"')
                            print("print(x + y + z)")
                            print("\n5. Basic Data Types")
                            print("- int: whole numbers, such as 10, 25, and 100.")
                            print("- float: numbers with decimal points, such as 12.5 and 3.14.")
                            print("- str: text or characters inside quotation marks.")
                            print("- bool: Boolean values, either True or False.")
                            print("Example from the PPT:")
                            print('name = "Maria"')
                            print("age = 20")
                            print("grade = 89.5")
                            print("is_enrolled = True")
                            print("print(name)")
                            print("print(age)")
                            print("print(grade)")
                            print("print(is_enrolled)")

                        elif module_choice == "4":
                            module4_viewed = True
                            print("\n============================================================")
                            print("       MODULE 4: ARITHMETIC OPERATORS AND EXPRESSIONS")
                            print("============================================================")
                            print("\n1. What are Arithmetic Operators?")
                            print("Arithmetic operators are symbols used to perform")
                            print("mathematical calculations on numbers.")
                            print("\nOperators shown in the PPT:")
                            print("+   Addition")
                            print("-   Subtraction")
                            print("*   Multiplication")
                            print("/   Division")
                            print("//  Floor Division")
                            print("%   Modulus")
                            print("**  Exponentiation")
                            print("\n2. Expressions in Python")
                            print("An expression is a combination of values, variables, and")
                            print("operators that evaluates to a result.")
                            print("Example from the PPT:")
                            print("a = 2")
                            print("b = 3")
                            print("c = 4")
                            print("print(a + b * c)")
                            print("Output: 14")
                            print("\n3. Order of Operations (PEMDAS)")
                            print("P - Parentheses")
                            print("E - Exponents")
                            print("M - Multiplication")
                            print("D - Division")
                            print("A - Addition")
                            print("S - Subtraction")
                            print("Multiplication is completed before addition in the example.")

                        elif module_choice == "5":
                            module5_viewed = True
                            print("\n============================================================")
                            print("        MODULE 5: BASIC INPUT AND OUTPUT IN PYTHON")
                            print("============================================================")
                            print("\n1. Accepting User Input")
                            print("The input() function allows a program to ask the user")
                            print("for information. All input is a string by default.")
                            print("Example from the PPT:")
                            print('name = input("Enter your name: ")')
                            print('age = input("Enter your age: ")')
                            print("\n2. Formatting Output")
                            print("A comma inside print() can display text and variable values.")
                            print("An f-string can place a variable inside a text message.")
                            print("Use :.2f to display a decimal number with exactly two decimal places.")
                            print("Example:")
                            print('print("Name:", name)')
                            print('print("Age:", age)')
                            print('print(f"Your grade is {grade:.2f}")')
                            print("Example output: Your grade is 89.50")
                            print("\n3. Converting Input to Other Data Types")
                            print("The PPT shows int() and float() for converting input.")
                            print("Example from the PPT:")
                            print('grade = float(input("Enter your grade: "))')
                            print('print(f"Your grade is {grade:.2f}")')
                            print("\nThe PPT also shows a Boolean input using a condition:")
                            print('answer = input("Are you a student? (yes/no): ")')
                            print('is_student = answer.lower() == "yes"')
                            print('print("Student status:", is_student)')
                            print("\n4. Combining Input and Output")
                            print("Example from the PPT:")
                            print('name = input("Enter your name: ")')
                            print('age = int(input("Enter your age: "))')
                            print('grade = float(input("Enter your final grade: "))')
                            print('print(f"Student: {name}, Age: {age}, Final Grade: {grade:.2f}")')

                        elif module_choice == "6":
                            module6_viewed = True
                            print("\n============================================================")
                            print("              MODULE 6: CONDITIONAL STATEMENTS")
                            print("============================================================")
                            print("\n1. Introduction to Conditional Statements")
                            print("A conditional statement allows a program to make decisions")
                            print("based on whether a condition is True or False.")
                            print("\n2. Relational Operators")
                            print("==  Equal to")
                            print("!=  Not equal to")
                            print(">   Greater than")
                            print("<   Less than")
                            print(">=  Greater than or equal to")
                            print("<=  Less than or equal to")
                            print("\n3. The if Statement")
                            print("An if statement runs a block of code when a condition is True.")
                            print("Example:")
                            print("age = 18")
                            print("if age >= 18:")
                            print('    print("Adult")')
                            print("\n4. The if-else Statement")
                            print("The else block runs when the if condition is False.")
                            print("Example:")
                            print("age = 16")
                            print("if age >= 18:")
                            print('    print("Adult")')
                            print("else:")
                            print('    print("Minor")')
                            print("\n5. The if-elif-else Statement")
                            print("elif checks another condition when the earlier condition is False.")
                            print("Example:")
                            print("grade = 85")
                            print("if grade >= 90:")
                            print('    print("Excellent")')
                            print("elif grade >= 75:")
                            print('    print("Passed")')
                            print("else:")
                            print('    print("Failed")')
                            print("\n6. Nested Condition")
                            print("A nested condition is an if statement inside another if statement.")
                            print("The PPT uses nested conditions to check more than one decision.")

                        elif module_choice == "7":
                            module7_viewed = True
                            print("\n============================================================")
                            print("                  MODULE 7: LOGICAL OPERATORS")
                            print("============================================================")
                            print("\n1. What are Logical Operators?")
                            print("Logical operators combine conditions and return True or False.")
                            print("The three logical operators in Python are:")
                            print("and - True when all conditions are True.")
                            print("or  - True when at least one condition is True.")
                            print("not - Reverses the result of a condition.")
                            print("\n2. The and Operator")
                            print("Example from the PPT:")
                            print("age = 20")
                            print("has_id = True")
                            print("if age >= 18 and has_id:")
                            print('    print("You are allowed to enter.")')
                            print("else:")
                            print('    print("You are not allowed to enter.")')
                            print("\n3. The or Operator")
                            print("Example from the PPT:")
                            print('day = "Saturday"')
                            print('if day == "Saturday" or day == "Sunday":')
                            print('    print("It\'s the weekend!")')
                            print("else:")
                            print('    print("It\'s a regular school day.")')
                            print("\n4. The not Operator")
                            print("Example from the PPT:")
                            print("is_raining = False")
                            print("if not is_raining:")
                            print('    print("You can go outside.")')
                            print("else:")
                            print('    print("Bring an umbrella.")')
                            print("\n5. Truth Tables")
                            print("AND: True and True is True. Other combinations are False.")
                            print("OR: True when at least one value is True.")
                            print("NOT: True becomes False, and False becomes True.")

                        elif module_choice == "8":
                            module8_viewed = True
                            print("\n============================================================")
                            print("        MODULE 8: INTRODUCTION TO ITERATION AND LOOPS")
                            print("============================================================")
                            print("\n1. Introduction to Iteration")
                            print("Iteration means repeating a set of instructions.")
                            print("Each repetition is called an iteration.")
                            print("Example from the PPT:")
                            print("for number in range(3):")
                            print('    print("Welcome to Python!")')
                            print("\n2. Types of Loops in Python")
                            print("for loop: repeats instructions for each item in a sequence.")
                            print("while loop: repeats instructions while a condition is True.")
                            print("\nfor-loop example from the PPT:")
                            print("for number in range(3):")
                            print('    print("Hello!")')
                            print("\nwhile-loop example from the PPT:")
                            print("count = 1")
                            print("while count <= 3:")
                            print('    print("Hello!")')
                            print("    count += 1")
                            print("\n3. The for Loop and range()")
                            print("The range() function provides a sequence of numbers.")
                            print("Example from the PPT:")
                            print("for number in range(1, 6):")
                            print("    print(number)")
                            print("\n4. Counting Down with range()")
                            print("Example from the PPT:")
                            print("for number in range(5, 0, -1):")
                            print("    print(number)")
                            print("\n5. The while Loop")
                            print("A while loop repeats while its condition is True.")
                            print("Example from the PPT:")
                            print("count = 1")
                            print("while count <= 5:")
                            print("    print(count)")
                            print("    count += 1")
                            print("\n6. Counting Down with a while Loop")
                            print("Example from the PPT:")
                            print("number = 5")
                            print("while number >= 1:")
                            print("    print(number)")
                            print("    number -= 1")
                            print("\n7. Repeating a Program with while True")
                            print("Example from the PPT:")
                            print("while True:")
                            print('    name = input("Enter your name (X to exit): ")')
                            print('    if name.upper() == "X":')
                            print('        print("Program stopped.")')
                            print("        break")
                            print('    print("Hello,", name)')

                        #AFTER THE LESSON
                        if module_choice != "0":
                            print("\n============================================================")
                            print("                    LESSON FINISHED")
                            print("============================================================")
                            print("You have reached the end of this lesson.")
                            print("\n1. Take the Quiz")
                            print("2. Back to Dashboard")

                            lesson_choice = input("\nEnter your choice: ")

                            while lesson_choice != "1" and lesson_choice != "2":
                                print("Invalid choice. Please try again.")
                                lesson_choice = input("Enter your choice: ")

                            #QUIZ
                            if lesson_choice == "1":
                                quiz_score = 0
                                question_number = 1
                                total_questions = 3

                                print("\n============================================================")
                                print("                         QUIZ")
                                print("============================================================")
                                print("Read each question and choose the correct answer.")

                                while question_number <= total_questions:
                                    print("\n------------------------------------------------------------")
                                    print(f"Question {question_number} of {total_questions}")

                                    correct_answer = ""

                                    #MODULE 1 QUESTIONS
                                    if module_choice == "1":
                                        if question_number == 1:
                                            print("What is a programming language used for?")
                                            print("A. Giving instructions to a computer")
                                            print("B. Cleaning a computer screen")
                                            print("C. Charging a computer")
                                            print("D. Changing the keyboard")
                                            correct_answer = "A"
                                        elif question_number == 2:
                                            print("How is Python described in the PPT?")
                                            print("A. A web browser")
                                            print("B. A high-level, interpreted, general-purpose language")
                                            print("C. A computer part")
                                            print("D. An operating system")
                                            correct_answer = "B"
                                        elif question_number == 3:
                                            print("Which is a reason to learn Python?")
                                            print("A. It is only for experts")
                                            print("B. It cannot be used for different tasks")
                                            print("C. It is simple and easy to learn")
                                            print("D. It has no community support")
                                            correct_answer = "C"

                                    #MODULE 2 QUESTIONS
                                    elif module_choice == "2":
                                        if question_number == 1:
                                            print("What does Python syntax mean?")
                                            print("A. Rules for writing Python code correctly")
                                            print("B. The color of a program")
                                            print("C. The computer brand")
                                            print("D. The name of a folder")
                                            correct_answer = "A"
                                        elif question_number == 2:
                                            print("Which function displays information on the screen?")
                                            print("A. input()")
                                            print("B. print()")
                                            print("C. range()")
                                            print("D. float()")
                                            correct_answer = "B"
                                        elif question_number == 3:
                                            print("Which symbol starts a single-line comment?")
                                            print("A. @")
                                            print("B. #")
                                            print("C. $")
                                            print("D. &")
                                            correct_answer = "B"

                                    #MODULE 3 QUESTIONS
                                    elif module_choice == "3":
                                        if question_number == 1:
                                            print("What is a variable?")
                                            print("A. A named storage location for data")
                                            print("B. A screen display")
                                            print("C. A type of keyboard")
                                            print("D. A comment in a program")
                                            correct_answer = "A"
                                        elif question_number == 2:
                                            print("Which variable name follows the rules in the PPT?")
                                            print("A. 1number")
                                            print("B. bread")
                                            print("C. space name")
                                            print("D. @value")
                                            correct_answer = "B"
                                        elif question_number == 3:
                                            print("Which data type is used for whole numbers?")
                                            print("A. str")
                                            print("B. int")
                                            print("C. float")
                                            print("D. bool")
                                            correct_answer = "B"

                                    #MODULE 4 QUESTIONS
                                    elif module_choice == "4":
                                        if question_number == 1:
                                            print("Which operator is used for multiplication?")
                                            print("A. +")
                                            print("B. -")
                                            print("C. *")
                                            print("D. /")
                                            correct_answer = "C"
                                        elif question_number == 2:
                                            print("What is the result of this expression?")
                                            print("17 // 3")
                                            print("A. 5")
                                            print("B. 5.6")
                                            print("C. 6")
                                            print("D. 2")
                                            correct_answer = "A"
                                        elif question_number == 3:
                                            print("What is the result of this code?")
                                            print("a = 2")
                                            print("b = 3")
                                            print("c = 4")
                                            print("print(a + b * c)")
                                            print("A. 20")
                                            print("B. 14")
                                            print("C. 4")
                                            print("D. Error")
                                            correct_answer = "B"

                                    #MODULE 5 QUESTIONS
                                    elif module_choice == "5":
                                        if question_number == 1:
                                            print("Which function accepts information from the user?")
                                            print("A. print()")
                                            print("B. input()")
                                            print("C. range()")
                                            print("D. int()")
                                            correct_answer = "B"
                                        elif question_number == 2:
                                            print("What type of value does input() return by default?")
                                            print("A. int")
                                            print("B. float")
                                            print("C. string")
                                            print("D. bool")
                                            correct_answer = "C"
                                        elif question_number == 3:
                                            print("Which function converts input to a decimal number?")
                                            print("A. int()")
                                            print("B. str()")
                                            print("C. float()")
                                            print("D. print()")
                                            correct_answer = "C"

                                    #MODULE 6 QUESTIONS
                                    elif module_choice == "6":
                                        if question_number == 1:
                                            print("When does the code inside an if statement run?")
                                            print("A. When the condition is True")
                                            print("B. When the condition is False")
                                            print("C. Only when the program ends")
                                            print("D. Every time without checking")
                                            correct_answer = "A"
                                        elif question_number == 2:
                                            print("Which keyword checks another condition?")
                                            print("A. else")
                                            print("B. elif")
                                            print("C. print")
                                            print("D. input")
                                            correct_answer = "B"
                                        elif question_number == 3:
                                            print("What is a nested condition?")
                                            print("A. An if statement inside another if statement")
                                            print("B. A print statement")
                                            print("C. A variable with no value")
                                            print("D. A loop that never ends")
                                            correct_answer = "A"

                                    #MODULE 7 QUESTIONS
                                    elif module_choice == "7":
                                        if question_number == 1:
                                            print("Which logical operator needs all conditions to be True?")
                                            print("A. or")
                                            print("B. not")
                                            print("C. and")
                                            print("D. if")
                                            correct_answer = "C"
                                        elif question_number == 2:
                                            print("When does the or operator return True?")
                                            print("A. When at least one condition is True")
                                            print("B. Only when all conditions are False")
                                            print("C. Only when all conditions are True")
                                            print("D. When there are no conditions")
                                            correct_answer = "A"
                                        elif question_number == 3:
                                            print("What does the not operator do?")
                                            print("A. Adds two values")
                                            print("B. Reverses the result of a condition")
                                            print("C. Repeats a program")
                                            print("D. Stores a value")
                                            correct_answer = "B"

                                    #MODULE 8 QUESTIONS
                                    elif module_choice == "8":
                                        if question_number == 1:
                                            print("What does iteration mean?")
                                            print("A. Repeating a set of instructions")
                                            print("B. Removing a variable")
                                            print("C. Printing one number only")
                                            print("D. Changing a computer setting")
                                            correct_answer = "A"
                                        elif question_number == 2:
                                            print("Which two loop types are covered in the PPT?")
                                            print("A. for and while")
                                            print("B. if and else")
                                            print("C. and and or")
                                            print("D. print and input")
                                            correct_answer = "A"
                                        elif question_number == 3:
                                            print("What numbers are displayed by this code?")
                                            print("for number in range(1, 6):")
                                            print("    print(number)")
                                            print("A. 1, 2, 3, 4, 5")
                                            print("B. 1, 2, 3, 4, 5, 6")
                                            print("C. 0, 1, 2, 3, 4, 5")
                                            print("D. 2, 3, 4, 5, 6")
                                            correct_answer = "A"

                                    answer = input("\nYour answer (A-D): ").upper()

                                    while answer != "A" and answer != "B" and answer != "C" and answer != "D":
                                        print("Invalid choice. Please enter A, B, C, or D.")
                                        answer = input("Your answer (A-D): ").upper()

                                    if answer == correct_answer:
                                        print("\nCorrect! Good job.")
                                        quiz_score = quiz_score + 1
                                    else:
                                        print(f"\nNot quite. The correct answer is {correct_answer}.")

                                    question_number = question_number + 1

                                #SAVE THE QUIZ RESULT IN PROGRESS VARIABLES
                                percentage = quiz_score / total_questions * 100

                                print("\n============================================================")
                                print("                      QUIZ RESULT")
                                print("============================================================")
                                print(f"Your Score : {quiz_score} / {total_questions}")
                                print(f"Percentage : {percentage:.2f}%")

                                if percentage >= 80:
                                    print("Feedback   : Excellent work!")
                                elif percentage >= 60:
                                    print("Feedback   : Good effort. Keep reviewing.")
                                else:
                                    print("Feedback   : Keep practicing and review the lesson.")

                                if module_choice == "1":
                                    module1_completed = True
                                    module1_attempts = module1_attempts + 1
                                    if quiz_score > module1_score:
                                        module1_score = quiz_score
                                elif module_choice == "2":
                                    module2_completed = True
                                    module2_attempts = module2_attempts + 1
                                    if quiz_score > module2_score:
                                        module2_score = quiz_score
                                elif module_choice == "3":
                                    module3_completed = True
                                    module3_attempts = module3_attempts + 1
                                    if quiz_score > module3_score:
                                        module3_score = quiz_score
                                elif module_choice == "4":
                                    module4_completed = True
                                    module4_attempts = module4_attempts + 1
                                    if quiz_score > module4_score:
                                        module4_score = quiz_score
                                elif module_choice == "5":
                                    module5_completed = True
                                    module5_attempts = module5_attempts + 1
                                    if quiz_score > module5_score:
                                        module5_score = quiz_score
                                elif module_choice == "6":
                                    module6_completed = True
                                    module6_attempts = module6_attempts + 1
                                    if quiz_score > module6_score:
                                        module6_score = quiz_score
                                elif module_choice == "7":
                                    module7_completed = True
                                    module7_attempts = module7_attempts + 1
                                    if quiz_score > module7_score:
                                        module7_score = quiz_score
                                elif module_choice == "8":
                                    module8_completed = True
                                    module8_attempts = module8_attempts + 1
                                    if quiz_score > module8_score:
                                        module8_score = quiz_score

                                input("\nPress ENTER to return to the dashboard...")

                            else:
                                print("Returning to dashboard...")
                                input("\nPress ENTER to continue...")

                    #MY PROFILE
                    elif dashboard_choice == "2":
                        completed_modules = 0

                        if module1_completed == True:
                            completed_modules = completed_modules + 1
                        if module2_completed == True:
                            completed_modules = completed_modules + 1
                        if module3_completed == True:
                            completed_modules = completed_modules + 1
                        if module4_completed == True:
                            completed_modules = completed_modules + 1
                        if module5_completed == True:
                            completed_modules = completed_modules + 1
                        if module6_completed == True:
                            completed_modules = completed_modules + 1
                        if module7_completed == True:
                            completed_modules = completed_modules + 1
                        if module8_completed == True:
                            completed_modules = completed_modules + 1

                        overall_progress = completed_modules / 8 * 100

                        print("\n======================== MY PROFILE ======================")
                        print(f"Full Name : {saved_full_name}")
                        print(f"Username  : {saved_username}")
                        print(f"Completed : {completed_modules} of 8 modules")
                        print(f"Progress  : {overall_progress:.2f}%")
                        input("\nPress ENTER to return to the dashboard...")

                    #VIEW PROGRESS
                    elif dashboard_choice == "3":
                        completed_modules = 0

                        if module1_completed == True:
                            completed_modules = completed_modules + 1
                        if module2_completed == True:
                            completed_modules = completed_modules + 1
                        if module3_completed == True:
                            completed_modules = completed_modules + 1
                        if module4_completed == True:
                            completed_modules = completed_modules + 1
                        if module5_completed == True:
                            completed_modules = completed_modules + 1
                        if module6_completed == True:
                            completed_modules = completed_modules + 1
                        if module7_completed == True:
                            completed_modules = completed_modules + 1
                        if module8_completed == True:
                            completed_modules = completed_modules + 1

                        overall_progress = completed_modules / 8 * 100

                        print("\n======================= VIEW PROGRESS =====================")
                        print(f"Completed Modules : {completed_modules} of 8")
                        print(f"Overall Progress  : {overall_progress:.2f}%")
                        print("\nMODULE STATUS")

                        if module1_completed == True:
                            print("1. Introduction to Programming - COMPLETED")
                        elif module1_viewed == True:
                            print("1. Introduction to Programming - LESSON VIEWED")
                        else:
                            print("1. Introduction to Programming - NOT STARTED")

                        if module2_completed == True:
                            print("2. Python Basic Syntax - COMPLETED")
                        elif module2_viewed == True:
                            print("2. Python Basic Syntax - LESSON VIEWED")
                        else:
                            print("2. Python Basic Syntax - NOT STARTED")

                        if module3_completed == True:
                            print("3. Variables, Constants, and Data Types - COMPLETED")
                        elif module3_viewed == True:
                            print("3. Variables, Constants, and Data Types - LESSON VIEWED")
                        else:
                            print("3. Variables, Constants, and Data Types - NOT STARTED")

                        if module4_completed == True:
                            print("4. Arithmetic Operators and Expressions - COMPLETED")
                        elif module4_viewed == True:
                            print("4. Arithmetic Operators and Expressions - LESSON VIEWED")
                        else:
                            print("4. Arithmetic Operators and Expressions - NOT STARTED")

                        if module5_completed == True:
                            print("5. Basic Input and Output in Python - COMPLETED")
                        elif module5_viewed == True:
                            print("5. Basic Input and Output in Python - LESSON VIEWED")
                        else:
                            print("5. Basic Input and Output in Python - NOT STARTED")

                        if module6_completed == True:
                            print("6. Conditional Statements - COMPLETED")
                        elif module6_viewed == True:
                            print("6. Conditional Statements - LESSON VIEWED")
                        else:
                            print("6. Conditional Statements - NOT STARTED")

                        if module7_completed == True:
                            print("7. Logical Operators - COMPLETED")
                        elif module7_viewed == True:
                            print("7. Logical Operators - LESSON VIEWED")
                        else:
                            print("7. Logical Operators - NOT STARTED")

                        if module8_completed == True:
                            print("8. Introduction to Iteration and Loops - COMPLETED")
                        elif module8_viewed == True:
                            print("8. Introduction to Iteration and Loops - LESSON VIEWED")
                        else:
                            print("8. Introduction to Iteration and Loops - NOT STARTED")

                        print("\nBEST QUIZ SCORES and QUIZ ATTEMPTS")
                        print(f"1. Introduction to Programming: {module1_score}/3 - Attempts: {module1_attempts}")
                        print(f"2. Python Basic Syntax: {module2_score}/3 - Attempts: {module2_attempts}")
                        print(f"3. Variables and Data Types: {module3_score}/3 - Attempts: {module3_attempts}")
                        print(f"4. Arithmetic and Expressions: {module4_score}/3 - Attempts: {module4_attempts}")
                        print(f"5. Basic Input and Output: {module5_score}/3 - Attempts: {module5_attempts}")
                        print(f"6. Conditional Statements: {module6_score}/3 - Attempts: {module6_attempts}")
                        print(f"7. Logical Operators: {module7_score}/3 - Attempts: {module7_attempts}")
                        print(f"8. Iteration and Loops: {module8_score}/3 - Attempts: {module8_attempts}")
                        input("\nPress ENTER to return to the dashboard...")

                    # LOG OUT
                    elif dashboard_choice == "4":
                        print("\nYou have been logged out.")
                        login_active = False
                        input("Press ENTER to return to the main menu...")

            else:
                print("\nInvalid username or password.")
                input("\nPress ENTER to return to the main menu...")


    #EXIT
    elif main_choice == "3":
        print("\nThank you for using the Programming Learning Portal!")
        print("Goodbye!")
        break

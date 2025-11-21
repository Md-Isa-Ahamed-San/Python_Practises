# [expression for item in iterable if condition]
## 🧩 **LEVEL 1: Basics**

# Practice simple transformations and element extraction.

# 1. ✅ Generate a list of numbers from `1` to `10`.

# pyright: ignore


ans = [i for i in range(1, 11)]
# print(ans)

# 2. ✅ Create a list of their squares.
li = [3, 2, 4, 1]
squares = [item**2 for item in li]
# print(squares)

# 3. ✅ Create a list of cubes for numbers from `1` to `5`.
li2 = [1, 2, 3, 4, 5]
cubes = [item**3 for item in li2]
# print(cubes)
# 4. ✅ Convert all characters in `"hello world"` to uppercase.
s = "hello world"
new_s_upper = [char.upper() for char in s]
new_s = "".join(new_s_upper)
# print(new_s)
# 5. ✅ Extract digits from a mixed string `"a1b2c3d4"`.
mixed_str = "a1b2c3d4"
digits = [digit for digit in mixed_str if digit.isdigit()]
# print(digits)


## 🧠 **LEVEL 2: With Conditions**

# Apply filters using `if`.

# 1. ✅ Get all even numbers between `1` and `20`.
even = [i for i in range(1, 21) if i % 2 == 0]
# print(even)


# 2. ✅ Get squares of odd numbers from `1` to `15`.
odd_squares = [i**2 for i in range(1, 16) if i % 2 != 0]
# print(odd_squares)

# 3. ✅ From a list of words `["apple", "banana", "cherry", "kiwi"]`, extract only those that contain the letter `'a'`.
list_words = ["apple", "banana", "cherry", "kiwi"]
words_with_a = [word for word in list_words if "a" in word]
# print(words_with_a)

# 4. ✅ Create a list of numbers divisible by both 3 and 5 from `1` to `50`.
divisible_by_3_and_5 = [i for i in range(1, 50) if (i % 3 == 0 and i % 5 == 0)]
# print(divisible_by_3_and_5)

# 5. ✅ Given `nums = [10, -5, 20, -15, 30]`, get absolute values for only the negative numbers.
nums = [10, -5, 20, -15, 30]
abs_neg = [abs(i) for i in nums if i < 0]
# print(abs_neg)


# Use functions, operations, and string formatting.

# 1. ✅ Convert `["Python", "is", "fun"]` → `["PYTHON", "IS", "FUN"]`.
words = ["Python", "is", "fun"]
new_words = [item.upper() for item in words]
# print(new_words)

# 2. ✅ From `["John", "Jane", "Jim"]`, create a list like `["Hi John", "Hi Jane", "Hi Jim"]`.
names = ["John", "Jane", "Jim"]
new_list = [f"Hi {name}" for name in names]
# print(new_list)
# 3. ✅ Convert `[1, 2, 3, 4, 5]` into strings like `"Number: 1"`, `"Number: 2"`, …
num_list = [1, 2, 3, 4, 5]
str_list = [f"Number {num}" for num in num_list]
# print(str_list)
# 4. ✅ From `[10, 20, 30]`, compute half the value of each number.
nums2 = [10, 20, 30]
half_num2 = [num // 2 for num in nums2]
# print(half_num2)

# 5. ✅ Flatten `[1, [2, 3], [4, 5]]` into a single list `[1, 2, 3, 4, 5]` (hint: nested comprehension or loop unpacking).
# [expression for outer in outer_iterable for inner in inner_iterable]
nested_list = [1, [2, 3], [4, 5]]
# flattened = [(x,y) for x for sublist in nested_list for y in nested_sub_list]

# flattened = [item for sublist in nested_list for item in (sublist if isinstance(sublist, list) else [sublist])]
# flattened = [item for item in nested_list for subItem in item ]
# print(flattened)

# ### **Exercise 3: Password Validator (Medium)**

# Create a password validator that checks:

# - At least 8 characters long
# - Contains at least one digit
# - Contains at least one uppercase letter
# - Contains at least one lowercase letter

# Keep asking until valid password entered.


# def pass_validator(password):
#     if len(password) < 8:
#         print("At Least 8 characters long")
#     elif not any(char.isdigit() for char in password):
#         print("At least one digit")
#     elif not any(char.isupper() for char in password):
#         print("At least one uppercase letter letter")
#     elif not any(char.islower() for char in password):
#         print("At least one lowercase letter")
#     else:
#         print("Valid Password")
#         return True

#     return False


# while True:
#     pwd = input("Enter Password: ")
#     if pass_validator(pwd):
#         break


# - Computer picks random number 1-100
# - User gets 7 attempts
# - After each guess, show "Higher" or "Lower"
# - Show remaining attempts
# - Congratulate on win or reveal answer on loss


def guessing_game(number):
    attempts = 7
    number = random.randint(1, 100)

    for i in range(1, attempts + 1):
        guess = int(input("Enter your guess (1-100): "))
        if guess == number:
            print("Congratulations! You've guessed the number!")
            return
        elif guess < number:
            print("Higher!")
        elif i == 7:
            print(f"Sorry, you've used all attempts. The number was {number}.")
            return
        else:
            print("Lower!")
        print(f"Attempts remaining: {attempts - i}")


# guessing_game(8)


# === TASK MANAGER ===
# 1. Add Task
# 2. View Tasks
# 3. Mark Complete
# 4. Delete Task
# 5. View Statistics
# 6. Exit

# Choose option: _


def task_manager():
    tasks = []

    while True:
        print("\n=== Task Manager ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Complete")
        print("4. Delete Task")
        print("5. View Statistics")
        print("6. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            print("\n--- Add Task ---")
            title = input("Enter task title: ")
            tasks.append({"title": {title}, "completed": False})
            print("Task added.")
        elif choice == "2":
            print("\n--- View Tasks ---")
            if not tasks:
                print("No tasks available.")
            else:
                for idx, task in enumerate(tasks, 1):
                    status = "Completed" if task["completed"] else "Pending"

                    print(f"{idx}. {task['title']} - {status}")
        elif choice == "3":
            print("\n --- Tasks Lists ---")
            if not tasks:
                print("No tasks Available")
            else:
                for idx, task in enumerate(tasks):
                    print(f"{idx + 1}.{task}")
                task_num = int(input("Enter task number to mark complete: "))
                if 0< task_num <= len(tasks):
                    # Mark task as complete
                    tasks[task_num-1]["completed"]=True
                    print("Task marked as complete.")
                else:
                    print("invalid task number")
        elif choice == "4":
            print("\n ---Delete Task ---")
            if not tasks:
                print("No tasks Available")
            else:
                for idx, task in enumerate(tasks):
                        print(f"{idx + 1}.{task}")
                task_num = int(input("Enter task number to delete: "))
                if 0<task_num <= len(tasks):
                    tasks.pop(task_num-1)
                    print("Task deleted.")
                else:
                    print("Invalid task number")
        elif choice == "5":
            print("\n --- Statistics ---")
            total_tasks = len(tasks)
            completed_tasks = sum(1 for task in tasks if task["completed"])
            incomplete_tasks = total_tasks - completed_tasks

            print(f"Total Tasks: {total_tasks}")
            print(f"Completed Tasks: {completed_tasks}")
            print(f"Incomplete Tasks: {incomplete_tasks}")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid option.")



task_manager()


"""
 Challenge: Self-Intro Script Generator

Create a Python script that interacts with the user and generates a personalized self-introduction.

Your program should:
1. Ask the user for their name, age, city, profession, and favorite hobby.
2. Format this data into a warm, friendly paragraph of self-introduction.
3. Print the final paragraph in a clean and readable format.

Example:
If the user inputs:
  Name: Priya
  Age: 22
  City: Jaipur
  Profession: Software Developer
  Hobby: playing guitar

Your script might output:
  "Hello! My name is Priya. I'm 22 years old and live in Jaipur. I work as a Software Developer and I absolutely enjoy playing guitar in my free time. Nice to meet you!"

Bonus:
- Add the current date to the end of the paragraph like: "Logged on: 2025-06-14"
- Wrap the printed message with a decorative border of stars (*)
"""

import datetime

name = input("What is your name?\n").strip()
age = input("How old are you?\n").strip()
city = input("In which city do you live in?\n").strip()
profession = input("what is your profession?\n").strip()
hobby = input("what is your hobby?\n").strip()

intro_msg = (
    f"Hello! my name is {name}, I'm {age} years old and live in {city}. "
    f"I work as a {profession} and I absolutely enjoy {hobby} in my free time. "
    f"Nice to meet you!\n"
)

current_date = datetime.date.today().isoformat()
intro_msg += f"\n Logged on: {current_date} \n"

border = "*" * 80
final_output = f"{border}\n {intro_msg} \n {border}"
print(final_output)





#                                        using loops 

# import datetime

# questions = {
#     "name": "What is your name?\n",
#     "age": "How old are you?\n",
#     "city": "In which city do you live in?\n",
#     "profession": "What is your profession?\n",
#     "hobby": "What is your hobby?\n",
# }

# answers = {}

# for key, question in questions.items():
#     answers[key] = input(question).strip()

# intro_msg = (
#     f"Hello! my name is {answers['name']}, I'm {answers['age']} years old and live in {answers['city']}. "
#     f"I work as a {answers['profession']} and I absolutely enjoy {answers['hobby']} in my free time. "
#     f"Nice to meet you!\n"
# )

# current_date = datetime.date.today().isoformat()
# intro_msg += f"\n Logged on: {current_date} \n"

# border = "*" * 80
# final_output = f"{border}\n {intro_msg} \n{border}"
# print(final_output)

from classes import Student
from classes import Question
from classes import Chef
from classes import ChineseChef

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 3.8, True)

print(student1.name)
print(student2.gpa)
print(student1.on_honor_roll())

myChef = Chef()
myChef.make_chicken()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_chicken()
myChineseChef.make_special_dish()
myChineseChef.make_fried_rice()

# question_prompts = [
#     "What color are apples?\n(a) Red/Green/\n(b) Purple\n(c) Orange\n\n",
#     "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
#     "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
# ]

# questions = [
#     Question(question_prompts[0], "a"),
#     Question(question_prompts[1], "c"),
#     Question(question_prompts[2], "b")
# ]

# def run_test(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.prompt)
#         if answer == question.answer:
#             score += 1

#     print("You got " + str(score) + "/" + str(len(questions)) + " correct")

# run_test(questions)
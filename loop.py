i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with it")

for letter in "Giraffe Academy":
    print(letter)

friends = ["Jim", "Karen", "Kevin"]
for friend in friends: #you can name it whatever you want - friend, name, i etc.
    print(friend)

for index in range(len(friends)):
    print(index)

for index in range(len(friends)):
    print(friends[index])

for index in range(10):
    print(index)

for index in range(3,10):
    print(index)

for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not first")

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You lose!")
else:
    print("You win!")

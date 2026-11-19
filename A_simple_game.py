secret_word = "Python"
hint = "Suggestion of a language"
guess = "" #Response of the player
guess_count = 0
guess_limit = 5
print(hint)

#The player wants to choose many response
while guess != secret_word:
    if guess_count < guess_limit:
     guess = input("Guess a word:")
     guess_count += 1
    else:
        break
if guess == secret_word:
    print("Correct")
else:
    print("You don't success because you exceed the limit of five responses!!!!")
import random

name = input("what is your name?")
print("good luck", name)

repeat = True
while repeat == True :
    vegetables = ['onion','tomato','potato','brinjal','pumpkin','cucumber','ginger','bittergourd','cauliflower','beetroot']
    fruits = ['apple','mango','melon','papaya','banana','grapes','cherry','orange','pineapple','jackfruit','strawberry']
    animals = ['lion','tiger','ant','dog','donkey','monkey','horse','mouse','zebra','snake','rabbit','crow','pigeon']
    things = ['notebook','pencil','pen','sharpener','eraser','duster','cutter','glue','calculator','colour','paper']

    words = vegetables + fruits + animals + things
    word = random.choice(words)
    print("your word has", len(word),"letters.")
    if word in vegetables:
      print("Hint: I am a vegetable")
    elif word in fruits:
      print("Hint: I am a fruit")
    elif word in animals:
      print("Hint: I am an animal")
    elif word in things:
      print("Hint: I am a thing")

    guesses = ''
    turns = 10
    while turns > 0:
       failed = 0
       for char in word:
            if char in guesses:
               print(char,end=' ')
            else:
               print("_",end=' ')
               failed += 1
       if failed == 0:
          print("You win")
          print("The word is:",word)
          break
       guess = input("guess a character:")
       guesses += guess
       if guess not in word:
          turns -= 1
          print("wrong")
          print("you have", + turns,'more guesses')
          if turns ==0:
             print("You loose")
             print("The correct word is",word)
    play_again = input("Do you want to play again?Type y for yes and n for no:")
    if play_again == "n":
        repeat = False
            
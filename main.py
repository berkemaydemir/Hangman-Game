import random
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list

print(logo)
which_word=random.randint(0,len(word_list)-1)
answer=word_list[which_word]
answer_lenght=len(answer)
print(answer)
end_game= False
lives=6

blink_list=[]
for i in range (0,len(answer)):
  blink_list.append("_")
print(blink_list)

guess_list=[]

while not end_game == True :
  guess=input("Guess a letter: ").lower()
  
  for i in guess_list:
    if i == guess :
      print("You have already guess this letter")   
      del guess_list [-1]

  answer_check=answer.count(guess)
  if answer_check>0:
         
    guess_list.append(guess)
    print(f"It has got {answer_check} letter")
  else:
    if i==guess:
      lives+=1
    guess_list.append(guess)   
    lives -= 1
    print(stages[lives])
    print("Letter is not in the word")
    print(f"You have a {lives} left")
    if lives == 0:
      end_game=True
      print("You Lose")
      print(f"Answer is: {answer}")

  for i in range(answer_lenght):
    
    if guess==answer[i]:
      blink_list[i]=guess
   
  print(blink_list)
  if blink_list.count("_") == 0:
    end_game=True
    print("You win")  


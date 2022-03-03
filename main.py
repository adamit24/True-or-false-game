# True or False Quiz

correct = 0
answered = 0
totalScore = 0


print('Welcome to the True or False Quiz about Python')
# ---- Questions ------

print('Question 1: \n'
      'A Burmese Python are Venomous. If you get bitten by one you need to go to the hospital. (T/F)')
answer = input('').upper()
if answer == 'T':
    print('Your answer is incorrect. In fact, Burmese Pythons are not Venomous \n'
          'Their bite still hurts very badly, but you wouldn\'t have to go to the hospital \n')
    answered += 1
elif answer == 'F':
      print('Your answer is correct. \n'
            'Burmese Pythons are non-venomous. But you still wouldn\'t want to get bitten.')
      correct += 1
      answered += 1
else:
      print('You have typed an invalid answer')

# Question 2 ---
print('Question 2: \n'
      'Burmese Pythons are one of the smallest snakes in the world.(T/F)')
answer = input('').upper()
if answer == 'T':
    print('Your answer is incorrect. \n'
          'Burmese Pythons are actually one of the top five largest snakes in the world \n'
          'The only thing that is larger than a Burmese is a Green Anaconda. \n'
          'However, other types of pythons take up the majority of the top 11 largest snakes. \n'
          'Burmese are the largest python, followed by:'
          'Reticulated Python \n'
          'African Rock Python \n'
          'Indian Python \n'
          'Amethystine (Scrub) Python \n'
          'And at 11 the Papuan Python \n')

    answered += 1
elif answer == 'F':
      print('Your answer is correct. \n'
            'The Burmese Python is actually the second largest snake in the world! \n'
            'The only thing beating it is the Green Anaconda.')
      correct += 1
      answered += 1
else:
      print('You have typed an invalid answer')


# Question 3
print('Question 3: \n'
      'Pythons are solitary animals. They only really come together during the spring for mating. (T/F)')
answer = input('').upper()
if answer == 'T':
      print('Your answer is correct. \n'
            'This is a shared characteristic with many reptiles, solitary. \n'
            'Reptiles Know what is up... Humans could learn a thing or two. \n')
      correct += 1
      answered += 1
elif answer == 'F':
      print('Your answer is incorrect. \n'
            'Pythons, or snakes in general, rarely get lonely \n'
            'The prefer to be alone due to hunting and resources \n'
            'A lot of snakes will attack each other because they are territorial \n')

      answered += 1
else:
      print('You have typed an invalid answer')

# Question 4 -----
print('Question 4: \n'
      'Pythons inject their prey with venom and then eat them after they have died. (T/F)')
answer = input('').upper()
if answer == 'T':
      print('Your answer is incorrect. \n'
            'Bro... we just answered a question about them NOT being venomous. \n'
            'smh')

      answered += 1
elif answer == 'F':
      print('Your answer is correct. \n'
            'As we discussed earlier, Pythons are not venomous. \n'
            'So how do they kill their prey? \n'
            'They do this by suffocating them. The python will coild themselves aroudn the prey then \n'
            'constrict their muscles, squeezing whatever they have within their grasps until it cannot breathe. \n'
            'This is why I hate hugs...\n')

      correct += 1
      answered += 1
else:
      print('You have typed an invalid answer')

# Question 5 --
print('Question 5: \n'
      'You totally thought that this was going to be a quiz about the Python Programming language, didn\'t you? (T/F)')
answer = input('').upper()
if answer == 'T':
      print('Oh yes, Adami... You totally got me. \n'
            'How dare you think that you could actually be serious for even the slightest moment... \n')
      correct += 1
      answered += 1
elif answer == 'F':
      print('No, Adami, I know you have a terrible since of humor. \n'
            'I completely expected a python pun at some point during the Unit...')
      correct += 1
      answered += 1
else:
      print('You have typed an invalid answer')

# Calculate the scores
print('You got', correct, 'during the quiz')
print('This is out of', answered, 'questions')
print('Your score is', correct,'/', answered,'. Which gives you a total score of:', (correct/answered) * 100, '%')

# Extra Practice:
# Currently, our program is only taking capital letters. If I try to use a lower case t or f it will
# give me the invalid response. How can we edit the program to accept user input both positive and negative.
# Also, how can we enhance this project to allow the user to type 'True/true' or 'False/false'?

# We gave the user a percentage, but lets change some things.
# 1. Let's get rid of the float aspect '20.0%' and make it 20%
# 2. Use the typical grade scale provided by your school. If the user falls within the range, give them
# 3. That specific letter grade:
# A = 90 - 100, B = 80 - 89, C = 70 - 79, D = 60 - 69, F = 59 and lower

# 3. Finally, leave a customizable message based off the score they received. For example:
# Output:
# 'Woo, you got an 100% on the quiz, that is an A'
# 'You sure know a lot about Burmese Pythons... weird flex but okay...

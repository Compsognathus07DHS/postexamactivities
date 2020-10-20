while True:
  description = input(print("Title of program: Compsognathus bot (ESPECIALLY for fellow 'Compsognathi'!")
print()
while True:
  description = input("HI! I am a virtual Compsognathus from a few million years ago, brought to comfort you in this app! You can tell me how you feel about your exams in a sentence, cause, well, sometimes you need a dinosaur to be there for ya.")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("tomorrow will be a better day. 不忘初心，锐意进取！(my motto!) That is, don't forget what you set out to do and do it to your best ability")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("to keep smiling. I'm so happy for you that you bounced back from troubles and achieved your goals! Well if you haven't, stay optimistic and open to challenges")
      counter += 1
    if each_word == "I am a fellow Compsognathus":
      feelings_list.append("Compsognathus")
      encouragement_list.append("you are stronger than you think, keep going! Congratulations and jiayou for our successes! Be 自豪 (proud in a good way) about your achievements, and STRIVE FOR THE BEST! I know it's in you! Seems like you are a fellow Compsognathus (hey did you look at the code ;) ) so I will hereby say: To shine like the sun, you have to first burn like it. This is my favourite quote among others, and I hope it would keep you inspired!")
      counter += 2

  if counter == 0:
    
      output = "Sorry I don't really understand. My Jurassic brain can't process that fab vocab! Please use different words? I'll look that up later. "

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  
  elif counter == 2:
      output = "AHA! YOU! I SMELL THE COMPSOGNATHUS IN YOU!"

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()

  

while True:
  description = input(print("Title of program: Compsognathus bot")
print()
while True:
  description = input("HI! I am a virtual Compsognathus from a few million years ago, brought to comfort you in this app! You can tell me how you feel in a sentence, cause, well, sometimes you need a dinosaur to be there for ya.")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("tomorrow will be a better day")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("to keep smiling")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("you are stronger than you think")
      counter += 1
    if each_word == "angry":
      feelings_list.append("angry")
      encouragement_list.append("Calm down and breathe in and out. Relax")
      counter += 1
    if each_word == "nervous":
      feelings_list.append("nervous")
      encouragement_list.append("Don't think too much.I believe you can do it")
      counter += 1
    if each_word == "bored":
      feelings_list.append("bored")
      encouragement_list.append("There's lots of fun things to do! You can read, draw, dance or even sing!")
      counter += 1
  if counter == 0:
    
      output = "Sorry I don't really understand. My Jurassic brain can't process that fab vocab! Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

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

  

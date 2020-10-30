print("Title of program: Compsognathus bot")
print()
print("HI! I am a virtual Compsognathus from a few million years ago, brought to comfort you in this app! You can tell me how you feel in a sentence, cause, well, sometimes you need a dinosaur to be there for ya.")
print()

while True:
  description = input("How do you feel?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("upset")
      encouragement_list.append("that tomorrow will be a better day")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("That is great! Keep smiling and spread the joy")
      counter += 2
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("to take a break and drink some water, it'll help you feel and focus better")
      counter += 1
    if each_word == "angry":
      feelings_list.append("angry")
      encouragement_list.append("to calm down and breathe in and out. Relax")
      counter += 1
    if each_word == "nervous":
      feelings_list.append("nervous")
      encouragement_list.append("Don't think too much about it. I believe you can do it")
      counter += 2
    if each_word == "bored":
      feelings_list.append("bored")
      encouragement_list.append("There's lots of fun things to do! You can read, draw, dance or even sing!")
      counter += 1
    if each_word == "upset":
      feelings_list.append("distressed")
      encouragement_list.append(" Remember to calm yourself, talk to your parents or friends, find something you enjoy to take your mind of your source of distress. Hope you feel better(:")
      counter += 2
    if each_word == "irritated":
      feelings_list.append("irritated")
      encouragement_list.append("Relax, don't waste your time and attention on the thing that is making you feel upset or annoyed, maintain a peaceful mind and be sure to make rational decisions")
      counter += 2
    if each_word == "dread":
      feelings_list.append("dreadful and nervous")
      encouragement_list.append("you are strong enough to face your challenges, you can overcome your problems and things will work out, don't dread the future too much")
      counter += 1   
    if each_word == "dreading":
      feelings_list.append("dreadful and nervous")
      encouragement_list.append("you are strong enough to face your challenges, you can overcome your problems and things will work out, don't dread what's to come too much")
      counter =+ 1   
    if each_word == "lazy":
      feelings_list.append("lazy")
      encouragement_list.append(" Do remember to plan you time wisely, play hard, work hard. You can laze but also do something meningful so that you won't regret wasting your time")
      counter += 2   
    if each_word == "giving" and "up":
      feelings_list.append("a lack of motivation")
      encouragement_list.append("there are people supporting you. Don't give up, continue working towards your goals, you are stronger than you think")
      counter += 1 
    if each_word == "excited":
      feelings_list.append("excited")
      encouragement_list.append(" About what? I assume it's a good thing then, good for you! (:")
      counter += 2   
                      
                      
  if counter == 0:
    
      output = "Sorry I don't really understand. My Jurassic brain can't process that fab vocab! Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember "+ encouragement_list[0] + "! Hope you feel better :)"  
                      
  elif counter == 2:
      output = "It seems that you are feeling quite " + feelings_list[0] + "." + encouragement_list[0]
                      
  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + "." + encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()




  

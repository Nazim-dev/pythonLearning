#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []

with open("Day 24/Input/Names/invited_names.txt") as name_file:
    content = name_file.read()
    names = content.split()
  
with open("Day 24/Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    print(letter)


for name in names:
    invite = letter.replace("[name]", name)
    with open(f"Day 24/Output/ReadyToSend/{name}_invite", mode="w") as to_send:
        to_send.write(invite)
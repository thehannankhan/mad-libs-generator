# ----- Mad Libs Generator -----

#Loop back to this point once code finishes
loop = 1
while (loop < 11):
# Taking user input
    noun = input("Choose a noun: ")
    p_noun = input("Choose a plural noun: ")
    noun2 = input("Choose a noun: ")
    place = input("Name a place: ")
    adjective = input("Choose an adjective (Describing word): ")
    noun3 = input("Choose a noun: ")
    noun4 = input("Choose a noun: ")
# Displays the story based on the users input
    print ("------------------------------------------")
    print ("Be kind to your",noun,"- footed", p_noun)
    print ("For a duck may be somebody's", noun2,",")
    print ("Be kind to your",p_noun,"in",place)
    print ("Where the weather is always",adjective,".")
    print ()
    print ("You may think that is this the",noun3,",")
    print ("Well it is.")
    print ("we all love", noun4, "here")
    print ("------------------------------------------")
# Loop back to "loop = 1"
    loop = loop + 1
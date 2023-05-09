#Import date and time to the code - it will help at the end in main when writing to file
import datetime

#Function asks user a question and then returns user answer

def get_intensity():
    intensity = int(input("How intense is your current emotion on a scale of 1-10? "))
    return intensity

#Function gets user answer from get_intensity function, and based on user answer decides what the intensity of the emotion is, returns answer
def get_emotion(intensity):
    if intensity <= 3:
        return "Mild Emotion"
    elif intensity <= 7:
        return "Moderate Emotion"
    else:
        return "Strong Emotion"

#Function asks user if their emotion is positive, negative , or if they don't know, returns answer
def get_positive_negative():
    #.upper converts user answer to uppercase
    positive_negative = input("Is your current emotion predominantly positive (P), negative (N), do you not know (D)? ").upper()
    return positive_negative

def get_p_situation():
    # Function to assess the source of emotion
    #Used a dictionary called options to store questions instead of numerous print statements
    #Dictonary has 3 keys -> first three options that the user is given (explained further in essay)
    #Each key has 3 corresponding values which are the emotions that get returned 
    options = {
        "An accomplishment or success": [
            "Joy",
            "Pride",
            "Accepted"
        ],
        "A relationship or social situation": [
            "Love",
            "Affection",
            "Admiration"
        ],
        "An event or experience": [
            "Excitement",
            "Surprise",
            "Awe"
        ]
    }
    
    #Asks user to pick from the 3 dictionary keys : success, relationship, experience
    print("Is the source of the emotion:")
    #enumerate keeps track of number and option Ex, ( 0, success) 
    for i, option in enumerate(options.keys()):
        #prints the 3 keys that the user chooses from 
        print(f"{i+1}. {option}")
    
    while True:
        try:
            #asks for user input stores it in ans variable
            ans = int(input("Enter your choice (1/2/3): "))
            #Error check -> makes sure user entered a number between 1 and 3 inclusive
            if 1 <= ans <= 3:
                # selected_option and feelings gets the values from the key selected for example is user chose 1 success (selected_option), then the keys retrieved are : joy,pride, and accepted(feelings)
                selected_option = list(options.keys())[ans-1]
                feelings = options[selected_option]
                print("Are you feeling:")
                #prints the feelings - enumerate keeps track of the index too
                for i, feeling in enumerate(feelings):
                    print(feeling)
                while True:
                    try:
                        #asks for user input stores it in emotion
                        emotion = int(input("Enter your choice (1/2/3): "))
                        #error check to make sure user entered a number between 1 and 3 inclusive
                        if 1 <= emotion <= 3:
                            #returns the emotion that the user selected
                            print(f"You are feeling: {feelings[emotion-1]}")
                            return feelings[emotion-1]
                        #if user did not enter a value between 1 and 3 this error statement is printed 
                        else:
                            print("Invalid input. Please try again.")
                    # A try block needs an except - except is a way of error handling
                    #ValueError deals with any errors that might occur when converting user input to integer
                    except ValueError:
                        print("Invalid input. Please try again.")
                #break because I want to end the code here if there is an error
                break
            #corresponds to the first error handling : selected_options to make sure user enters value between 1 and 3
            else:
                print("Invalid input. Please try again.")
        #Except for the first try - ValueError deals with conversion of user input to integer and any errors that might occur in that case
        except ValueError:
            print("Invalid input. Please try again.")

#function is user selects feeling a negative emotion
def get_n_situation():
    #dictionary with options keys and 3 values for each key
    options = {
        "Treat or danger": [
            "Fear",
            "Anxiety",
            "Insecure"
        ],
        "Loss or disappointment": [
            "Sad",
            "Grief",
            "Disappointment"
        ],
        "An event or experience": [
            "Anger",
            "Frustration",
            "Resentment"
        ]
    }
    
    #code block is the same as the one in get_p_situation
    print("Is the source of the emotion:")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    while True:
        try:
            ans = int(input("Enter your choice (1/2/3): "))
            if 1 <= ans <= 3:
                selected_option = list(options.keys())[ans-1]
                feelings = options[selected_option]
                print("Are you feeling:")
                for i, feeling in enumerate(feelings):
                    print(feeling)
                while True:
                    try:
                        emotion = int(input("Enter your choice (1/2/3): "))
                        if 1 <= emotion <= 3:
                            print(f"You are feeling: {feelings[emotion-1]}")
                            return feelings[emotion-1]
                        else:
                            print("Invalid input. Please try again.")
                    except ValueError:
                        print("Invalid input. Please try again.")
                break
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")
    
#Function is user selects they do not know if their emotion is position or negative
def get_dk_situation():
    #options dictionary - similar to the ones in get_p_situation and get_n_situation
    options = {
        "A conflict or goal": [
            "Frustration",
            "Ambivalence",
            "Hesitant"
        ],
        "Uncertain or ambiguous situation": [
            "Anxiety",
            "Confusion",
            "Stressed"
        ],
        "An event or experience": [
            "Mixed Emotions",
            "Disgust",
            "Resentment"
        ]
    }
    
    #same code block as get_p_situation and get_n_situation
    print("Is the source of the emotion:")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    while True:
        try:
            ans = int(input("Enter your choice (1/2/3): "))
            if 1 <= ans <= 3:
                selected_option = list(options.keys())[ans-1]
                feelings = options[selected_option]
                print("Are you feeling:")
                for i, feeling in enumerate(feelings):
                    print(feeling)
                while True:
                    try:
                        emotion = int(input("Enter your choice (1/2/3): "))
                        if 1 <= emotion <= 3:
                            print(f"You are feeling: {feelings[emotion-1]}")
                            return feelings[emotion-1]
                        else:
                            print("Invalid input. Please try again.")
                    except ValueError:
                        print("Invalid input. Please try again.")
                break
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")



def main():
    print("Welcome to the Emotion Identifier!")
    print("Please answer the following questions...")

    # get emotion intensity value
    intensity = get_intensity()
    # what intensity value means : mild, moderate, or strong
    emotion_level = get_emotion(intensity)
    # If the feeling was positive, negative, user does not know
    positive_negative = get_positive_negative()
    #runs function get_p_situation if user stated positive feeling
    if positive_negative == "P":
        emotion = get_p_situation()
    #runs function get_n_situation is user stated negative feeling
    elif positive_negative == "N":
        emotion = get_n_situation()
    #runs function get_dk_situation is user stated don't know 
    else:
        emotion = get_dk_situation()

    # write emotion details to file
    #now variable uses datetime import to store current date adn time 
    now = datetime.datetime.now()
    #new file called emotion_log with specified now variable in the title
    filename = f"emotion_log_{now.strftime('%Y-%m-%d')}.txt"
    
    #with closes the file automatically once we are done writing to it
    #Thonny warning Using open without explicitly specifying an encoding
    # Googled - said to specify  utf-8 encoding 
    with open(filename, 'a',encoding='utf-8') as f:
        #writes current date to the file
        #strftime('%Y-%m-%d') is how to use the datetime import and how to format the information
        #Information from import module 
        f.write(f"Date: {now.strftime('%Y-%m-%d')}\n")
        #writes current time to the file
        f.write(f"Time: {now.strftime('%H:%M:%S')}\n")
        #writes the users emotional state to the file
        f.write(f"Feeling: {emotion}\n")
        #write the number and what that means to the file - example 4, Moderate Emotion
        f.write(f"Intensity: {intensity, emotion_level}\n")
        #aesthetic separate for text for readablility 
        f.write("--------------------\n")

    # print the identified emotion for the user to see in the terminal/shell
    print("You feel it as a", emotion_level)

#Runs the main function
main()



# Computer Vision RPS
# Milestone 2:
I have managed to create the keras_model file through teachable machine. I experienced a few difficulties when trying to trying to make sure that rock, paper, scissors and nothing would be distinguishable when trialling out the different variables. It took a lot of time with trial and error to make sure that there was no characteristic in each of the variables that were making the programme incorrectly recognise which variable I was trying to display. The files created have been pushed to git hub and the variables are now all very disguishable with on average 100 percent recognition of each othe images displayed. 
When I downloaded the keras files I also copied the code suggested in order to support myself when creating the programme in visual space code as I have not completed a task involving machone learning before. 

# Milestone 4
I have created the manual_rps.py which contains the code to run the game hangman without picture. The imput for this code is only based on written imput not visual. When creating this code I followed the instrutions as advised on the portal. However, I found it beneficial to add an imput validation section to make sure that the imput the user provided would be imput that the game would recognise. I also added a print welcome message to make it more appealing to the user. I  did contemplate whether to add an additional scoring option within the game. However as it was not on the portal instructions I decided not to as to not over complicate the code. I have ran the code and it runs correctly but does run on a continuous loop because I have not coded a scoring system to break the loop to end the game. I would also like to add at this point that I did experience some issues with milestone 3 which took considerable longer than I anticipated as I was unable to run the python file through the terminal as I kept getting an error message. However, the file rn perfectly fine when I types in python milestone_3_task_4.py in the terminal.

# Milestone 5
In milestone 5 I have managed to bring together the rock, paper scissors game. I had to make a lot of changes in order to make the game work when combining the RPS_template.py file with the manual_rsp.py file. First of all I needed to remove the main function as the camera and the game was running as two seperate files within the camera_rps.py file. I also had to add in the variable of "nothing" as I did not realise I had not included that previously. I decided to add in a while loop which would provide the countdown on the camera which would allow the user to see when each round is about to start: 
(font = cv2.FONT_HERSHEY_SIMPLEX 
    org = (50, 50) 
    fontScale = 1
    color = (255, 0, 0) 
    thickness = 2
  
    t0 = time.time()
    countdown = 5
    while time.time() - t0 < countdown:
        ret, frame = cap.read()
        cv2.putText(frame, f'{countdown - int(time.time() - t0)}', org, font,  
                    fontScale, color, thickness, cv2.LINE_AA)). 
Adding in the display of the timer was not easy and I did not reslise how much detail needed to be provided in order for the output to be displayed. 
I have also added the code in to display the scores of both the user and the computer and the code to end the game when either the user or the computer has scored 3:
( if user_score == 3 or computer_score == 3:
        break)
and then when the game is ended the following code is displayed:
if user_score == 3:
    print("Congratulations! You won the game!")
elif computer_score == 3:
    print("Better luck next time. You lost.")

I am aware that some of the things I have done are different to what has been asked. However, this was more sense to me to do and I am still trying to get my head around python so I am really struggling to get everything perfectly correct. 
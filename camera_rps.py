import cv2 
import numpy as np
from keras.models import load_model
import random
import time

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Printing opening message and defining variables and scores.
print("Welcome to Rock-Paper-Scissors!")
options = ["rock", "paper", "scissors", "nothing"]
user_score = 0
computer_score= 0

# Get_winner
while True:
    if user_score == 3 or computer_score == 3:
        break
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalise the image
    data[0] = normalized_image
    prediction = model.predict(data)
    prediction_label = np.argmax(prediction)
    user_choice = options[prediction_label]

    # Display_countdown
    font = cv2.FONT_HERSHEY_SIMPLEX 
    org = (50, 50) 
    fontScale = 1
    color = (255, 0, 0) 
    thickness = 2
  
    t0 = time.time()
    countdown = 5
    while time.time() - t0 < countdown:
        ret, frame = cap.read()
        cv2.putText(frame, f'{countdown - int(time.time() - t0)}', org, font,  
                    fontScale, color, thickness, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    
    computer_choice = random.choice(options)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
        user_score +=1
    elif user_choice == "nothing":
        print("You chose nothing")
    else:
        print("You lost")
        computer_score +=1
  
    print(f"current score: You {user_score} - Computer {computer_score}")

cap.release()
cv2.destroyAllWindows()

# Display winner
if user_score == 3:
    print("Congratulations! You won the game!")
elif computer_score == 3:
    print("Better luck next time. You lost.")

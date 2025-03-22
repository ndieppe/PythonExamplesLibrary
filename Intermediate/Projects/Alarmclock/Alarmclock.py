import time #to count time
import datetime #to get current time
import pygame #purely for sound effects
import os
#function to set the alarm
def set_alarm(alarm_time):
    print(f"Alarm set for: {alarm_time}")
    sound_file = "alarm_sound.mp3" #defining the sound file


if __name__ == "__main__":
    alarm_time = input("Enter the alarm time in the format HH:MM:SS: ")
    set_alarm(alarm_time)
    is_running = True

    while is_running == True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("Wake up!")
            is_running = False
            pygame.mixer.init()
            pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "alarm_sound.mp3"))
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                time.sleep(1)   #wait for the sound to finish playing
        time.sleep(1)

#TODO: make it show in new window
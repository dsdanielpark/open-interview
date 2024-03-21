import os
import random
import pygame
import threading
import time
from typing import List


class RandomQPlay:
    """
    A class to play MP3 files in a given directory randomly. Allows user interaction to skip to the next song or quit the playback.

    Attributes:
        directory (str): The directory path where MP3 files are located.
        next_song (bool): A flag to control the flow of songs, whether to skip to the next song or not.
    """

    def __init__(self, directory: str) -> None:
        """
        Initializes the MP3Player with the directory containing MP3 files.

        Parameters:
            directory (str): The directory path where MP3 files are located.
        """
        self.directory = directory
        self.next_song = False
        pygame.mixer.init()

    def find_mp3_files(self) -> List[str]:
        """
        Finds all MP3 files in the directory that contain the word 'question' in their filenames.

        Returns:
            List[str]: A list of paths to the MP3 files.
        """
        mp3_files = []
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                if file.endswith(".mp3") and "question" in file:
                    mp3_files.append(os.path.join(root, file))
        return mp3_files

    def play_mp3_file(self, file_path: str) -> None:
        """
        Loads and plays a single MP3 file.

        Parameters:
            file_path (str): The path to the MP3 file to be played.
        """
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

    def input_listener(self) -> None:
        """
        Listens for user input to either quit the playback ('q') or skip to the next song ('n').
        """
        while True:
            user_input = input()
            if user_input.strip().lower() == "q":
                pygame.mixer.music.stop()
                return
            elif user_input.strip().lower() == "n":
                pygame.mixer.music.stop()
                self.next_song = True
                return

    def play_random_mp3(self) -> None:
        """
        Plays MP3 files found in the directory randomly. Allows skipping to the next song or quitting via user input.
        """
        print(
            "Press 'q' to quit the process, 'n' to skip to the next MP3. It plays 'question.mp3' files randomly from the folder. Although set to a 2-minute interval, pressing 'n' immediately plays the next question."
        )
        mp3_files = self.find_mp3_files()
        random.shuffle(mp3_files)

        for mp3_file in mp3_files:
            self.next_song = False
            print(f"Now playing: {mp3_file}")
            self.play_mp3_file(mp3_file)

            listener_thread = threading.Thread(target=self.input_listener)
            listener_thread.start()

            while pygame.mixer.music.get_busy() and not self.next_song:
                time.sleep(0.1)

            listener_thread.join()

            if self.next_song:
                continue
            if not pygame.mixer.music.get_busy():
                break

        print("Finished playing all files or stopped by user.")

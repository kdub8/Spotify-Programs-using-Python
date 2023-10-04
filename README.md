# Spotify-Programs-using-Python

In this repository, I have created a compilation of concise Python 3 scripts capable of retrieving the top 10 songs by any specified artist or streaming songs from Spotify on your operating system.

# Spotify Song Search & Play Automation

## Overview

This Python script automates the process of searching for a song on Spotify. It uses the `pyautogui` library to simulate keyboard inputs and interacts with the Spotify desktop application to perform a song search.

## How It Works

1. The script prompts the user to enter the name of the song (and optionally, the artist's name).

2. It waits for 2 seconds to give the user time to switch to the Spotify application.

3. The script launches the Spotify application using the `os.system` command.

4. After launching Spotify, it waits for 6 seconds to allow the application to fully load.

5. The script simulates the keyboard shortcut `Ctrl + L` to focus on the search bar in Spotify.

6. It types the song name (and artist) into the search bar with a specified typing interval of 0.1 seconds between characters.

7. To execute the search, the script simulates pressing the `Enter` key.

8. Additional key presses (`Page Down`, `Tab`, `Enter`, `Enter`) are used to navigate to and select the desired search result if needed.

## Usage

1. Ensure you have Python installed on your system.

2. Install the `pyautogui` library if you haven't already. You can install it using `pip`:

   ```
   pip install pyautogui
   ```

3. Run the script. It will prompt you to enter the name of the song (and artist, if desired).

4. Switch to the Spotify application within the 2-second timeframe.

5. The script will automate the song search process and select the desired result.

6. Enjoy listening to the song on Spotify!

## Notes

- This script is designed to work with the Spotify desktop application on a Windows system. If you are using a different operating system or Spotify version, you may need to make adjustments to the script.

- Be cautious when automating interactions with applications, and ensure you are complying with Spotify's terms of service and any applicable laws and regulations.

- The script may require adjustments or updates if the Spotify application's user interface changes in the future.


# Spotify Artist's Top 10 Songs Finder

## Overview

This Python script allows users to find the top 10 songs of a specific artist on Spotify. It utilizes the Spotify Web API to search for an artist and retrieve their top tracks. The script handles authentication using client credentials and provides a user-friendly interface for inputting the artist's name.

## Prerequisites

- You need to have a Spotify Developer account to obtain the `CLIENT_ID` and `CLIENT_SECRET` required for authentication. These credentials are used to obtain an access token from the Spotify API.

- Ensure you have Python installed on your system.

## Installation

1. Clone this repository or download the script to your local machine.

2. Install the required Python libraries using `pip`:

   ```
   pip install dotenv requests
   ```

3. Create a `.env` file in the same directory as the script and add your Spotify API credentials:

   ```
   CLIENT_ID=your_client_id
   CLIENT_SECRET=your_client_secret
   ```

## Usage

1. Run the script using Python:

   ```
   python spotify_top_songs.py
   ```

2. The script will prompt you to enter the name of the artist for whom you want to find the top 10 songs.

3. After providing the artist's name, the script will make requests to the Spotify API to retrieve the artist's information and top songs.

4. The top 10 songs of the artist will be displayed in the console, including their names.

5. Enjoy discovering the artist's most popular tracks on Spotify!

## Notes

- This script is designed to work with the Spotify Web API and assumes that the artist name you provide exists on Spotify.

- Be cautious when handling API credentials and ensure you keep them secure. Do not share your credentials with others.

- The Spotify API access token obtained by this script is limited in scope to only retrieve artist and track information.

- Make sure to comply with Spotify's terms of service and API usage policies when using this script.

- The script may require updates if the Spotify API or its endpoints change in the future.

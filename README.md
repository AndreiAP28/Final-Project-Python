# Simple Music Library App

### Video Demo: [video link](https://youtu.be/4GpASSMRmPI)

## Project Description

This project recreates the backend of major music streaming platforms like **Apple Music**, **Spotify**, and **Soundcloud**, without using any of their APIs. Each song is added manually using user input, and all data is stored in CSV files, including the playlists.

### Project Structure (files):

- project.py
- test_project.py
- requirements.txt
- music_library.csv
- {name of the created playlist}.csv
- README.md

## App's Features

- **Add a song to the library**: Users can add new songs to their library by providing the title, artist, and album information.

- **Search for a song**: Users can search for a specific song in their library using the title, artist, and album information.

- **Create a playlist**: Users can create playlists to organize their music collection.

- **View playlists**: Users can view all the playlists they have created.

- **Add songs to a playlist**: Users can add songs from their library to a specific playlist.

- **View playlist's songs**: Users can view the songs contained within a specific playlist.

- **Exit**: Users can exit the application.

## About Libraries

_**TABULATE**_: This module is used for printing a variety of tables, including smart column alignment and configurable number formatting. ([Read more](https://pypi.org/project/tabulate/))

_**PYFIGLET**_: This module takes ASCII text and renders it in ASCII art fonts (like the title above, which is the 'block' font). ([Read more](https://pypi.org/project/pyfiglet/))

## Importing & Installing the Libraries

Before running the application, make sure you have the required dependencies installed. You can install them using pip:

```bash
pip install tabulate
```

```bash
pip install pyfiglet
```

Right after that the libaries are ready for being imported and used:

```python
from tabulate import tabulate
import pyfiglet
import csv
import re
```

## Usage

```bash
python project.py
```

```
            _____ _                 _       ___  ___          _
           /  ___(_)               | |      |  \/  |         (_)
           \ `--. _ _ __ ___  _ __ | | ___  | .  . |_   _ ___ _  ___
            `--. \ | '_ ` _ \| '_ \| |/ _ \ | |\/| | | | / __| |/ __|
           /\__/ / | | | | | | |_) | |  __/ | |  | | |_| \__ \ | (__
           \____/|_|_| |_| |_| .__/|_|\___| \_|  |_/\__,_|___/_|\___|
                             | |
                             |_|
             _     _ _                             ___
            | |   (_) |                           / _ \
            | |    _| |__  _ __ __ _ _ __ _   _  / /_\ \_ __  _ __
            | |   | | '_ \| '__/ _` | '__| | | | |  _  | '_ \| '_ \
            | |___| | |_) | | | (_| | |  | |_| | | | | | |_) | |_) |
            \_____/_|_.__/|_|  \__,_|_|   \__, | \_| |_/ .__/| .__/
                                           __/ |       | |   | |
                                          |___/        |_|   |_|

+----------+---------------------------+
|   Option | Description               |
+==========+===========================+
|        1 | Add a song in library     |
+----------+---------------------------+
|        2 | Search for a song         |
+----------+---------------------------+
|        3 | Create a playlist         |
+----------+---------------------------+
|        4 | View playlists            |
+----------+---------------------------+
|        5 | Add songs into a playlist |
+----------+---------------------------+
|        6 | View playlist's songs     |
+----------+---------------------------+
|        7 | Exit                      |
+----------+---------------------------+
Enter the number that match your choice:
```

Depending on your preferences, choose the option that matches your action.

if you enter either a number that is not in the range 1-7, or an input that is not a number, an error will be displayed.

Per example if you select option no. 6, depends on what playlists are created at the moment and which songs belongs to those playlists, it will be displayed the followings:

```
+------+-----------------------+
|   ID | Name                  |
+======+=======================+
|    1 | Feels Harder n Harder |
+------+-----------------------+
|    2 | random_Playlist       |
+------+-----------------------+
Choose the playlist by typing its ID:
```

I will choose "Feels Harder n Harder" playlist by typing 1:

```
Skeletons - Travis Scott
Mask Off - Future
No Role Modelz - J. Cole
Pornography - Travis Scott
```

**This was just an example, I will let you the opportunity to test the rest of the app! :)**
**ENJOY EXPLORING THE APP! :)**

## Social Media

- **EdX**: AndreiAP_28
- **GitHub**: AndreiAP28

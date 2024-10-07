from tabulate import tabulate
import pyfiglet
import csv
import re


class Song():
    def __init__(self, title, artist, album):
        self._title =  title
        self._artist = artist
        self._album = album

    @property
    def artist(self):
        return self._artist
    
    @artist.setter
    def artist(self, _):
        try:
            raise AttributeError
        except AttributeError:
            print("ARTIST CANNOT BE CHANGED ONCE SET.")
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, _):
        try:
            raise AttributeError
        except AttributeError:
            print("TITLE CANNOT BE CHANGED ONCE SET.")
    
    @property
    def album(self):
        return self._album
    
    @album.setter
    def album(self, _):
        try:
            raise AttributeError
        except AttributeError:
            print("ALBUM CANNOT BE CHANGED ONCE SET.")



class Playlist():
    def __init__(self, name):
        self.name = name
        self.songs = []

    def get_name(self):
        return self.name

    def add_song(self, song):
        for s in self.songs:
            if song.title == s.title and song.artist == s.artist and song.album == s.album:
                print(f"Song is already in {self.name} playlist.")
                break
        self.songs.append(song)
    
    def remove_song(self, title):
        if title in self.songs:
            self.songs.remove(title)
        else:
            print(f"{title} is not in {self.name} playlist.")
        
    def search_song(self, keyword1, keyword2, keyword3):
        found_song = []
        for song in self.songs:
            if keyword1 == song.title and keyword2 == song.artist and keyword3 == song.album:
                found_song.append(song)
        if len(found_song) == 0:
            return True
        else:
            return False    
        
    @property
    def show(self):
        return self.songs

class Library():
    def __init__(self):
        self.db_songs = []

    def add_song(self, song):
        self.db_songs.append(song)
    

    def search_song(self, keyword1, keyword2, keyword3):
        found_song = []
        for song in self.db_songs:
            if keyword1 == song.title and keyword2 == song.artist and \
                 keyword3 == song.album:
                found_song.append(song)
        if len(found_song) == 0:
            return "Song cannot be found in the library."
        else:
            return found_song    
    

    def show_library(self):
        return self.db_songs             
        

def printing_options(library_database, all_playlists):
    options = [
        {"Option": 1, "Description": "Add a song in library"},
        {"Option": 2, "Description": "Search for a song"},
        {"Option": 3, "Description": "Create a playlist"},
        {"Option": 4, "Description": "View playlists"},
        {"Option": 5, "Description": "Add songs into a playlist"},
        {"Option": 6, "Description": "View playlist's songs"},
        {"Option": 7, "Description": "Exit"}
    ]

    table_options =  tabulate(options,headers = "keys", tablefmt = "grid")
    while True:
            print(table_options)
            user_input = input("Enter the number that match your choice: ")

            if user_input.isdigit():
                user_input = int(user_input)
                if user_input == 1:
                    add_song_option(library_database)
                elif user_input == 2:
                    search_song_option(all_playlists, library_database)
                elif user_input == 3:
                    create_playlist_option(all_playlists, library_database)
                elif user_input == 4:
                    view_playlists_option(all_playlists)
                elif user_input == 5:
                    add_song_to_playlist_option(all_playlists, library_database)
                elif user_input == 6:
                    view_playlist_songs_option(all_playlists)
                elif user_input == 7:
                    print(pyfiglet.figlet_format("The program is SHUTTING DOWN...", justify='center', font = "doom"))
                    break
                else:
                    print("Invalid option. Please enter a number between 1 and 7.")
            else:
                print("Invalid input.Please add a number.")



#FUNCTIONS FOR APP OPTIONS

def add_song_option(library_database):
    while True:
        print("Type the name of the song following by the artist, and the album which belongs to; ")
        print("Example: Yosemite-Travis Scott-Astroworld(if the song is a single, simply write 'Single'): ")
        song_details = input()
        pattern = r'^[\w\d\s\$%@!\^&*().,#-]+-[\w\d\s\$%@!\^&*().,#-]+-(?:[\w\d\s\$%@!\^&*().,#-]+|Single)$'
        validation = re.search(pattern, song_details, flags = re.IGNORECASE)
        if not validation:
            print("Invalid input format. Please follow the specified format.")
        else:
            break

    song_name, artist, album = map(str.strip, song_details.split("-"))
    if album.lower() == "single":
        album = None
    check_db = library_database.search_song(song_name, artist, album)
    if not isinstance(check_db, list):
        song = Song(song_name, artist, album)
        library_database.add_song(song)
    else:
        print(f"{song_name}-{artist} already exist.")





def search_song_option(all_playlists, library_database):
    while True:
        print("Type the name of the song following by the artist, and the album which belongs to; ")
        print("Example: Yosemite-Travis Scott-Astroworld(if the song is a single, simply write 'Single'): ")
        searchingsong_input = input("What song are you looking for?: ")
        pattern = r'^[\w\d\s\$%@!\^&*().,#-]+-[\w\d\s\$%@!\^&*().,#-]+-(?:[\w\d\s\$%@!\^&*().,#-]+|Single)$'
        validation = re.search(pattern, searchingsong_input, flags = re.IGNORECASE)
        if not validation:
            print("Invalid input format. Please follow the specified format.")
        else:
            break

    Isong_title, Isong_artist, Isong_album = searchingsong_input.split("-")
    if Isong_album.lower() == "single":
        Isong_album = None
    search_results = library_database.search_song(Isong_title, Isong_artist, Isong_album)
    if not isinstance(search_results, list):
        print(search_results)
        return search_results
    else:
        add_to_playlist = input("Do you want to add this song to one of your playlists?(yes/no): ")
        if add_to_playlist.lower() in ['yes', 'y']:
            if view_playlists_option(all_playlists) == False:
                return False
            
            playlist_id = input("Choose the playlist by typing its ID: ")
            while True:
                try:
                    playlist_id = int(playlist_id)
                    if playlist_id not in range(1, len(all_playlists) + 1):
                        raise ValueError(f"Invalid playlist ID. Choose an ID between 1 and {len(all_playlists)}")
                    break
                except ValueError as VE:
                    print("Invalid Input. Please enter a valid playlist ID.")
                    continue
        
            selected_playlist = all_playlists[int(playlist_id) - 1]
            check_exist = selected_playlist.search_song(Isong_title, Isong_artist, Isong_album)
            if check_exist == True:
                selected_playlist.add_song(search_results[0])
                playlist_into_csv(selected_playlist, selected_playlist.name)
                return True
            else:
                print(f"{Isong_title} - {Isong_artist} is already in {selected_playlist.name}")
                return f"{Isong_title} - {Isong_artist} is already in {selected_playlist.name}"
        elif add_to_playlist.lower() in ['no','n']:
            pass
        else:
            print("Invalid input!")

    
                
                
                

   


def create_playlist_option(all_playlists, library_database):
    playlist_name = input("Choose a name for your playlist: ")
    for playlist in all_playlists:
        if playlist.name == playlist_name:
            print(f"{playlist_name} already exists.")
            return 
    
    user_playlist = Playlist(playlist_name)
    all_playlists.append(user_playlist)
    playlist_into_csv(user_playlist, playlist_name)

    while True:
        user_choice_add_song = input(f"Do you want to add a song in {playlist_name}?(yes/no): ")
        if user_choice_add_song.lower() in ["no", "n"]:
            break
        elif user_choice_add_song.lower() in ["yes", "y"]:
            print("Type the name of the song following by the artist, and the album which belongs to; ")
            print("Example: Yosemite-Travis Scott-Astroworld(if the song is a single, simply write 'Single'): ")
            song_details = input()
            pattern = r'^[\w\d\s\$%@!\^&*().,#-]+-[\w\d\s\$%@!\^&*().,#-]+-(?:[\w\d\s\$%@!\^&*().,#-]+|Single)$'
            validation = re.search(pattern, song_details, flags = re.IGNORECASE)
            if validation == None:
                print("Invalid input format. Please follow the specified format.")
                continue
            
            song_name, artist, album = map(str.strip, song_details.split("-"))
            if album.lower() == "single":
                album = None

            search_results = library_database.search_song(song_name, artist, album)
            if not isinstance(search_results, str):
                song = search_results[0]
                if user_playlist.search_song(song.title, song.artist, song.album):      
                    user_playlist.add_song(song)
                    playlist_into_csv(user_playlist, playlist_name)
                else:
                    print(f"{song.title} - {song.artist} is already in {playlist_name}.")  
            else:
                print("Invalid option. Could you try again by using YES/NO?: ")
    




def view_playlists_option(all_playlists):
    all_titles = []
    
    if len(all_playlists) == 0:
        print("There are no playlists at the moment!")
        return False
    
    for playlist in all_playlists:
        all_titles.append(playlist.get_name())
    all_titles = list(enumerate(all_titles, start = 1))
    print(tabulate(all_titles, headers = ["ID", "Name"], tablefmt = "grid"))
    




def add_song_to_playlist_option(all_playlists, library_database):
    if view_playlists_option(all_playlists) == False:
        return
    
    exit = False
    while not exit:
        playlist_id = input("Choose the playlists by typing its ID: ")
        try:
            playlist_id = int(playlist_id)
            if playlist_id not in range(1, len(all_playlists) + 1):
                raise ValueError(f"Invalid playlist ID. Choose between 1 and {len(all_playlists)}.")
        except ValueError as VE:
            print(VE)
            continue
            
        
        selected_playlist = all_playlists[int(playlist_id) - 1]
        while True:
            print("Type the name of the song following by the artist, and the album which belongs to; ")
            print("If you want to stop the process simply type 'STOP'")
            print("Example: Yosemite-Travis Scott-Astroworld(if the song is a single, simply write 'Single'): ")
            song_details = input("Song: ")
            if song_details.lower() == "stop":
                exit = True
                break

            pattern =  r'^[\w\d\s\$%@!\^&*().,#-]+-[\w\d\s\$%@!\^&*().,#-]+-(?:[\w\d\s\$%@!\^&*().,#-]+|Single)$'
            validation = re.search(pattern, song_details, flags = re.IGNORECASE)
            if validation == None:
                print("Invalid input format. Please follow the specified format.")
                continue
            song_name, artist, album = map(str.strip, song_details.split("-"))
            if album.lower() == "single":
                album = None

            search_results = library_database.search_song(song_name, artist, album)
            if not isinstance(search_results,list):
                print(search_results)
            else:
                song = search_results[0]
                if selected_playlist.search_song(song_name, artist, album) == True:
                    selected_playlist.add_song(song)
                    playlist_into_csv(selected_playlist, selected_playlist.name)
                    print(f"{song_name} - {artist} was successfully added to {selected_playlist.name}.")
                else:
                    print(f"{song_name} - {artist} is already in {selected_playlist.name}.")
                    return f"{song_name} - {artist} is already in {selected_playlist.name}."
                   
               



def view_playlist_songs_option(all_playlists):
    if view_playlists_option(all_playlists) == False:
        return
    while True:
        playlist_id = input("Choose the playlist by typing its ID: ")
        try:
            playlist_id = int(playlist_id)
            if playlist_id not in range(1, len(all_playlists) + 1):
                raise ValueError(f"Invalid ID. Choose a ID between 1 and {len(all_playlists)}")
        except ValueError as VE:
            print(VE)
            continue
    
        selected_playlist = all_playlists[int(playlist_id) - 1]
        if len(selected_playlist.show) == 0:
            print(f"{selected_playlist.name} is EMPTY.")
            break

        for song in selected_playlist.show:
            print(f"{song.title} - {song.artist}")
        break
#END OF THE FUNCTIONS FOR THE APP OPTIONS


#FUNCTIONS FOR SAVING/LOADING THE DATA INTO/FROM CSV

def library_into_csv(library_database):
    with open("playlists/music_library.csv", 'w', newline = '') as file:
        fieldnames = ['Title', 'Artist', 'Album']
        writer = csv.DictWriter(file, fieldnames= fieldnames)
    
        if file.tell() == 0:
            writer.writeheader()

        for song in library_database.show_library():
            writer.writerow({'Title': song.title, 'Artist': song.artist, 'Album': song.album})
            




def playlist_into_csv(playlist, filename):
    with open(f"playlists/{filename}.csv", 'w', newline = '') as file:
        fieldnames = ['Title', 'Artist', 'Album']
        writer = csv.DictWriter(file, fieldnames = fieldnames)

        if file.tell() == 0:
            writer.writeheader()

        for song in playlist.show:
            writer.writerow({'Title': song.title, 'Artist': song.artist, 'Album': song.album})



def load_library_from_csv(library_database):
    with open("playlists/music_library.csv", 'r') as file:
        if file.readline().strip() == "":
            return 
        
        file.seek(0)
        reader = csv.DictReader(file, fieldnames = ['Title' ,'Artist', 'Album'])

        next(reader)

        for row in reader:
            if row['Album'] == '':
                row['Album'] = None
            song = Song(row['Title'], row['Artist'], row['Album'])
            library_database.add_song(song)





def save_playlist_names_into_csv(all_playlists):
    with open("playlists/playlist_names.csv", 'w', newline= '') as file:
        writer = csv.writer(file)
        for playlist in all_playlists:
            writer.writerow([playlist.name])



def load_playlists_names_from_csv(names):
    with open("playlists/playlist_names.csv", 'r') as file:
        first_line = file.readline().strip()
        if not first_line:
            return "empty"
        
        file.seek(0)

        reader = csv.reader(file)
        for row in reader:
            for name in row:
                names.append(name.strip())



def load_playlists_from_csv(all_playlists):
    playlists_names = []
    load_playlists_names_from_csv(playlists_names)
    if load_playlists_names_from_csv == "empty":
        return 
    
    for name in playlists_names:
        playlist = Playlist(name)
        try:
            with open(f"playlists/{name}.csv", 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['Album'] == '':
                        row['Album'] = None
                    song = Song(row['Title'], row['Artist'], row['Album'])
                    playlist.add_song(song)
        except FileNotFoundError:
            raise FileNotFoundError(f"There is no playlist '{name}'.csv")
        all_playlists.append(playlist)




def main(): 
    library_database = Library()
    all_playlists = []
    
    load_library_from_csv(library_database)
    load_playlists_from_csv(all_playlists)

    
    print(pyfiglet.figlet_format("Simple Music Library App", justify='center', font = "doom"))
    printing_options(library_database, all_playlists)
    
    save_playlist_names_into_csv(all_playlists)
    library_into_csv(library_database)
    
   





if __name__ == "__main__":
    main()
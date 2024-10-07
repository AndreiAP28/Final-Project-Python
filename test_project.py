import warnings
warnings.filterwarnings('ignore', category = DeprecationWarning)
import pytest
import csv
from project import (
    Library,
    Playlist,
    Song,
    search_song_option,
    view_playlists_option,
    add_song_to_playlist_option
)


@pytest.fixture
def library_database():
    return Library()

@pytest.fixture
def empty_playlist():
    return Playlist("Empty Playlist")

@pytest.fixture
def mock_input(monkeypatch):
    mock_input = []

    def mock_input_prompt(prompt):
        nonlocal mock_input
        print(prompt)
        if len(mock_input) == 0:
            raise ValueError("Mock input is empty")
        return mock_input.pop(0)

    # Apply the monkeypatch to replace the input() function
    monkeypatch.setattr('builtins.input', mock_input_prompt)

    return mock_input

# Define test functions
def test_search_song_option(mock_input, monkeypatch, library_database, empty_playlist):
    mock_input.extend(["Yosemite-Travis Scott-Astroworld", "yes", "1"])
    assert search_song_option([empty_playlist], library_database) == "Song cannot be found in the library."

    library_database.add_song(Song('Yosemite', 'Travis Scott', 'Astroworld'))
    mock_input.extend(["Yosemite-Travis Scott/-Astroworld", "yes", "1"])
    assert search_song_option([empty_playlist], library_database) == True
   
    

def test_search_song_option_invalid_input(mock_input, monkeypatch, capsys, library_database):
    mock_input.extend(["invalid input", "Yosemite-Travis Scott-Astroworld", "yes", "1"])
    search_song_option([], library_database)

    captured = capsys.readouterr()
    output = captured.out.strip()

    assert "Invalid input format. Please follow the specified format." in output

def test_search_song_option_no_playlists(mock_input, monkeypatch, capsys, library_database):
    library_database.add_song(Song("Yosemite", "Travis Scott", "Astroworld"))
    mock_input.extend(["Yosemite-Travis Scott-Astroworld", "yes"])
    result = search_song_option([], library_database)

    assert result == False

    captured = capsys.readouterr()
    output = captured.out.strip()

    assert "There are no playlists at the moment!" in output

def test_view_playlists_option_no_playlists(capsys):
    result = view_playlists_option([])
    assert result == False

    captured = capsys.readouterr()
    output = captured.out.strip()

    assert "There are no playlists at the moment!" in output


def test_add_song_to_playlist_option(mock_input, monkeypatch, library_database, empty_playlist):

    song1 = Song("Yosemite", "Travis Scott", "Astroworld")
    library_database.add_song(song1)
    #empty_playlist.add_song(Song("Yosemite", "Travis Scott", "Astroworld"))
    # Mock user input
    mock_input.extend(["1", "Yosemite-Travis Scott-Astroworld", "stop"])

    # Call the function under test
    add_song_to_playlist_option([empty_playlist], library_database)

    # Assert that the song was added to the playlist
    assert empty_playlist.show[0] == song1

    mock_input.extend(["1", "Yosemite-Travis Scott-Astroworld", "stop"])
    output = add_song_to_playlist_option([empty_playlist], library_database)
    assert "Yosemite - Travis Scott is already in Empty Playlist." in output



'''
def test_playlist_into_csv(tmp_path):
    # Setup - create a playlist and add a song to it
    playlist = Playlist("Test Playlist")
    playlist.add_song(Song("Yosemite", "Travis Scott", "Astroworld"))

    # Call the function under test
    csv_file_path = tmp_path/"test_playlist"
    playlist_into_csv(playlist, csv_file_path)

    # Read the content of the CSV file
    with open(csv_file_path.with_suffix(".csv"), 'r') as file:
        reader = csv.reader(file)
        content = list(reader)

    # Assert the correctness of the data
    expected_content = [["Title", "Artist", "Album"],
                        ["Yosemite", "Travis Scott", "Astroworld"]]
    assert content == expected_content
'''
"""
Jacen LeCompte
12/16/20
Getting your genre of video with GUI
"""


import genre as genre
import self as self

# noinspection PyUnresolvedReferences
import tk as tk

import Video_Genre_Generator as sg
import genres as genres
from tkinter import *
from random import randint

root: Tk = Tk()
root.title('Figure Out Your Video Genre!')
root.iconbitmap('c:/gui/trophy.ico')
root.geometry("400x400")
root.configure(bg="#53b828",)


def pick():
    # 10 genres
    entries = ['Music', 'Gaming', 'Cooking', 'Movie', 'Art', 'Sports', 'Health', 'Vlog', 'Science', 'Comedy']

    # convert genres to a set
    entries_set = set(entries)
    # convert back to the list = 10
    unique_entries = list(entries_set)

    # create the genre list
    our_number = len(unique_entries) - 1
    # create a random genre for video to watch
    random = randint(0, our_number)

    genrelabel = Label(root, text=unique_entries[random], bg="#53b828", font=("Verdana", 18))
    genrelabel.pack(pady=50)


toplabel = Label(root, text="Video Genre Generator!", bg="#53b828",  font=("Verdana", 24))
toplabel.pack(pady=20)

genreButton = Button(root, text="Reveal video's genre!", bg="#53b828", activebackground='#53b828',
                     font=("Verdana", 24), command=pick)
genreButton.pack(pady=20)

root.mainloop()


def def_init_() -> object:
    pass


def length():
    pass


class VideoGenre:
    # Video genre will work for a linked list
    def __init__(self):
        pass

    def_init_()
    self.genres = genres  # of genres to be showed
    self.length = length  # of time the video will be about
    self.nxt = None  # used to get the next video in the queue


class ReturnQueue:
    def __init__(self):
        pass

    def_init_()
    self.genres_size = 0  # this is for the queue size
    self.youtube_front = None  # The place that the videos will play from


def make_return(individual, video_genre):

    """
    I made this as my enqueue. :param self: :param video_genre: this is the video genre which needs to be enqueued
    :return: this is when nothing is needed to be return but only the method used is increased with the queue size
    and will enqueue what genre is shown or passed
    """
    video_genre = "time" if video_genre.lower() == "time" else \
        "youtube"
    front = getattr(individual, f'{length}_front')
    if front is None:
        setattr(individual, f'{length}_front', video_genre)
    else:
        setattr(individual, f'{length}_front', individual.set_front(front, video_genre))
    individual.queue_size += 1


def set_front(one, two):
    """
    I made this so the front of my queue is unique
    """
    if one is None:
        return two
    if two is None:
        return one
    if len(one.video) < len(two.video):
        temp = one
        one.nxt = self.set_front(one.nxt, two)
    else:
        temp = two
        two.nxt = self.set_front(one, two.nxt)
    return temp


def return_all(personal):
    """
    :param personal:
    that is used a lot in the GUI implementation) :return: Must return the genres that the user has enqueued over time
    """
    if not length:
        youtube_return = personal.return_all("youtube")
        time_return = personal.return_all("time")
        return youtube_return + time_return
    my_list = []
    types = "time" if length.lower() == "time" else "youtube"
    while getattr(personal, f'{length}_front'):
        my_list.append(personal.next_return(types))
    return my_list


def nxt_return(personal):
    """
    :param personal:
    :return: goes back to the front of the queue
    """
    if not length:
        youtube_return = personal.return_all("youtube")
        time_return = personal.return_all("time")
        return [youtube_return + time_return]
    front = getattr(personal, f'{genre}_front').nxt
    current = front
    nx = getattr(personal, f'{genre}_front').nxt
    current.nxt = None
    setattr(personal, f'{genre}_front', nx)
    return current.genres


def amt_of_genres(personal):
    # method was just for testing attributes that will later show up again
    return f'{personal, sg.queue_size} Genres that have been produced for the videos'


class GenreReturn(object):
    pass


if '_name_' == '_main_':
    # just want to show the genre
    return_queue = ReturnQueue()
    # Theme
    sg.theme('#53b828')
    # Layout
    layout = [[sg.Text('Please input your video genre (Only one genre)')],
              [sg.InputText(key="returned")],
              [sg.Radio('YouTube', "radio2", default=False, key="youtube")],
              [sg.Radio('Time', "radio2", default=False, key="time",)],
              [sg.Button('Enter')],
              [sg.Text('The current video genre'), sg.Text('The time length of the video')],
              [sg.Text('', key='time_text', size=(15, 11)),
               sg.Text('', key='youtube_text', size=(9, 11))],
              [sg.Button('Show everything'), sg.Button('Show YouTube', key="return_youtube"),
               sg.Button('Show the time', key="return_time")],
              [sg.Button('End')]]

    # Look of the Window
    window = sg.Window('Returns', layout, size=(270, 320))
    # reads the inputs
    while True:

        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            # used for the window for the user is closed by them
            break
        # if the user selects a genre of video then youtube will play that video and erase everything in boxes
        if event == 'Enter':
            if values['returned'] == '' or values['returned'] == '':
                sg.Popup('I need you to select only one genre', title='ERROR!')
                continue

            if values["youtube"]:
                # setting the genre to youtube since the radio is pressed and played there
                length = "YouTube"
                set_window = window.FindElement('Youtube_text')
                # this makes sure that the genre list and the text shows when searched on youtube
                if 'process' in set_window.get():
                    set_window.Update('')

                set_window.Update(f'{set_window.get()}\n{values["returned"]}')

            else:
                # set genre to time of the video
                length = "time"
                set_window = window.FindElement('time_text')
                # this makes sure that the genre list and the text shows when searched on youtube with the time
                if 'process' in set_window.get():
                    set_window.Update(f'{set_window.get()}\n{values["returned"]}')

            # variable is changed
            my_genre = GenreReturn()
            return_queue.make_return(my_genre)
            print(f'You have entered {values ["returned"]}')
            # text empty
            window.FindElement('returned').Update('')
        if event == 'return youtube':
            # return both time and youtube for the genre of video
            x = return_queue.return_youtube("YouTube")
            total_youtube = sum([len(r) for r in x])
            window.findelement('youtube_text').Update(f'{total_youtube}' f'YouTube returned' 'processed')

            if event == "return_time":
                # Return Youtube video genre
                x = return_queue.return_time("time")
                total_num_genres = sum([len(r) for r in x])
                window.FindElement('time_text').Update(f'{total_num_genres}' f'time returned' 'processed')
                # Fixed GUI
                window.Refresh()
            # No Window
            window.close()
            # once exited there is a new line
            input('Please press a key to continue')

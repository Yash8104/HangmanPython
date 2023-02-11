import random
import tkinter
from tkinter import *
from tkinter import font

import tkmacosx
from PIL import Image, ImageTk

import words_list


class App(Tk):

    def __init__(self):
        super().__init__()
        self.geometry('900x500')
        self.title("Hangman")
        self.frame_1 = tkinter.Frame(self)
        self.frame_1.pack(fill='both', expand=True)

    def load_logo(self):
        logo = Image.open('/Users/yashjain/Desktop/python projects/tkinter lectures gui/mini_project/images/logo.png')
        logo = logo.resize((500, 281))
        logo_in_tk = ImageTk.PhotoImage(logo)
        return logo_in_tk

    def load_hangman(self, state):

        if state == 6:
            hangman = Image.open('/Users/yashjain/Desktop/python projects/tkinter lectures gui/mini_project/images/hangman1.png')
        elif state == 5:
            hangman = Image.open('/Users/yashjain/Desktop/python projects/tkinter lectures gui/mini_project/images/hangman2.png')
        elif state == 4:
            hangman = Image.open('/Users/yashjain/Desktop/python projects/tkinter lectures gui/mini_project/images/hangman3.png')
        elif state == 3:
            hangman = Image.open('/Users/yashjain/Desktop/python projects/tkinter lectures gui/mini_project/images/hangman4.png')
        elif state == 2:
            hangman = Image.open('/Users/yashjain/Desktop/python projects/tkinter lectures gui/mini_project/images/hangman5.png')
        elif state == 1:
            hangman = Image.open('/Users/yashjain/Desktop/python projects/tkinter lectures gui/mini_project/images/hangman6.png')
        else:
            hangman = Image.open('/Users/yashjain/Desktop/python projects/tkinter lectures gui/mini_project/images/hangman0.png')

        hangman = hangman.resize((180, 180))
        hangman_in_tk = ImageTk.PhotoImage(hangman)
        return hangman_in_tk

    def make_starting_window(self):
        # making the starting window
        # frame 1 (inside frame_1)
        self.starting_window_frame_1 = tkinter.Frame(self.frame_1)
        self.starting_window_frame_1.pack()

        # image - logo (inside the starting_window_frame_1)
        image = self.load_logo()
        self.label_logo = tkinter.Label(self.starting_window_frame_1, image=image)
        self.label_logo.image = image
        self.label_logo.pack()

        # frame 2 (inside the frame_1)
        self.starting_window_frame_2 = tkinter.Frame(self.frame_1)
        self.starting_window_frame_2.pack(pady=30)

        # button - play (inside the starting_window_frame_2)

        self.starting_window_button_play = tkmacosx.Button(self.starting_window_frame_2)
        self.starting_window_button_play['text'] = "Start"
        self.starting_window_button_play['command'] = self.play_game
        self.starting_window_button_play['bg'] = "black"
        self.starting_window_button_play['fg'] = "white"
        self.starting_window_button_play['overbackground'] = 'red'
        self.starting_window_button_play['overforeground'] = 'black'
        self.starting_window_button_play['width'] = 150
        self.starting_window_button_play['borderless'] = 1
        self.starting_window_button_play['height'] = 50
        self.starting_window_button_play['font'] = font.Font(family='Helvetica', size=30, weight='bold', slant='roman')
        self.starting_window_button_play.grid(row=0, column=0, pady=10, padx=10)

        # button - quit (inside the starting_window_frame_2)

        self.starting_window_button_quit = tkmacosx.Button(self.starting_window_frame_2)
        self.starting_window_button_quit['text'] = "Quit"
        self.starting_window_button_quit['command'] = self.ending
        self.starting_window_button_quit['bg'] = "black"
        self.starting_window_button_quit['fg'] = 'white'
        self.starting_window_button_quit['overbackground'] = 'green'
        self.starting_window_button_quit['overforeground'] = 'black'
        self.starting_window_button_quit['width'] = 150
        self.starting_window_button_quit['height'] = 50
        self.starting_window_button_quit['font'] = font.Font(family='Helvetica', size=30, weight='bold', slant='roman')
        self.starting_window_button_quit.grid(row=0, column=1, pady=10, padx=10)

    def make_game_window(self):
        # making the game window with hangman and all

        # frame_0 for holding the exit button and the image (hangman)

        self.game_window_frame_0 = tkinter.Frame(self.frame_1)
        # self.game_window_frame_0['bg'] = 'red'
        # self.game_window_frame_0['width'] = 900
        # self.game_window_frame_0['height'] = 50
        self.game_window_frame_0.pack(fill='x', expand=True)

        # button - exit (to exit back)

        self.game_window_frame_0_button = tkmacosx.Button(self.game_window_frame_0)
        self.game_window_frame_0_button['text'] = ' ⃪ Exit'
        self.game_window_frame_0_button['bg'] = 'white'
        self.game_window_frame_0_button['bordercolor'] = 'black'
        self.game_window_frame_0_button['bd'] = 4
        self.game_window_frame_0_button['activebackground'] = 'red'
        self.game_window_frame_0_button['width'] = 120
        self.game_window_frame_0_button['height'] = 30
        self.game_window_frame_0_button['font'] = font.Font(family='SignPainter', size=30, weight='bold', slant='roman')
        self.game_window_frame_0_button['command'] = self.go_back
        # self.game_window_frame_0_button.place(x=0,y=0)
        self.game_window_frame_0_button.grid(row=0, column=0, stick=tkinter.NW)

        # string var - score

        self.var_score = tkinter.StringVar()
        self.var_score.set('Score : 0')

        # label - score

        self.label_score = tkinter.Label(self.game_window_frame_0)
        self.label_score['textvariable'] = self.var_score
        self.label_score['font'] = font.Font(family='Gill Sans', size=30, weight='bold')
        # self.label_score.place(x=375,y=5)
        self.label_score.grid(row=0, column=1, sticky=tkinter.N, padx=230)

        # frame_1

        self.game_window_frame_1 = tkinter.Frame(self.frame_1)
        self.game_window_frame_1.pack(pady=10)

        # image - hangman (in frame_1)
        image = self.load_hangman(state=0)
        self.label_hangman = tkinter.Label(self.game_window_frame_1, image=image)
        self.label_hangman.image = image
        self.label_hangman.grid(row=0, column=0)

        # frame_2 for holding the words

        self.game_window_frame_2 = tkinter.Frame(self.frame_1)
        self.game_window_frame_2.pack(pady=20)

        # string var - lives left

        self.var_lives_left = tkinter.StringVar()
        self.var_lives_left.set("Lives left : 0")

        # label - lives left (in frame_2)

        self.label_lives_left = tkinter.Label(self.game_window_frame_2)
        self.label_lives_left['textvariable'] = self.var_lives_left
        self.label_lives_left['font'] = ("Calibri", 15)
        self.label_lives_left.grid(row=0, column=0, pady=10)

        # string var - star words

        self.var_star_words = tkinter.StringVar()
        self.var_star_words.set('_ _ _')

        # label (______)

        self.label_star_words = tkinter.Label(self.game_window_frame_2)
        self.label_star_words['textvariable'] = self.var_star_words
        self.label_star_words['font'] = ("Calibri", 20)
        self.label_star_words.grid(row=1, column=0)

        # frame_3 for all the buttons

        self.game_window_frame_3 = tkinter.Frame(self.frame_1)
        self.game_window_frame_3.pack(pady=10)

        # buttons

        padx_button = 0
        pady_button = 0

        # button - a

        self.button_a = tkmacosx.Button(self.game_window_frame_3)
        self.button_a['bg'] = 'black'
        self.button_a['fg'] = 'white'
        self.button_a['text'] = 'A'
        self.button_a['font'] = font.Font(family='Gill Sans Light', size=15)
        self.button_a['width'] = 35
        self.button_a['height'] = 35

        self.button_a.grid(row=0, column=0, padx=padx_button, pady=pady_button)

        # button - b

        self.button_b = tkmacosx.Button(self.game_window_frame_3)
        self.button_b['bg'] = 'black'
        self.button_b['fg'] = 'white'
        self.button_b['text'] = 'B'
        self.button_b['font'] = font.Font(family='Gill Sans Light', size=15)
        self.button_b['width'] = 35
        self.button_b['height'] = 35

        self.button_b.grid(row=0, column=1, padx=padx_button, pady=pady_button)

        # button - c

        self.button_c = tkmacosx.Button(self.game_window_frame_3)
        self.button_c['bg'] = 'black'
        self.button_c['fg'] = 'white'
        self.button_c['text'] = 'C'
        self.button_c['font'] = font.Font(family='Gill Sans Light', size=15)
        self.button_c['width'] = 35
        self.button_c['height'] = 35

        self.button_c.grid(row=0, column=2, padx=padx_button, pady=pady_button)

        # button - d

        self.button_d = tkmacosx.Button(self.game_window_frame_3)
        self.button_d['bg'] = 'black'
        self.button_d['fg'] = 'white'
        self.button_d['text'] = 'D'
        self.button_d['font'] = font.Font(family='Gill Sans Light', size=15)
        self.button_d['width'] = 35
        self.button_d['height'] = 35

        self.button_d.grid(row=0, column=3, padx=padx_button, pady=pady_button)

        # button - e

        self.button_e = tkmacosx.Button(self.game_window_frame_3)
        self.button_e['bg'] = 'black'
        self.button_e['fg'] = 'white'
        self.button_e['text'] = 'E'
        self.button_e['font'] = font.Font(family='Gill Sans Light', size=15)
        self.button_e['width'] = 35
        self.button_e['height'] = 35

        self.button_e.grid(row=0, column=4, padx=padx_button, pady=pady_button)

        # button - f

        self.button_f = tkmacosx.Button(self.game_window_frame_3)
        self.button_f['bg'] = 'black'
        self.button_f['fg'] = 'white'
        self.button_f['text'] = 'F'
        self.button_f['font'] = font.Font(family='Gill Sans Light', size=15)
        self.button_f['width'] = 35
        self.button_f['height'] = 35

        self.button_f.grid(row=0, column=5, padx=padx_button, pady=pady_button)

        # button - g

        self.button_g = tkmacosx.Button(self.game_window_frame_3)
        self.button_g['bg'] = 'black'
        self.button_g['fg'] = 'white'
        self.button_g['text'] = 'G'
        self.button_g['font'] = font.Font(family='Gill Sans Light', size=15)
        self.button_g['width'] = 35
        self.button_g['height'] = 35

        self.button_g.grid(row=0, column=6, padx=padx_button, pady=pady_button)

        # button - h

        self.button_h = tkmacosx.Button(self.game_window_frame_3)
        self.button_h['bg'] = 'black'
        self.button_h['fg'] = 'white'
        self.button_h['text'] = 'H'
        self.button_h['font'] = font.Font(family='Gill Sans Light', size=15)
        self.button_h['width'] = 35
        self.button_h['height'] = 35

        self.button_h.grid(row=0, column=7, padx=padx_button, pady=pady_button)

        # button - i

        self.button_i = tkmacosx.Button(self.game_window_frame_3)
        self.button_i['bg'] = 'black'
        self.button_i['fg'] = 'white'
        self.button_i['text'] = 'I'
        self.button_i['font'] = font.Font(family='Gill Sans Light', size=15)
        self.button_i['width'] = 35
        self.button_i['height'] = 35

        self.button_i.grid(row=0, column=8, padx=padx_button, pady=pady_button)

        # button - j

        self.button_j = tkmacosx.Button(self.game_window_frame_3)
        self.button_j['bg'] = 'black'
        self.button_j['fg'] = 'white'
        self.button_j['text'] = 'J'
        self.button_j['font'] = font.Font(family='Gill Sans Light', size=15)
        self.button_j['width'] = 35
        self.button_j['height'] = 35

        self.button_j.grid(row=0, column=9, padx=padx_button, pady=pady_button)

        # button - k

        self.button_k = tkmacosx.Button(self.game_window_frame_3)
        self.button_k['bg'] = 'black'
        self.button_k['fg'] = 'white'
        self.button_k['text'] = 'K'
        self.button_k['font'] = font.Font(family='Gill Sans Light', size=15)
        self.button_k['width'] = 35
        self.button_k['height'] = 35

        self.button_k.grid(row=0, column=10, padx=padx_button, pady=pady_button)

        # button - l

        self.button_l = tkmacosx.Button(self.game_window_frame_3)
        self.button_l['bg'] = 'black'
        self.button_l['fg'] = 'white'
        self.button_l['text'] = 'L'
        self.button_l['font'] = font.Font(family='Gill Sans Light', size=15)
        self.button_l['width'] = 35
        self.button_l['height'] = 35

        self.button_l.grid(row=0, column=11, padx=padx_button, pady=pady_button)

        # button - m

        self.button_m = tkmacosx.Button(self.game_window_frame_3)
        self.button_m['bg'] = 'black'
        self.button_m['fg'] = 'white'
        self.button_m['text'] = 'M'
        self.button_m['font'] = font.Font(family='Gill Sans Light', size=15)
        self.button_m['width'] = 35
        self.button_m['height'] = 35

        self.button_m.grid(row=0, column=12, padx=padx_button, pady=pady_button)

        # button - n

        self.button_n = tkmacosx.Button(self.game_window_frame_3)
        self.button_n['bg'] = 'black'
        self.button_n['fg'] = 'white'
        self.button_n['text'] = 'N'
        self.button_n['font'] = font.Font(family='Gill Sans Light', size=15)
        self.button_n['width'] = 35
        self.button_n['height'] = 35
        # self.button_n['command'] = lambda : self.disable_button(button=self.button_n)

        self.button_n.grid(row=1, column=0, padx=padx_button, pady=pady_button)

        # button - o

        self.button_o = tkmacosx.Button(self.game_window_frame_3)
        self.button_o['bg'] = 'black'
        self.button_o['fg'] = 'white'
        self.button_o['text'] = 'O'
        self.button_o['font'] = font.Font(family='Gill Sans Light', size=15)
        self.button_o['width'] = 35
        self.button_o['height'] = 35

        self.button_o.grid(row=1, column=1, padx=padx_button, pady=pady_button)

        # button - p

        self.button_p = tkmacosx.Button(self.game_window_frame_3)
        self.button_p['bg'] = 'black'
        self.button_p['fg'] = 'white'
        self.button_p['text'] = 'P'
        self.button_p['font'] = font.Font(family='Gill Sans Light', size=15)
        self.button_p['width'] = 35
        self.button_p['height'] = 35

        self.button_p.grid(row=1, column=2, padx=padx_button, pady=pady_button)

        # button - q

        self.button_q = tkmacosx.Button(self.game_window_frame_3)
        self.button_q['bg'] = 'black'
        self.button_q['fg'] = 'white'
        self.button_q['text'] = 'Q'
        self.button_q['font'] = font.Font(family='Gill Sans Light', size=15)
        self.button_q['width'] = 35
        self.button_q['height'] = 35

        self.button_q.grid(row=1, column=3, padx=padx_button, pady=pady_button)

        # button - r

        self.button_r = tkmacosx.Button(self.game_window_frame_3)
        self.button_r['bg'] = 'black'
        self.button_r['fg'] = 'white'
        self.button_r['text'] = 'R'
        self.button_r['font'] = font.Font(family='Gill Sans Light', size=15)
        self.button_r['width'] = 35
        self.button_r['height'] = 35

        self.button_r.grid(row=1, column=4, padx=padx_button, pady=pady_button)

        # button - s

        self.button_s = tkmacosx.Button(self.game_window_frame_3)
        self.button_s['bg'] = 'black'
        self.button_s['fg'] = 'white'
        self.button_s['text'] = 'S'
        self.button_s['font'] = font.Font(family='Gill Sans Light', size=15)
        self.button_s['width'] = 35
        self.button_s['height'] = 35

        self.button_s.grid(row=1, column=5, padx=padx_button, pady=pady_button)

        # button - t

        self.button_t = tkmacosx.Button(self.game_window_frame_3)
        self.button_t['bg'] = 'black'
        self.button_t['fg'] = 'white'
        self.button_t['text'] = 'T'
        self.button_t['font'] = font.Font(family='Gill Sans Light', size=15)
        self.button_t['width'] = 35
        self.button_t['height'] = 35

        self.button_t.grid(row=1, column=6, padx=padx_button, pady=pady_button)

        # button - u

        self.button_u = tkmacosx.Button(self.game_window_frame_3)
        self.button_u['bg'] = 'black'
        self.button_u['fg'] = 'white'
        self.button_u['text'] = 'U'
        self.button_u['font'] = font.Font(family='Gill Sans Light', size=15)
        self.button_u['width'] = 35
        self.button_u['height'] = 35

        self.button_u.grid(row=1, column=7, padx=padx_button, pady=pady_button)

        # button - v

        self.button_v = tkmacosx.Button(self.game_window_frame_3)
        self.button_v['bg'] = 'black'
        self.button_v['fg'] = 'white'
        self.button_v['text'] = 'V'
        self.button_v['font'] = font.Font(family='Gill Sans Light', size=15)
        self.button_v['width'] = 35
        self.button_v['height'] = 35

        self.button_v.grid(row=1, column=8, padx=padx_button, pady=pady_button)

        # button - w

        self.button_w = tkmacosx.Button(self.game_window_frame_3)
        self.button_w['bg'] = 'black'
        self.button_w['fg'] = 'white'
        self.button_w['text'] = 'W'
        self.button_w['font'] = font.Font(family='Gill Sans Light', size=15)
        self.button_w['width'] = 35
        self.button_w['height'] = 35

        self.button_w.grid(row=1, column=9, padx=padx_button, pady=pady_button)

        # button - x

        self.button_x = tkmacosx.Button(self.game_window_frame_3)
        self.button_x['bg'] = 'black'
        self.button_x['fg'] = 'white'
        self.button_x['text'] = 'X'
        self.button_x['font'] = font.Font(family='Gill Sans Light', size=15)
        self.button_x['width'] = 35
        self.button_x['height'] = 35

        self.button_x.grid(row=1, column=10, padx=padx_button, pady=pady_button)

        # button - y

        self.button_y = tkmacosx.Button(self.game_window_frame_3)
        self.button_y['bg'] = 'black'
        self.button_y['fg'] = 'white'
        self.button_y['text'] = 'Y'
        self.button_y['font'] = font.Font(family='Gill Sans Light', size=15)
        self.button_y['width'] = 35
        self.button_y['height'] = 35

        self.button_y.grid(row=1, column=11, padx=padx_button, pady=pady_button)

        # button - z

        self.button_z = tkmacosx.Button(self.game_window_frame_3)
        self.button_z['bg'] = 'black'
        self.button_z['fg'] = 'white'
        self.button_z['text'] = 'Z'
        self.button_z['font'] = font.Font(family='Gill Sans Light', size=15)
        self.button_z['width'] = 35
        self.button_z['height'] = 35

        self.button_z.grid(row=1, column=12, padx=padx_button, pady=pady_button)

        # frame 4

        self.game_window_frame_4 = tkinter.Frame(self.frame_1)
        # self.game_window_frame_4['bg'] = 'red'
        self.game_window_frame_4.pack(fill='x', expand=True)
        self.game_window_frame_4.columnconfigure(0, weight=1)

    # def test(self,state):
    #
    #     if state == 7:
    #         state = 0
    #     image = self.load_hangman(state=state)
    #     self.label_hangman['image'] = image
    #     self.label_hangman.image = image
    #     self.update()
    #
    #     state = state + 1
    #     self.label_hangman.after(1000,lambda : self.test(state))

    def make_play_again_button(self):

        # play again button

        self.play_again_button = tkmacosx.Button(self.game_window_frame_4)
        self.play_again_button['text'] = 'Play again!'
        self.play_again_button['font'] = font.Font(family='Helvetica', size=10, weight='bold', slant='roman')
        self.play_again_button['width'] = 90
        self.play_again_button['height'] = 30
        self.play_again_button['bg'] = '#292B30'
        self.play_again_button['fg'] = 'white'
        self.play_again_button['activebackground'] = 'red'
        self.play_again_button['activeforeground'] = 'black'
        self.play_again_button.grid(row=0, column=1, sticky=tkinter.NE)

    def play_game(self):

        self.clearing_the_frame()
        self.make_game_window()

    def disable_button(self, button):

        button['state'] = tkinter.DISABLED
        button['fg'] = 'black'
        button['bg'] = 'white'


    def go_back(self):
        self.clearing_the_frame()
        self.make_starting_window()

    def updating_hangman_images(self, state):
        image = self.load_hangman(state=state)
        self.label_hangman['image'] = image
        self.label_hangman.image = image
        self.update()

    def ending(self):
        self.destroy()

    def clearing_the_frame(self):
        for widget in self.frame_1.winfo_children():
            widget.destroy()


class Game(App):

    def __init__(self):
        super().__init__()
        self.words = words_list.return_list()
        self.word = ""
        self.lives = 6
        self.known_letters = []
        self.score = 0
        self.star_word = ""

    def make_starting_window(self):
        super(Game, self).make_starting_window()
        self.starting_window_button_play['command'] = self.start_the_game

    def go_back(self):
        self.reset_all_variables()
        super(Game, self).go_back()

    def make_game_window(self):
        super(Game, self).make_game_window()
        self.button_a['command'] = lambda: self.click('a', self.button_a)
        self.button_b['command'] = lambda: self.click('b', self.button_b)
        self.button_c['command'] = lambda: self.click('c', self.button_c)
        self.button_d['command'] = lambda: self.click('d', self.button_d)
        self.button_e['command'] = lambda: self.click('e', self.button_e)
        self.button_f['command'] = lambda: self.click('f', self.button_f)
        self.button_g['command'] = lambda: self.click('g', self.button_g)
        self.button_h['command'] = lambda: self.click('h', self.button_h)
        self.button_i['command'] = lambda: self.click('i', self.button_i)
        self.button_j['command'] = lambda: self.click('j', self.button_j)
        self.button_k['command'] = lambda: self.click('k', self.button_k)
        self.button_l['command'] = lambda: self.click('l', self.button_l)
        self.button_m['command'] = lambda: self.click('m', self.button_m)
        self.button_n['command'] = lambda: self.click('n', self.button_n)
        self.button_o['command'] = lambda: self.click('o', self.button_o)
        self.button_p['command'] = lambda: self.click('p', self.button_p)
        self.button_q['command'] = lambda: self.click('q', self.button_q)
        self.button_r['command'] = lambda: self.click('r', self.button_r)
        self.button_s['command'] = lambda: self.click('s', self.button_s)
        self.button_t['command'] = lambda: self.click('t', self.button_t)
        self.button_u['command'] = lambda: self.click('u', self.button_u)
        self.button_v['command'] = lambda: self.click('v', self.button_v)
        self.button_w['command'] = lambda: self.click('w', self.button_w)
        self.button_x['command'] = lambda: self.click('x', self.button_x)
        self.button_y['command'] = lambda: self.click('y', self.button_y)
        self.button_z['command'] = lambda: self.click('z', self.button_z)

    def update_the_values(self):

        self.var_score.set(f"Score: {self.score}")
        self.var_star_words.set(self.convert_to_spaces_word(self.star_word))
        self.var_lives_left.set(f"Lives: {self.lives}")

    def start_the_game(self):

        self.play_game()

        self.word = random.choice(self.words)
        self.star_word = "_" * len(self.word)
        self.reset_all_variables()
        self.update_the_values()

    def click(self, letter, button):

        self.disable_button(button)

        print(self.word)

        if letter in self.word:
            self.star_word = ""

            for i in range(0, len(self.word)):

                if letter == self.word[i] or self.word[i] in self.known_letters:
                    self.star_word = self.star_word + self.word[i]
                else:
                    self.star_word = self.star_word + "_"


            # updating the list

            self.known_letters.append(letter)
            self.update_the_values()


            if self.star_word == self.word:
                self.won()

            return

        self.updating_hangman_images(self.lives)
        self.lives = self.lives - 1
        self.update_the_values()


        if self.lives == 0:
            self.lost()

    def lost(self):
        self.var_lives_left.set("You lost!!!")
        self.var_star_words.set(self.convert_to_spaces_word(self.word))
        self.make_play_again_button()
        self.disable_all_button()

    def disable_all_button(self):

        for button in self.game_window_frame_3.winfo_children():
            button['state'] = tkinter.DISABLED
            button['fg'] = 'black'
            button['bg'] = 'white'


    def won(self):
        self.var_lives_left.set("You won!!!")
        self.score = self.score + 1
        self.make_play_again_button()
        self.disable_all_button()

    def convert_to_spaces_word(self, word):
        lol = ""
        for i in word:
            lol = lol + i + " "

        return lol

    def make_play_again_button(self):
        super(Game, self).make_play_again_button()
        self.play_again_button['command'] = self.play_again

    def play_again(self):

        self.start_the_game()

    def reset_all_variables(self):
        self.lives = 6
        self.known_letters.clear()




if __name__ == '__main__':
    game = Game()
    game.make_starting_window()
    game.mainloop()

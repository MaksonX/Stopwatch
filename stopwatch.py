from customtkinter import *
import time
import datetime as dt


class Stopwatch():
    def __init__(self):
        self.button_clicked = True
        self.is_dark_mode = False
        self.start = time.time()
        self.finish = time.time()
        self.modes = ['Light', 'Dark']
        #window
        self.root = CTk()
        self.root.resizable(False, False)
        self.root.title('Stopwatch')
        self.root.geometry('419x400')
        set_appearance_mode('light')

        #frame for clock
        self.frame_for_clock = CTkFrame(self.root)
        self.frame_for_clock.grid(row=0, rowspan=1, columnspan=20)

        #frame for buttons
        self.frame_for_buttons = CTkFrame(self.root, width=300)
        self.frame_for_buttons.grid(row=1, rowspan=1, columnspan=4)

        #frame for a timer
        self.frame_for_timer = CTkFrame(self.root)
        self.frame_for_timer.grid(row=2, rowspan=1)

        #label for clock
        self.lbl_actual_time = CTkLabel(self.frame_for_clock)
        self.lbl_actual_time.grid(row=0, column=0, padx=7)
        self.update_clock()

        #Dropdown list to change theme mode
        self.cmb = CTkComboBox(self.frame_for_clock, values=self.modes, command=self.choose, justify=CENTER)
        self.cmb.grid(row=0, column=4, padx=212)

        #button to start the timer
        self.btn_start = CTkButton(self.frame_for_buttons, text='Start', command=self.start_timer)
        self.btn_start.grid(row=0, column=0, padx=7)
        
        #button to stop the timer
        self.btn_stop = CTkButton(self.frame_for_buttons, text='Stop', command=self.stop_the_clock)
        self.btn_stop.grid(row=0, column=1)

        #label showing a timer
        self.lbl_timer = CTkLabel(self.frame_for_timer, text='0.0')
        self.lbl_timer.grid(row=2)

        
        self.root.mainloop()

    def choose(self, choice):
        set_appearance_mode(choice)

    def start_timer(self):
        self.btn_start.configure(state='disabled')
        self.btn_stop.configure(state='normal')
        self.button_clicked = True
        self.start = time.time()
        self.update_timer()

    def update_timer(self):
        if self.button_clicked:
            self.finish = time.time()
            if self.finish - self.start < 1:
                self.lbl_timer.configure(text=f'{self.finish - self.start:.1}')
            elif self.finish - self.start < 10:
                self.lbl_timer.configure(text=f'{self.finish - self.start:.2}')
            else:
                diff_in_timer = int(self.finish - self.start)
                n = len(str(diff_in_timer)) + 1
                self.lbl_timer.configure(text=f'{self.finish - self.start:.{n}}')
            self.root.after(10, self.update_timer)

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.lbl_actual_time.configure(text=now)
        self.root.after(10, self.update_clock)

    def stop_the_clock(self):
        self.button_clicked = False
        self.start = None
        self.finish = None
        self.lbl_timer.configure(text=self.finish)
        self.btn_stop.configure(state='disabled')
        self.btn_start.configure(state='normal')

if __name__ == '__main__':
    app = Stopwatch()

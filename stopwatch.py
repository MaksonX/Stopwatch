from customtkinter import *
import time
import datetime as dt

class Stopwatch():
    def __init__(self):
        #window
        self.root = CTk()
        self.root.resizable(False, False)
        self.root.title('Stopwatch')
        self.root.geometry('419x400')
        set_appearance_mode('system')

        # ------------------------- Variables for functions ------------------------
        self.string_theme_switcher = StringVar(value='on')
        self.string_start_finish = StringVar(value='Record')
        self.button_clicked_for_stopwatch = False
        self.start = None
        self.finish = None
        self.get_for_entry = None
        self.timer_start = None
        self.button_clicked_for_timer = False

        # ------------------------- Tabview for timer and stopwatch ---------------------------
        self.tabs = CTkTabview(self.root, height=400, width=419)
        self.tab_stopwatch = self.tabs.add('Stopwatch')
        self.tab_timer = self.tabs.add('Timer')
        self.tabs.place(relx=0, rely=0)
 
        # ------------------------- Label for clock ----------------------------------------
        self.lbl_actual_time = CTkLabel(self.tabs)
        self.lbl_actual_time.place(relx=0, rely=0.0)
        self.update_clock()

        # ------------------------- Theme switcher -----------------------------
        self.theme_switcher = CTkSwitch(self.tabs, text='', onvalue='on', offvalue='off', command=self.theme_switch, variable=self.string_theme_switcher)
        self.theme_switcher.place(rely=0.0, relx=0.9)

        # ------------------------- Label for stopwatch ---------------
        self.label_for_stopwatch = CTkLabel(self.tab_stopwatch, text='0.0', font=(None, 20))
        self.label_for_stopwatch.place(relx=0.47, rely=0.3)
        
        # ------------------------- Button to start/stop the stopwatch ---------------------
        self.btn_stopwatch = CTkButton(self.tab_stopwatch, textvariable=self.string_start_finish, command=self.record)
        self.btn_stopwatch.place(relx=0.323, rely=0.4)

        # ------------------------- Entry for amount of time ------------------------
        self.entr_for_timer = CTkEntry(self.tab_timer, placeholder_text='Input time')
        self.entr_for_timer.place(relx=0.315, rely=0.2)

        # ------------------------- Label for timer ----------------------------------------
        self.label_for_timer = CTkLabel(self.tab_timer, text='0.0')
        self.label_for_timer.place(relx=0.315, rely=0.3)

        # ------------------------- Button to start the timer --------------------------------
        self.btn_for_timer = CTkButton(self.tab_timer, text='Start timer')
        self.btn_for_timer.place(relx=0.5, rely=0)

        self.root.mainloop()

    def theme_switch(self):
        if self.string_theme_switcher.get() == 'on':
            set_appearance_mode('dark')
            self.string_theme_switcher.set('on')
        elif self.string_theme_switcher.get() == 'off':
            set_appearance_mode('light')
            self.string_theme_switcher.set('off')

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.lbl_actual_time.configure(text=now)
        self.root.after(1000, self.update_clock)

    def record(self):
        if not self.button_clicked_for_stopwatch:
            self.start = time.time()
            self.button_clicked_for_stopwatch = True
            self.string_start_finish.set('Stop')
            self.update_record()
        else:
            self.finish = time.time()
            self.button_clicked_for_stopwatch = False
            self.string_start_finish.set('Record')

    def update_record(self):
        if self.button_clicked_for_stopwatch:
            self.finish = time.time()
            elapsed_time = self.finish - self.start
            formatted_time = "{:.1f}".format(elapsed_time)
            self.label_for_stopwatch.configure(text=formatted_time)
            self.root.after(100, self.update_record)

if __name__ == '__main__':
    app = Stopwatch()

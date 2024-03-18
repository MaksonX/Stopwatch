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
        self.time_var_for_update_timer = None
        self.var_for_after_method = None

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
        self.theme_switcher.place(rely=0.008, relx=0.9)

        # ------------------------- Label for stopwatch ---------------
        self.label_for_stopwatch = CTkLabel(self.tab_stopwatch, text='0.0', font=(None, 20))
        self.label_for_stopwatch.place(relx=0.465, rely=0.3)
        
        # ------------------------- Button to start/stop the stopwatch ---------------------
        self.btn_stopwatch = CTkButton(self.tab_stopwatch, textvariable=self.string_start_finish, command=self.record)
        self.btn_stopwatch.place(relx=0.323, rely=0.4)

        # ------------------------- Entry for amount of time ------------------------
        self.entr_for_timer = CTkEntry(self.tab_timer, placeholder_text='Input time')
        self.entr_for_timer.place(relx=0.32, rely=0.3)

        # ------------------------- Label for timer ----------------------------------------
        self.label_for_timer = CTkLabel(self.tab_timer, text='0.0')
        self.label_for_timer.place(relx=0.466, rely=0.2)

        # ------------------------- Button to start the timer --------------------------------
        self.btn_for_timer = CTkButton(self.tab_timer, text='Start timer', command=self.submit_time)
        self.btn_for_timer.place(relx=0.3184, rely=0.409)

        # ------------------------- Label to say to user time is up ----------------------------
        self.label_for_time_is_up = CTkLabel(self.tab_timer, text='', font=(None, 20))
        self.label_for_time_is_up.place(relx=0.3823, rely=0.09)

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

    def submit_time(self):
        self.button_clicked_for_timer = not self.button_clicked_for_timer
        self.start = time.time()
        self.time_var_for_update_timer = float(self.entr_for_timer.get())
        self.label_for_time_is_up.configure(text='')
        self.btn_for_timer.configure(text='Stop')
        self.update_timer()
    
    def update_timer(self):
        t = float(self.entr_for_timer.get())
        if self.button_clicked_for_timer:
            self.finish = time.time()
            if (t - (self.finish - self.start)) < 0.02999999999:
                self.label_for_time_is_up.configure(text='Time is up', font=(None, 20))
                self.label_for_timer.configure(text=f'{abs(t - (self.finish - self.start)):.1}')
                self.button_clicked_for_timer = False
                self.btn_for_timer.configure(text='Start timer')
                self.root.after_cancel(self.var_for_after_method)
            else:
                self.label_for_timer.configure(text=f'{(t - (self.finish - self.start)):.2}')
                self.time_var_for_update_timer -= (self.finish - self.start)
                self.var_for_after_method = self.root.after(100, self.update_timer)
    
if __name__ == '__main__':
    app = Stopwatch()

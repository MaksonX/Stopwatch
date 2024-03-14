import tkinter as tk
import tkinter.ttk as ttk
import time
import datetime as dt


class Timer():
    def __init__(self):
        self.button_clicked = True
        self.is_dark_mode = False
        self.start = time.time()
        self.finish = time.time()
        #window
        self.root = tk.Tk()
        self.root.configure()
        self.root.title('Time Shower')
        self.root.geometry('300x300')
        self.root.iconbitmap(True, 'E:\PythonProjects\PYTHON\pylogo.ico')

        #frame for clock
        self.frame_for_clock = tk.LabelFrame(self.root, text='Actual time')
        self.frame_for_clock.grid(row=0, rowspan=1, columnspan=4)

        #frame for buttons

        self.frame_for_buttons = tk.LabelFrame(self.root, text='Buttons to control the timer', width=300)
        self.frame_for_buttons.grid(row=1, rowspan=1, columnspan=4)

        #frame for a timer
        self.frame_for_timer = tk.Frame(self.root)
        self.frame_for_timer.grid(row=2, rowspan=1)

        #label for clock
        self.lbl_actual_time = tk.Label(self.frame_for_clock, padx=2, pady=2)
        self.lbl_actual_time.grid(row=1)
        self.update_clock()

        #button to start the timer
        self.btn_start = ttk.Button(self.frame_for_buttons, text='Start', command=self.start_timer)
        self.btn_start.grid(row=0, column=0)
        
        #button to stop the timer
        self.btn_stop = ttk.Button(self.frame_for_buttons, text='Stop', command=self.stop_the_clock)
        self.btn_stop.grid(row=0, column=1)

        #button which changes the theme of the app
        self.btn_change_theme = ttk.Button(self.frame_for_buttons, text='Change theme', command=self.change_theme)
        self.btn_change_theme.grid(row=0, column=2)

        #label showing a timer
        self.lbl_timer = tk.Label(self.frame_for_timer, text='0.0')
        self.lbl_timer.grid(row=2)

        #frame for points in timer
        self.frame_for_points = tk.LabelFrame(self.root, text='Points')
        self.frame_for_points.grid(row=3)

        #button which creates points in timer
        # self.button_for_points

        self.cfgs_for_white_theme = {'bg': 'white', 'fg': 'black'}
        
        self.cfgs_for_black_theme = {'bg': 'black', 'fg': 'white'}
        
        self.root.mainloop()

    def change_theme(self):
        if self.is_dark_mode:
            self.change_to_white(self.cfgs_for_white_theme)
        else:
            self.change_to_black(self.cfgs_for_black_theme)

        self.is_dark_mode = not self.is_dark_mode

    def change_to_white(self, theme: dict):
        self.root.configure(bg=theme['bg'])

        style = ttk.Style()
        style.theme_use('default')

        style.map('Mod.TButton',
                  background = [("active", "white"), ("!active", "white")],
                  foreground = [('active', 'black'), ("!active", "black")])

        for widget in self.root.winfo_children():
            widget_type = widget.winfo_class()

            if widget_type == 'Labelframe':
                widget.configure(bg=theme['bg'], fg=theme['fg'])
                
                for widget_2 in widget.winfo_children():
                    widget_type_lblfrms = widget_2.winfo_class()

                    if widget_type_lblfrms == 'TButton':
                        widget_2.configure(style='Mod.TButton')
                    elif widget_type_lblfrms == 'Label':
                        widget_2.configure(bg=theme['bg'], fg=theme['fg'])
            elif widget_type == 'Frame':
                widget.configure(bg=theme['bg'])
                
                for widget_2 in widget.winfo_children():
                    widget_type_frms = widget_2.winfo_class()
                    
                    if widget_type_frms == 'TButton':
                        widget_2.configure(style='Mod.TButton')
                    elif widget_type_frms == 'Label':
                        widget_2.configure(bg=theme['bg'], fg=theme['fg'])
        
    def change_to_black(self, theme: dict):
        self.root.configure(bg=theme['bg'])

        style = ttk.Style()
        style.theme_use('default')

        style.map('Mod.TButton',
                  background = [("active", "black"), ("!active", "black")],
                  foreground = [('active', 'white'), ("!active", "white")])
        
        for widget in self.root.winfo_children():
            widget_type = widget.winfo_class()

            if widget_type == 'Labelframe':
                widget.configure(bg=theme['bg'], fg=theme['fg'])
                
                for widget_2 in widget.winfo_children():
                    widget_type_lblfrms = widget_2.winfo_class()

                    if widget_type_lblfrms == 'TButton':
                        widget_2.configure(style='Mod.TButton')
                    elif widget_type_lblfrms == 'Label':
                        widget_2.configure(bg=theme['bg'], fg=theme['fg'])
            elif widget_type == 'Frame':
                widget.configure(bg=theme['bg'])
                
                for widget_2 in widget.winfo_children():
                    widget_type_frms = widget_2.winfo_class()
                    
                    if widget_type_frms == 'TButton':
                        widget_2.configure(style='Mod.TButton')
                    elif widget_type_frms == 'Label':
                        widget_2.configure(bg=theme['bg'], fg=theme['fg'])

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
    print('Hello')

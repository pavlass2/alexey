import tkinter
from tkinter import ttk
from work_session import Work_session

class Window(tkinter.Frame):

    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.master = master

        # variables
        txf_width = 50
        txf_height = 3
        padding = 10

        # initiate tabs
        tabControl = ttk.Notebook(root)
        tab_new_session = ttk.Frame(tabControl)
        tab_session_history = ttk.Frame(tabControl)
        tab_settings = ttk.Frame(tabControl)
        tabControl.add(tab_new_session, text='Session')
        tabControl.add(tab_session_history, text='Session history')
        tabControl.add(tab_settings, text='Settings')
        # Packing the tab control to make the tabs visible
        tabControl.pack(expand=1, fill="both")

        # Session tab
        s = ttk.Style()
        s.theme_use("clam")
        s.configure('alexey.lbl_actual_remaining_time.TLabel', font=('Helvetica', 32), borderwidth=4, bordercolor='red')
        s.configure("alexey.lbl_general.TButton", font=('Helvetica', 16))
        s.configure("alexey.lbl_general.TLabel", font=('Helvetica', 10))
        s.configure("alexey.lbl_general.TText", font=('Helvetica', 10))
        self.__session = { 
            # 0
            "lbl_session_name": ttk.Label(tab_new_session, justify="center", text="Session name", style="alexey.lbl_general.TLabel"),
            "txt_session_name": tkinter.Text(tab_new_session, wrap="none", width=txf_width, height=1),
            # 1
            "lbl_problem": ttk.Label(tab_new_session, justify="center", text="Problem\nBasic description of the problem.", style="alexey.lbl_general.TLabel"),
            "txt_problem": tkinter.Text(tab_new_session, wrap="word", width=txf_width, height=txf_height),
            # 2
            "lbl_goal": ttk.Label(tab_new_session, justify="center", text="Goal\nWhat do you plan do achieve in this session?", style="alexey.lbl_general.TLabel"),
            "txt_goal": tkinter.Text(tab_new_session, wrap="word", width=txf_width, height=txf_height),
            # 3
            "lbl_actual_remaining_time": ttk.Label(tab_new_session, justify="center", text="0:00:00", style="alexey.lbl_actual_remaining_time.TLabel"),
            "btn_start_session": ttk.Button(tab_new_session, text="Start session", command=self.__start_session, state="disabled", style="alexey.lbl_general.TButton"),            
            # 4
            "lbl_goal_achieved": ttk.Label(tab_new_session, justify="center", text="Did you achieved you projected goal?", style="alexey.lbl_general.TLabel"),
            "txt_goal_achieved": tkinter.Text(tab_new_session, wrap="word", width=txf_width, height=txf_height, state="disabled"),
            # 5
            "lbl_problem_solved": ttk.Label(tab_new_session, justify="center", text="Is the problem, you worked on, solved?", style="alexey.lbl_general.TLabel"),
            "txt_problem_solved": tkinter.Text(tab_new_session, wrap="word", width=txf_width, height=txf_height, state="disabled"),
            # 6
            "lbl_result_message": ttk.Label(tab_new_session, justify="center", text="Any comment concerning result of this session?", style="alexey.lbl_general.TLabel"),
            "txt_result_message": tkinter.Text(tab_new_session, wrap="word", width=txf_width, height=txf_height, state="disabled"),
            # 7
            "empty_space": "empty_space",
            "btn_save_session": ttk.Button(tab_new_session, text="Save", command=self.__save_session, state="disabled", style="alexey.lbl_general.TButton"),            
        }

        column = 0
        row = 0
        for key in self.__session:
            if key != "empty_space":
                self.__session[key].grid(column=column, row=row, padx=padding, pady=padding)
            
            column += 1            
            if column > 1:
                column = 0
                row += 1

        self.bind_all('<<Modified>>', self.__check_start_session_button_state)


    def __start_session(self):
        print("Session started")
        self.__session["txt_session_name"]["state"] = "disabled"
        self.__session["txt_problem"]["state"] = "disabled"
        self.__session["txt_goal"]["state"] = "disabled"
        self.__session["btn_start_session"]["state"] = "disabled"

    def __save_session(self):
        pass

    def __check_start_session_button_state(self, event):
        if (self.__session["txt_session_name"].get("1.0", "end-1c") != ""\
        and self.__session["txt_problem"].get("1.0", "end-1c") != ""\
        and self.__session["txt_goal"].get("1.0", "end-1c") != ""):
            self.__session["btn_start_session"]["state"] = "enabled"            



# window_width = 600
# window_height = 600
root = tkinter.Tk()
# root.geometry(str(window_width) + "x" + str(window_height))
window = Window(root)
# window.grid()

# setup style
# style = ttk.Style()
# style.theme_create(
#     "MyStyle", parent="alt", settings={
#         "TNotebook": {
#             "configure": {
#                 "tabmargins": [2, 5, 2, 0] 
#             } 
#         },
#         "TNotebook.Tab": {
#             "configure": {
#                 "padding": [window_width / 8, 5] 
#             },
#         }
#     }
# )
# style.theme_use("MyStyle")
# style

# def reset_style(event):
#     global window_width
#     window_width = event.width
#     global window_height
#     window_height = event.height
#     global style
#     style.configure("TNotebook.Tab", padding=str(window_width / 8))

# set window title
root.wm_title("Alexey")



# setup tabs
# tabControl = ttk.Notebook(root)
# tab_new_session = ttk.Frame(tabControl)
# tab_session_history = ttk.Frame(tabControl)
# tab_settings = ttk.Frame(tabControl)
# tabControl.add(tab_new_session, text='New work session')
# tabControl.add(tab_session_history, text='Session history')
# tabControl.add(tab_settings, text='Settings')
# # Packing the tab control to make the tabs visible
# tabControl.pack(expand=1, fill="both")
# # Creating Label widget as a child of the parent window (root)
# ttk.Label(tab_new_session, text="Welcome to GeeksForGeeks").grid(column=0, row=0, padx=30, pady=30)
# ttk.Label(tab_session_history, text="Lets dive into the world of computers").grid(column=0, row=0, padx=30, pady=30)

# show window
root.mainloop()

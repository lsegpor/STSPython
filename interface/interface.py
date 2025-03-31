from tkinter import *
from tkinter import messagebox, ttk, filedialog
import sys
sys.path.append('../autogen/agwb/python/')
sys.path.append('../smx_tester/')
#from file_management import FileManagement as fm
#from main import Main
#from smx_tester import *
from PIL import Image, ImageTk
import os

class Interface:
    
    def __init__(self, root):
        
        self.root = root
        #self.main = Main()
        #self.log = fm.set_logging_details()

        self.root.config(bg="white")
        
        notebook = ttk.Notebook(root)
        notebook.pack(expand=True, fill="both")
        
        tab1 = Frame(notebook, bg="white")
        tab2 = Frame(notebook, bg="white")
        tab3 = Frame(notebook, bg="white")

        notebook.add(tab1, text="Setup 0")
        notebook.add(tab2, text="Setup 1")
        notebook.add(tab3, text="Setup 2")

        tab1.grid_rowconfigure(0, weight=1)
        tab1.grid_rowconfigure(1, weight=0)
        tab1.grid_columnconfigure(0, weight=1)

        top_frame = Frame(tab1, bg="white")
        top_frame.grid(row=0, column=0, sticky="nsew", columnspan=2)
        
        top_frame.grid_columnconfigure(0, weight=1, uniform="equal")
        top_frame.grid_columnconfigure(1, weight=1, uniform="equal")

        bottom_frame = Frame(tab1, bg="white")
        bottom_frame.grid(row=1, column=0, sticky="nsew")

        top_frame.grid_columnconfigure(0, weight=1)
        top_frame.grid_rowconfigure(0, weight=1)

        left_frame = Frame(top_frame, bg="white")
        left_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=0)

        right_frame = Frame(top_frame, bg="white")
        right_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=(20, 10))

        frame_top_left = Frame(left_frame, bg="white")
        frame_top_left.grid(row=0, column=0, sticky="nsew", padx=0, pady=10)
        
        button_frame = Frame(tab1, bg="white")
        button_frame.grid(row=2, column=0, sticky="nsew", padx=0, pady=20)
        
        checkbox_frame1 = Frame(right_frame, bg="white")
        checkbox_frame1.grid(row=3, column=1, columnspan=2, sticky="we", padx=(2, 10), pady=8)
        
        checkbox_frame2 = Frame(right_frame, bg="white")
        checkbox_frame2.grid(row=4, column=1, columnspan=2, sticky="we", padx=(2, 10), pady=8)

        try:
            route_image = "/home/cbm/lsegura/emu_ladder/python/module_tests/dinosaur_icon.png"
            image = Image.open(route_image)
            image = image.resize((80, 80))
            image_tk = ImageTk.PhotoImage(image)
        except Exception as e:
            print(f"Error loading the image: {e}")
            image_tk = None

        if image_tk:
            logo_label = Label(frame_top_left, image=image_tk, bg="white")
            logo_label.image = image_tk
            logo_label.grid(row=0, column=0, padx=0, pady=10, sticky="w")
        else:
            logo_label = Label(frame_top_left, text="(No Image)", font=("Times New Roman", 12), bg="white", fg="red")
            logo_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        titulo_label = Label(frame_top_left, text="STS Module Testing", font=("Times New Roman", 20, "bold"), bg="white")
        titulo_label.grid(row=0, column=1, padx=5, pady=10, sticky="w")

        frame_left = Frame(left_frame, bg="white")
        frame_left.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        frame_left.grid_columnconfigure(0, weight=1, uniform="equal")
        frame_left.grid_columnconfigure(1, weight=1, uniform="equal")

        labels = ["Module ID:", "EMU ID:", "I@150V for P-side:", "I@150V for N-side:"]
        entries = []

        for i, label in enumerate(labels):
            Label(frame_left, text=label, bg="white", font=("Times New Roman", 12)).grid(row=i, column=0, padx=(0, 15), pady=15, sticky="e")
            entry = Entry(frame_left)
            entry.grid(row=i, column=1, pady=15, sticky="w")
            entries.append(entry)

        self.module_entry, self.emu, self.slc_pside, self.slc_nside = entries
        
        text_area = Text(bottom_frame, wrap="word", font=("Times New Roman", 12), height=8)
        text_area.pack(side="left", expand=True, fill="both", padx=(25, 0), pady=20)

        scrollbar = Scrollbar(bottom_frame)
        scrollbar.pack(side="right", fill="y", pady=20, padx=(0, 25))

        text_area.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=text_area.yview)

        button1 = Button(button_frame, text="Run tests", bg="#4a4948", fg="white", activebackground="#242323", activeforeground="white", font=("Times New Roman", 15), width=15, relief="flat", borderwidth=1)
        button1.grid(row=0, column=0, padx=10)

        button2 = Button(button_frame, text="Save observations", bg="#4a4948", fg="white", activebackground="#242323", activeforeground="white", font=("Times New Roman", 15), width=15, relief="flat", borderwidth=1)
        button2.grid(row=0, column=1, padx=10)

        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)
        
        label_directory = Label(right_frame, text="Directory File:", bg="white", font=("Times New Roman", 12))
        label_directory.grid(row=0, column=0, pady=15, sticky="w")

        self.entry_directory = ttk.Entry(right_frame)
        self.entry_directory.grid(row=0, column=1, padx=5, pady=15, sticky="we")

        select_button1 = Button(right_frame, text="Browse...", command=self.select_directory, bg="#4a4948", fg="white", activebackground="#242323", activeforeground="white", font=("Times New Roman", 12), relief="flat", borderwidth=1)
        select_button1.grid(row=0, column=2, padx=5, pady=5, sticky="e")
        
        default_directory1 = os.path.expanduser("/home/cbm/lsegura/emu_ladder/python/ladder_files")
        self.entry_directory.insert(0, default_directory1)
        
        label_calibration = Label(right_frame, text="Calibration Dir:", bg="white", font=("Times New Roman", 12))
        label_calibration.grid(row=1, column=0, pady=15, sticky="w")

        self.entry_calibration = ttk.Entry(right_frame)
        self.entry_calibration.grid(row=1, column=1, padx=5, pady=15, sticky="we")

        select_button2 = Button(right_frame, text="Browse...", command=self.select_calibration, bg="#4a4948", fg="white", activebackground="#242323", activeforeground="white", font=("Times New Roman", 12), relief="flat", borderwidth=1)
        select_button2.grid(row=1, column=2, padx=5, pady=5, sticky="e")
        
        default_directory2 = os.path.expanduser("calibration_path")
        self.entry_calibration.insert(0, default_directory2)
        
        label_asic = Label(right_frame, text="Number of ASICs to test (0-7):", bg="white", font=("Times New Roman", 15, "bold"))
        label_asic.grid(row=2, column=0, padx=10, pady=10, sticky="we", columnspan=3)
        
        label_nside = Label(right_frame, text="ASIC N-Side:", bg="white", font=("Times New Roman", 12))
        label_nside.grid(row=3, column=0, padx=(10, 2), pady=10, sticky="we", columnspan=1)
        
        checkbox_vars1 = [IntVar() for _ in range(8)]

        for i in range(8):
            chk = Checkbutton(checkbox_frame1, variable=checkbox_vars1[i], font=("Times New Roman", 8), bg="white")
            chk.grid(row=0, column=i, padx=5, pady=0)
            
        label_pside = Label(right_frame, text="ASIC P-Side:", bg="white", font=("Times New Roman", 12))
        label_pside.grid(row=4, column=0, padx=(10, 2), pady=10, sticky="we", columnspan=1)
        
        checkbox_vars2 = [IntVar() for _ in range(8)]

        for i in range(8):
            chk = Checkbutton(checkbox_frame2, variable=checkbox_vars2[i], font=("Times New Roman", 8), bg="white")
            chk.grid(row=0, column=i, padx=5, pady=0)
            
        label_tests = Label(right_frame, text="Tests to execute:", bg="white", font=("Times New Roman", 15, "bold"))
        label_tests.grid(row=5, column=0, padx=10, pady=10, sticky="we", columnspan=3)

    def select_directory(self):
        directory = filedialog.askdirectory(initialdir=self.entry_directory.get())
        if directory:
            self.entry_directory.delete(0, END)
            self.entry_directory.insert(0, directory)
            
    def select_calibration(self):
        directory = filedialog.askdirectory(initialdir=self.entry_calibration.get())
        if directory:
            self.entry_calibration.delete(0, END)
            self.entry_calibration.insert(0, directory)

    
    def main_programme(self):
        #module=self.module_entry.get()
        #sensor_size=self.sensor_size.get()
        #sensor_qgrade=self.sensor_qgrade.get()
        #sn_pside=self.sn_pside.get()
        #sn_nside=self.sn_nside.get()
        #slc_pside=self.slc_pside.get()
        #slc_nside=self.slc_nside.get()
        
        self.main.execute_tests("M3DL1T4001124A2", "124A2", "124B2", 124, "A", 0, 0)
        messagebox.showinfo("Result", "Tests concluded.")

if __name__ == "__main__":
    root = Tk()
    root.title("STS_Module Testing")
    root.resizable(False, False)
    root.iconphoto(True, PhotoImage(file="/home/cbm/lsegura/emu_ladder/python/module_tests/dinosaur_icon.png"))
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 850
    window_height = 700
    position_x = (screen_width - window_width) // 2
    position_y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    interface = Interface(root)
    root.mainloop()
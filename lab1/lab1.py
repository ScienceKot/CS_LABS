# Importing all needed libraries.
import glob
import json
import tarfile
from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter.font import Font
import requests
import audit
import re

# Defining the Graphical user Interface.
main_app = Tk()
main_app.resizable(False, False)
app_font = Font(family="Courier New", size=12)
s = ttk.Style()
s.configure('TFrame', background='#000000')
main_app.title("Security Benchmarking Tool")
main_app.geometry("950x550")
frame = ttk.Frame(main_app, width=950, height=550, style='TFrame')
frame.grid(column=0, row=0)


index = 0
array = []
matching = []

vars = StringVar()
to_file = []
structure = []

def download_url(url : str, save_path : str, chunk_size : int = 1024) -> None:
    '''
        This function downloads a files an url.
    :param url: str
        The source url to download from.
    :param save_path: str
        The path in the system to save the files.
    :param chunk_size: int
        The chunk size of the downloading data.
    '''
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)

def extract_file():
    '''
        This function downloads the audits and extracts them in a specific folder.
    :return:
    '''
    url = "https://www.tenable.com/downloads/api/v1/public/pages/download-all-compliance-audit-files/downloads/7472/download?i_agree_to_tenable_license_agreement=true"
    download_url(url, "audits.tar.gz")
    tf = tarfile.open("audits.tar.gz")
    tf.extractall()
    print(glob.glob("portal_audits/*"))

def import_audit():
    '''
        This function is importing the audits.
    '''
    global array
    file_name = fd.askopenfilename(initialdir="../portal_audits")
    if file_name:
        arr = []
    global structure
    structure = audit.main(file_name)
    for element in structure:
        for key in element:
            str = ''
            for char in element[key]:
                if char != '"' and char != "'":
                    str += char
            is_space_first = True
            str2 = ''
            for char in str:
                if char == ' ' and is_space_first:
                    continue
                else:
                    str2 += char
                    is_space_first = False
            element[key] = str2

    global matching
    matching = structure
    if len(structure) == 0:
        f = open(file_name, 'r')
        structure = json.loads(f.read())
        f.close()
    for struct in structure:
        if 'description' in struct:
            arr.append(struct['description'])
        else:
            arr.append('Error in selecting')
    vars.set(arr)


lstbox = Listbox(frame, bg="#000000", font=app_font, fg="white", listvariable=vars, selectmode=MULTIPLE, width=75, selectbackground='red',height=20, highlightthickness=3)
lstbox.grid(row=0, column=0, columnspan=3, padx=100, pady=100)

def save_config():
    '''
        This function is saving the application configurations.
    '''
    lstbox.select_set(0, END)
    for struct in structure:
        lstbox.insert(END, struct)

    file_name = fd.asksaveasfilename(filetypes=(("AUDIT FILES", ".audit"), ("All files", ".")))
    file_name += '.audit'
    file = open(file_name, 'w')
    selection = lstbox.curselection()
    for i in selection:
        to_file.append(matching[i])
    json.dump(to_file, file)
    file.close()

# Defining the button of the Graphical user interface.
btn_font = Font(family="Courier New", size=10)
save_btn = Button(frame, bg="white", fg="black", font=btn_font, text="Save", width=8, height=1, command=save_config).place(relx=0.01, rely=0.01)
import_btn = Button(frame, bg="white", fg="black", font=btn_font, text="Import", width=8, height=1,command=import_audit).place(relx=0.01, rely=0.065)
download_btn = Button(frame, bg="white", fg="black", font=btn_font, text="Download", width=8, height=1,command=extract_file).place(relx=0.01, rely=0.12)
exit_btn = Button(frame, bg="white", fg="black", font=btn_font, text="Exit", width=8, height=1, command=main_app.quit).place(relx=0.01, rely=0.175)


main_app.mainloop()
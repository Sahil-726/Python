import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox
from googletrans import Translator

def translate_text():
        text=srcText.get("1.0", tk.END).strip()
        target_lang=lang.get()
        
        if not text:
            messagebox.showwarning("Input Error", "Please enter the text to translate")
            return
        languages={
              "English":"en",
              "French":"fr",
              "German":"de",
              "Spanish":"es",
              "Hindi":"hi",
              "Chinese":"zh-cn"
        }
        dest_lang=languages.get(target_lang)
        if dest_lang is None:
           messagebox.showerror("Language Error", "Select any language.")
           return
        try:
            trans=Translator()
            translated=trans.translate(text,dest=dest_lang)
            desText.delete("1.0", tk.END)
            desText.insert(tk.END,translated.text)
        except Exception as e:
           messagebox.showerror("Translation Error", f"An error occurred: {str(e)}")

root =tk.Tk()
root.title("Google Translator")
root.geometry("500x550")
root.config(bg="#00FFFF")
lab=tk.Label(root,text="Translator",font=("Time New Roman", 40, "bold"))
lab.place(x=100, y=35 ,height=80, width=300)
#label of source text..
lab=tk.Label(root,text="Source Text",font=("Time New Roman", 22, "bold"), bg="#66CDAA")
lab.place(x=20, y=130 ,height=25, width=460)
# source text area..
srcText=tk.Text(root,font=("Time New Roman", 13),wrap="word")
srcText.place(x=20, y=158,height=120, width=460)
#creation of drop down menu..
lang=tk.StringVar(root)
lang.set("English")
lang_menu=ttk.OptionMenu(root,lang,"English", "Hindi", "French", "Chinese","German","Spanish")
lang_menu.place(x=20, y=295)
#Button for conversion..
button=ttk.Button(root,text="Translate", command=translate_text)
button.place(x=398,y=295)
# Converted text label
labC=tk.Label(root,text="Converted Text",font=("Time New Roman", 22, "bold"), bg="#66CDAA")
labC.place(x=20, y=345 ,height=25, width=460)
# Converted text area
desText=tk.Text(root,font=("Time New Roman", 13),wrap="word")
desText.place(x=20, y=373,height=120, width=460)

root.mainloop()

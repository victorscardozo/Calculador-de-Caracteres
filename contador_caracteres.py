from tkinter import *
import customtkinter



def contar_caracteres():

   
    frase = entry.get()
    caracteres_com_espaco = len(frase)

    print(frase)


   # caracteres_sem_espaco = len(frase)- frase.count(" ")
    #print(caracteres_sem_espaco)



    texto_2["text"] = caracteres_com_espaco

janela = customtkinter.CTk()

janela.title("Tkinter.com - CustomTkinter TextBox")
janela.geometry('400x400')



entry = Entry(janela, width=50, font=('Arial 10'))
entry.grid(column=1, row=2, padx=30, pady=10)

#textbox = customtkinter.CTkTextbox(janela)
#textbox.pack(pady=20)



texto_1 = Label(janela, text = 'Insira abaixo o texto:')
texto_1.grid(column=1, row=1, padx=30, pady=10)



botao = Button(janela, text='Contar caracteres', command=contar_caracteres)
botao.grid(column=1, row=3, padx=30, pady=10)



texto_2 = Label(janela, text="")
texto_2.grid(column=1, row=4, padx=30, pady=40)
janela.mainloop()
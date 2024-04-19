from tkinter import *
import customtkinter






#Funcao para contar caracteres 
def contar_caracteres():

    #Pegar o valor inserido na textbox e atribuí-lo à variavel frase
    frase = textbox.get(1.0, END) 

    #Identificar o numero de caracteres total
    caracteres_com_espaco = len(frase)
    #Identificar o numero de caracteres total - espaços
    caracteres_sem_espaco = len(frase)- frase.count(" ")



    #Substituir o Texto 2 pelo resultado 
    texto_2["text"] = caracteres_com_espaco-1

    #Substituir o texto 3 pelo resultado 
    texto_3["text"] = caracteres_sem_espaco-1




#Definir a janela 1
janela = customtkinter.CTk()

#Tilulo e dimensões da janela
janela.title("Contador de Caracteres")
janela.geometry('400x500')


#Definindo a caixa de texto e sua posiçao
textbox = customtkinter.CTkTextbox(janela)
textbox.grid(pady=20,padx=20, column=1, row=2, ipadx=70)


#Definindo texto 1 e sua posição
texto_1 = Label(janela, text = 'Insira abaixo o texto:')
texto_1.grid(column=1, row=1, padx=30, pady=10)


#Definindo Botão, sua posição e a função que executará
botao = Button(janela, text='Contar caracteres', command=contar_caracteres)
botao.grid(column=1, row=3, padx=30, pady=10)


#Definindo texto 2 e sua posição
texto_2 = Label(janela, text="")
texto_2.grid(column=1, row=4, padx=30, pady=40, ipadx=15)


#Definindo texto 3 e sua posição
texto_3 = Label(janela, text="")
texto_3.grid(column=1, row=5, padx=30, pady=40, ipadx=15)










janela.mainloop()
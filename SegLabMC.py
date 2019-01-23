#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aluno: Pedro Pacheco Mendes Filho
Prova de Programacao II
"""

from tkinter import *
import time

class Aplication:
    def __init__(self, master=None):
        self.users = {'admin':'admin'}
        self.master = master
        
        self.dados = {'João da Silva':['234.456.678-12','12/12/2003','M','Bolsista'],
                      'Carlos Oliveira':['135.486.698-22','22/02/1997','M','Bolsista'],
                      'Fernanda Coelho':['678.345.234-00','31/07/1995','F','Bolsista'],
                      'Jussara Vitória':['978.645.434-10','26/08/1993','F','Estagiária'],
                      'Mayara Sousa':['958.623.418-34','20/10/1982','F','Estagiária'],
                      'Pedro Forte':['358.983.888-33','02/03/1972','M','Coordenador']}
        master.geometry('700x700')
        master.title("Segurança LABMC")
        
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
  
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
  
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()
  
        self.titulo = Label(self.primeiroContainer, text="Login e Registro")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
  
        self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
  
        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)
  
        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)
  
        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)
  
        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "12")
        self.autenticar["width"] = 15
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()
        
        self.registrar = Button(self.quartoContainer)
        self.registrar["text"] = "Registrar"
        self.registrar["font"] = ("Calibri", "12")
        self.registrar["width"] = 15
        self.registrar["command"] = self.verificarRegister
        self.registrar.pack()
  
        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()
        
  
    #Método verificar senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario in list(self.users.keys()):
            if (self.users[usuario] == senha):
                self.mensagem["text"] = "Autenticado"
                self.user_logado = usuario
                self.user_senha = senha
                self.primeiroContainer.destroy()
                self.segundoContainer.destroy()
                self.terceiroContainer.destroy()
                self.quartoContainer.destroy()
                
                self.interface()
        else:
            self.mensagem["text"] = "Erro na autenticação"
            
        pass
    
    def interface(self):
        self.master.geometry('700x500')
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(self.master)
        self.primeiroContainer.pack()
  

        
        self.container = [Frame(self.master, padx=40),Frame(self.master, padx=20),Frame(self.master, padx=20),Frame(self.master, padx=20),Frame(self.master, padx=20)]
        for b in self.container:
            b.pack()
        
        self.btContainer = Frame(self.master)
        self.btContainer["pady"] = 20
        self.btContainer.pack()
        
        self.txtContainer = Frame(self.master)
        self.txtContainer['bg'] = 'red'
        self.txtContainer.pack()
        
        self.titulo = Label(self.primeiroContainer, text="Usuario: {}\nPesquisar(pelo Nome):".format(self.user_logado))
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
        
        
        self.nomeLabel = Label(self.container[0],text="Nome:", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
  
        self.nome = Entry(self.container[0])
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)
  
        self.cpfLabel = Label(self.container[1], text="CPF", font=self.fontePadrao)
        self.cpfLabel.pack(side=LEFT)
  
        self.cpf = Entry(self.container[1])
        self.cpf["width"] = 30
        self.cpf["font"] = self.fontePadrao
        self.cpf.pack(side=LEFT)
        
        self.dataLabel = Label(self.container[2], text="Data", font=self.fontePadrao)
        self.dataLabel.pack(side=LEFT)
  
        self.data = Entry(self.container[2])
        self.data["width"] = 30
        self.data["font"] = self.fontePadrao
        self.data.pack(side=LEFT)
        
        self.sexLabel = Label(self.container[3], text="Sexo", font=self.fontePadrao)
        self.sexLabel.pack(side=LEFT)
  
        self.sex = Entry(self.container[3])
        self.sex["width"] = 30
        self.sex["font"] = self.fontePadrao
        self.sex.pack(side=LEFT)
        
        self.funcLabel = Label(self.container[4], text="Função", font=self.fontePadrao)
        self.funcLabel.pack(side=LEFT)
  
        self.func = Entry(self.container[4])
        self.func["width"] = 30
        self.func["font"] = self.fontePadrao
        self.func.pack(side=LEFT)
        
        self.pesqBt = Button(self.btContainer)
        self.pesqBt["text"] = "Pesquisar"
        self.pesqBt["font"] = ("Calibri", "12")
        self.pesqBt["width"] = 15
        self.pesqBt["command"] = self.pesquisar
        self.pesqBt.pack()
        
        self.defBt = Button(self.btContainer)
        self.defBt["text"] = "Atualizar Cadastro"
        self.defBt["font"] = ("Calibri", "12")
        self.defBt["width"] = 15
        self.defBt["command"] = self.atualizar
        self.defBt.pack()
        
        self.newBt = Button(self.btContainer)
        self.newBt["text"] = "Novo Cadastro"
        self.newBt["font"] = ("Calibri", "12")
        self.newBt["width"] = 15
        self.newBt["command"] = self.novo
        self.newBt.pack()
        
        
        
        
        self.mensagem = Label(self.btContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()
        
        self.textForm = Label(self.txtContainer, text="", font=self.fontePadrao)
        self.textForm.pack()

        self.listar()
        
        
        
#        self.txtidusuario.delete(0, END)
#        self.txtidusuario.insert(INSERT, user.idusuario)
        
    def novo(self):
        b = {self.nome.get():[self.cpf.get(),self.data.get(),self.sex.get(),self.func.get()]}
        self.dados.update(b)
        self.mensagem['text']="Usuário Cadastrado!"
        self.listar()
        print(self.dados)
        
    def pesquisar(self):
        nome = self.nome.get()
        if nome in list(self.dados.keys()):
            self.cpf.delete(0, END)
            self.cpf.insert(INSERT, self.dados[nome][0])
            self.data.delete(0, END)
            self.data.insert(INSERT, self.dados[nome][1])
            self.sex.delete(0, END)
            self.sex.insert(INSERT, self.dados[nome][2])
            self.func.delete(0, END)
            self.func.insert(INSERT, self.dados[nome][3])
            self.mensagem['text']="Usuário Encontrado!"
        else:
            self.mensagem['text']="Nenhum Usuário encontrado!"
            
    def atualizar(self):
        nome = self.nome.get()
        if nome in list(self.dados.keys()):
            self.dados[nome][0] = self.cpf.get()
            self.dados[nome][1] = self.data.get()
            self.dados[nome][2] = self.sex.get()
            self.dados[nome][3] = self.func.get()
            self.mensagem['text'] = 'Usuário Atualizado!'
            self.listar()
        else:
            self.mensagem['text'] = 'Nenhum usuário encontrado!'
            
            
    def listar(self):
        msg = "{:^24s} {:^24s} {:^24s} {:^24s} {:^24s}\n".format('Nome','CPF','Data','Sexo', 'Função')
        for b in list(self.dados.keys()):
            msg+="{:^24s} {:^24s} {:^24s} {:^24s} {:^24s}\n".format(b, self.dados[b][0],self.dados[b][1],self.dados[b][2],self.dados[b][3])
            
        self.textForm['text'] = msg
        
        
    
    def verificarRegister(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        
        
        if(len(senha)==0):
            self.mensagem['text'] = 'A senha não pode ficar vazia! Crie uma senha.'
        elif(len(senha) <= 6):
            self.mensagem["text"] = "Senha Muito Curta\nTente Novamente!"
        else:

            lista = list(senha)
                
            numeros = 0
            letras = 0
            especiais = 0
            for b in lista:
                if b in '01234567891':
                    numeros +=1
                elif b in 'qwertyuiopasdfghjklçzxcvbnm':
                    letras +=1
                else:
                    especiais += 1
                    
            
            if numeros>0 and letras>0 and especiais>0:
                mensagem= "A senha é Forte.Parabens!"
            elif numeros>0 and letras>0:
                mensagem= "A senha é Intermerdiário.Atenção!"

            else:
                mensagem= "A senha é Facil\nCuidado!"
                return False
            
            if usuario in list(self.users.keys()):
                mensagem = "Registro Já Existe!"

            else:
                self.users.update({usuario:senha})
                mensagem += "\nUsuario Registrado!\nAutentique para Entrar!"
                
            self.mensagem['text'] = mensagem
                
            print("Usuarios:\n {}".format(self.users))
            
         
            
                    

        


        
    
root = Tk()
Aplication(root)
root.mainloop()

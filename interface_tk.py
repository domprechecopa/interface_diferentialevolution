import sys
import datetime
from tkinter import *
from tkinter import ttk
from differential_evolution import DifferentialEvolution
from helpers import interface_tk_support
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from PIL import Image

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    interface_tk_support.set_Tk_var()
    top = Toplevel1 (root)
    interface_tk_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    interface_tk_support.set_Tk_var()
    top = Toplevel1 (w)
    interface_tk_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        #########################
        with open('historico.log', 'w') as log:
            log.write('#'*10 + 'Diferential Evolution' + '#'*10 + '\n\n')
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.mostrarprint = False
        self.funcoes =   ['sphere', 'ackley', 'rosenbrock', 'rastrigin','griewank']
        self.strategys = ['rand1bin','best1bin', 'best2bin', 'rand2bin','randbest1bin',
                          'rand1exp','best1exp','best2exp','rand2exp' ,'randbest1exp']
        self.all_vals = []
        self.avg_vals = []
        self.imgfuncoes = []
        #########################
        for i in self.funcoes:
            self.imgfuncoes.append(Image.open("graphics/"+i + '.png').resize((558,360),Image.ANTIALIAS))

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#ececec' # Closest X11 color: 'gray92' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

##########
        top.geometry("936x633+489+183")
        top.title("Diferencial Revolution")
        top.configure(highlightcolor="black")
        top.resizable(width=False, height=False)
        self.top = top
        self.img = []
#############

        self.Input_Dados = Frame(top)
        self.Input_Dados.place(relx=0.053, rely=0.029, relheight=0.501
                , relwidth=0.155)
        self.Input_Dados.configure(relief='groove')
        self.Input_Dados.configure(borderwidth="2")
        self.Input_Dados.configure(relief='groove')
        self.Input_Dados.configure(width=145)

        self.Label1 = Label(self.Input_Dados)
        self.Label1.place(relx=0.069, rely=0.029, height=22, width=126)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='sw')
        self.Label1.configure(borderwidth="2")
        self.Label1.configure(text='''Número de Iterações''')

        self.Label1_4 = Label(self.Input_Dados)
        self.Label1_4.place(relx=0.069, rely=0.116, height=22, width=106)
        self.Label1_4.configure(activebackground="#f9f9f9")
        self.Label1_4.configure(anchor='sw')
        self.Label1_4.configure(borderwidth="2")
        self.Label1_4.configure(text='''Dim''')

        self.Label1_5 = Label(self.Input_Dados)
        self.Label1_5.place(relx=0.069, rely=0.203, height=22, width=106)
        self.Label1_5.configure(activebackground="#f9f9f9")
        self.Label1_5.configure(anchor='sw')
        self.Label1_5.configure(borderwidth="2")
        self.Label1_5.configure(text='''CR''')

        self.Label1_6 = Label(self.Input_Dados)
        self.Label1_6.place(relx=0.069, rely=0.29, height=22, width=106)
        self.Label1_6.configure(activebackground="#f9f9f9")
        self.Label1_6.configure(anchor='sw')
        self.Label1_6.configure(borderwidth="2")
        self.Label1_6.configure(text='''F''')

        self.Label1_7 = Label(self.Input_Dados)
        self.Label1_7.place(relx=0.069, rely=0.377, height=22, width=106)
        self.Label1_7.configure(activebackground="#f9f9f9")
        self.Label1_7.configure(anchor='sw')
        self.Label1_7.configure(borderwidth="2")
        self.Label1_7.configure(text='''Polupation Size''')

        self.Label1_8 = Label(self.Input_Dados)
        self.Label1_8.place(relx=0.069, rely=0.464, height=22, width=106)
        self.Label1_8.configure(activebackground="#f9f9f9")
        self.Label1_8.configure(anchor='sw')
        self.Label1_8.configure(borderwidth="2")
        self.Label1_8.configure(text='''Upper Limit''')

        self.Label1_9 = Label(self.Input_Dados)
        self.Label1_9.place(relx=0.069, rely=0.551, height=22, width=106)
        self.Label1_9.configure(activebackground="#f9f9f9")
        self.Label1_9.configure(anchor='sw')
        self.Label1_9.configure(borderwidth="2")
        self.Label1_9.configure(text='''Lower Limit''')

        self.Label1_10 = Label(self.Input_Dados)
        self.Label1_10.place(relx=0.069, rely=0.638, height=22, width=106)
        self.Label1_10.configure(activebackground="#f9f9f9")
        self.Label1_10.configure(anchor='sw')
        self.Label1_10.configure(borderwidth="2")
        self.Label1_10.configure(text='''Print Status''')

        self.Label1_1 = Label(self.Input_Dados)
        self.Label1_1.place(relx=0.069, rely=0.725, height=22, width=106)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(anchor='sw')
        self.Label1_1.configure(borderwidth="2")
        self.Label1_1.configure(text='''Function''')

        self.text_num_runs = Label(self.Input_Dados)
        self.text_num_runs.place(relx=0.069, rely=0.812, height=22, width=86)
        self.text_num_runs.configure(activebackground="#f9f9f9")
        self.text_num_runs.configure(anchor='sw')
        self.text_num_runs.configure(borderwidth="2")
        self.text_num_runs.configure(text='''Number Runs''')

        self.text_Strategy = Label(self.Input_Dados)
        self.text_Strategy.place(relx=0.069, rely=0.899, height=22, width=86)
        self.text_Strategy.configure(activebackground="#f9f9f9")
        self.text_Strategy.configure(anchor='sw')
        self.text_Strategy.configure(borderwidth="2")
        self.text_Strategy.configure(text='''Strategy''')

        self.Frame2 = Frame(top)
        self.Frame2.place(relx=0.203, rely=0.029, relheight=0.501
                , relwidth=0.136)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(width=126)

        self.ent_num_iter = Entry(self.Frame2)
        self.ent_num_iter.place(relx=0.08, rely=0.029, height=22, relwidth=0.848)

        self.ent_num_iter.configure(background="white")
        self.ent_num_iter.configure(font="TkFixedFont")
        self.ent_num_iter.configure(selectbackground="#c4c4c4")

        self.ent_dim = Entry(self.Frame2)
        self.ent_dim.place(relx=0.08, rely=0.116,height=22, relwidth=0.848)
        self.ent_dim.configure(background="white")
        self.ent_dim.configure(font="TkFixedFont")
        self.ent_dim.configure(selectbackground="#c4c4c4")

        self.ent_CR = Entry(self.Frame2)
        self.ent_CR.place(relx=0.08, rely=0.203,height=22, relwidth=0.848)
        self.ent_CR.configure(background="white")
        self.ent_CR.configure(font="TkFixedFont")
        self.ent_CR.configure(selectbackground="#c4c4c4")

        self.ent_F = Entry(self.Frame2)
        self.ent_F.place(relx=0.08, rely=0.29,height=22, relwidth=0.848)
        self.ent_F.configure(background="white")
        self.ent_F.configure(font="TkFixedFont")
        self.ent_F.configure(selectbackground="#c4c4c4")

        self.ent_pop_size = Entry(self.Frame2)
        self.ent_pop_size.place(relx=0.08, rely=0.377, height=22, relwidth=0.848)

        self.ent_pop_size.configure(background="white")
        self.ent_pop_size.configure(font="TkFixedFont")
        self.ent_pop_size.configure(selectbackground="#c4c4c4")

        self.ent_upper_lim = Entry(self.Frame2)
        self.ent_upper_lim.place(relx=0.08, rely=0.464, height=22
                , relwidth=0.848)
        self.ent_upper_lim.configure(background="white")
        self.ent_upper_lim.configure(font="TkFixedFont")
        self.ent_upper_lim.configure(selectbackground="#c4c4c4")

        self.ent_lower_lim = Entry(self.Frame2)
        self.ent_lower_lim.place(relx=0.08, rely=0.551, height=22
                , relwidth=0.848)
        self.ent_lower_lim.configure(background="white")
        self.ent_lower_lim.configure(font="TkFixedFont")
        self.ent_lower_lim.configure(selectbackground="#c4c4c4")

        self.Sel_MostrarPrint = Checkbutton(self.Frame2)
        self.Sel_MostrarPrint.place(relx=0.08, rely=0.638, relheight=0.064
                , relwidth=0.544)
        self.Sel_MostrarPrint.configure(activebackground="#f9f9f9")
        self.Sel_MostrarPrint.configure(justify='left')
        self.Sel_MostrarPrint.configure(text='''Mostrar''')
        self.Sel_MostrarPrint.configure(variable=interface_tk_support.che86)

        self.select_funcao = ttk.Combobox(self.Frame2,values = self.funcoes)
        self.select_funcao.place(relx=0.08, rely=0.725, relheight=0.058
                , relwidth=0.780)
        self.select_funcao.configure(takefocus="")
        self.select_funcao.current(0)

        self.style.map('TRadiobutton',background=
              [('selected', _bgcolor), ('active', _ana2color)])
        self.ShowFuncao = ttk.Radiobutton(self.Frame2, command=self.plotarfuncao)
        self.ShowFuncao.place(relx=0.86, rely=0.725, relwidth=0.14
                , relheight=0.0, height=19)
        self.ShowFuncao.configure(takefocus="")

        self.select_strategy = ttk.Combobox(self.Frame2, values = self.strategys)
        self.select_strategy.place(relx=0.08, rely=0.899, relheight=0.058
                , relwidth=0.856)
        self.select_strategy.configure(takefocus="")
        self.select_strategy.current(0)

        self.ent_num_run = Spinbox(self.Frame2, from_=1.0, to=10.0)
        self.ent_num_run.place(relx=0.08, rely=0.812, relheight=0.064
                , relwidth=0.856)
        self.ent_num_run.configure(activebackground="#f9f9f9")
        self.ent_num_run.configure(background="white")
        self.ent_num_run.configure(highlightbackground="black")
        self.ent_num_run.configure(selectbackground="#c4c4c4")

        self.Button1 = Button(top, command = self.limpar_dados)
        self.Button1.place(relx=0.053, rely=0.537, height=30, width=104)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(text='''Limpar Dados''')

        self.Button3 = Button(top,command=self.executar)
        self.Button3.place(relx=0.171, rely=0.537, height=30, width=85)
        self.Button3.configure(activebackground="#f9f9f9")
        self.Button3.configure(state='active')
        self.Button3.configure(text='''Executar''')

        self.Button4 = Button(top, command = self.button_plot)
        self.Button4.place(relx=0.267, rely=0.537, height=30, width=60)
        self.Button4.configure(activebackground="#f9f9f9")
        self.Button4.configure(text='''Plot''')

        self.TProgressbar1 = ttk.Progressbar(top)
        self.TProgressbar1.place(relx=0.053, rely=0.595, relwidth=0.288
                , relheight=0.0, height=19)

        self.credits_text = Label(top)
        self.credits_text.place(relx=0.011, rely=0.914, height=42, width=336)
        self.credits_text.configure(activebackground="#f9f9f9")
        self.credits_text.configure(anchor='nw')
        self.credits_text.configure(borderwidth="2")
        self.credits_text.configure(justify = LEFT)
        self.credits_text.configure(text='''Desenvolvido pelo Laboratório de Modelagem Computacional
Discente: Ana Karina''')

        self.Scrolledlistbox1 = ScrolledListBox(top)
        self.Scrolledlistbox1.place(relx=0.053, rely=0.653, relheight=0.239
                , relwidth=0.906)
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(font="TkFixedFont")
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox1.configure(width=10)

        self.Button2 = Button(top, command= self.limpar_historico)
        self.Button2.place(relx=0.833, rely=0.914, height=30, width=118)
        self.Button2.configure(activebackground="#f9f9f9")
        self.Button2.configure(text='''Limpar Histórico''')

        self.Canvas1 = FigureCanvasTkAgg(self.fig,master = top)
        self.Canvas1.get_tk_widget().place(relx=0.363, rely=0.029, relheight=0.567
                , relwidth=0.589)
        self.Canvas1.get_tk_widget().configure(borderwidth="2")
        self.Canvas1.get_tk_widget().configure(relief='ridge')
        self.Canvas1.get_tk_widget().configure(selectbackground="#c4c4c4")
        self.Canvas1.get_tk_widget().configure(width=551)

        self.prev_grafico = Button(top,state = DISABLED,command=self.prev_grafico_action)
        self.prev_grafico.place(relx=0.363, rely=0.595, height=30, width=45)
        self.prev_grafico.configure(activebackground="#f9f9f9")
        self.prev_grafico.configure(text='''< Prev''')

        self.next_grafico = Button(top, state = DISABLED,command=self.next_grafico_action)
        self.next_grafico.place(relx=0.908, rely=0.595, height=30, width=45)
        self.next_grafico.configure(activebackground="#f9f9f9")
        self.next_grafico.configure(text='''Next >''')

#############BUTTON TEST #########################
        self.Test_Button = Button(top, command = self.test_dados)
        self.Test_Button.place(relx=0.705, rely=0.914, height=27, width=112)
        self.Test_Button.configure(text='''Don't Touch me''')
##################################################

        self.NavegateFrame = Frame(top)
        self.NavegateFrame.place(relx=0.417, rely=0.595, relheight=0.058
                , relwidth=0.486)
        self.NavegateFrame.configure(relief='groove')
        self.NavegateFrame.configure(borderwidth="2")
        self.NavegateFrame.configure(relief='groove')
        self.NavegateFrame.configure(width=455)

        self.toolbar = NavigationToolbar2Tk(self.Canvas1, self.NavegateFrame)
        self.toolbar.update()
        self.Canvas1._tkcanvas.place(relx=0.363, rely=0.029, relheight=0.567
                , relwidth=0.589)
    def executar(self):
            self.dados = {}
            self.dados['Numero de Iteracoes']=[self.ent_num_iter.get(),'int']
            self.dados['Dim'] = [self.ent_dim.get(),'int']
            self.dados['CR']=[self.ent_CR.get(),'float']
            self.dados['F']=[self.ent_F.get(),'float']
            self.dados['Population Size']=[self.ent_pop_size.get(),'int']
            self.dados['Upper Limit']=[self.ent_upper_lim.get(),'float']
            self.dados['Lower Limit']=[self.ent_lower_lim.get(),'float']
            self.dados['Num Runs'] = [self.ent_num_run.get(),'int']
            error = False
            self.comma_dot()
            for i in self.dados.keys():
                try:
                    if(self.dados[i][1] == 'int' ):
                        self.dados[i][0]=int(self.dados[i][0])
                    elif(self.dados[i][1] == 'float'):
                        self.dados[i][0]=float(self.dados[i][0])
                except:
                    self.printar("Erro na Entrada de dados = {}".format(i))
                    error = True
            self.printar("##################################")
            if not error:
                self.run_simulate(self.dados)

    def run_simulate(self,dados):
        self.all_vals = []
        self.avg_vals = []
        self.TProgressbar1["value"] = 0            
        number_of_runs = self.dados['Num Runs'][0]
        self.TProgressbar1["maximum"] = number_of_runs
        val = 0
        print_time = True
        self.img = []
        for i in range(number_of_runs):
            start = datetime.datetime.now()
            de = DifferentialEvolution(num_iterations=dados['Numero de Iteracoes'][0], dim=dados['Dim'][0],
                        CR=dados['CR'][0], F=dados['F'][0], population_size=dados['Population Size'][0], print_status=self.mostrarprint, func=self.select_funcao.get(),
                        upper_limit=dados['Upper Limit'][0],lower_limit=dados['Lower Limit'][0],printar=self.printar, selstrategy = self.select_strategy.get())
            val_temp, all_vals, avg_vals = de.simulate(i)
            val += val_temp
            self.all_vals.append(all_vals)
            self.avg_vals.append(avg_vals)
            if print_time:
                self.printar('')
                self.printar ("Time taken: {}".format( datetime.datetime.now() - start))
                self.printar('')
            self.TProgressbar1["value"] +=1
            self.top.update_idletasks()
        self.printar ('-'*80)
        self.printar('')
        self.printar ("Final average of all runs: {}".format( val / number_of_runs))
        
    def button_plot(self):
        try:
            self.grafico_interface(indice=0)
        except:
            self.printar("Error ao plotar a funcao!")

    def plotarfuncao(self):
        self.fig.clear()
        self.fig.legend(title=self.select_funcao.get())
        self.fig.figimage(self.imgfuncoes[self.funcoes.index(self.select_funcao.get())])
        self.Canvas1.draw()
    def grafico_interface(self, indice=0):
            if indice == None or len(self.all_vals)-1==0:
                self.prev_grafico['state']  = DISABLED
                self.next_grafico['state']  = DISABLED
            elif indice == 0:
                self.prev_grafico['state'] = DISABLED
                self.next_grafico['state'] = NORMAL
            elif indice == len(self.all_vals)-1:
                self.prev_grafico['state']  = NORMAL
                self.next_grafico['state']  = DISABLED
            else:
                self.prev_grafico['state'] = NORMAL
                self.next_grafico['state']  = NORMAL

            self.fig.clear()
            a = self.fig.add_subplot(111)
            a.plot(self.all_vals[indice], 'r', label='Best')
            a.plot(self.avg_vals[indice], 'g', label='Average')
            a.grid(True, linestyle='-.')
            a.legend()
            # a.xlabel('Iterations')
            # a.ylabel('Objective Function Value')
            self.Canvas1.draw()
            self.printar("Grafico = {}".format(indice+1))
            self.grafico = indice
    def printar(self,texto):
        self.Scrolledlistbox1.insert(END,texto)
        self.Scrolledlistbox1.see('end')
        self.top.update_idletasks()
        with open('historico.log', 'a') as log:
            log.write('{}\n'.format(texto))
    def next_grafico_action(self):
        self.grafico+=1
        self.grafico_interface(self.grafico)
        

    def prev_grafico_action(self):
        self.grafico-=1
        self.grafico_interface(self.grafico)
    def comma_dot(self):
        for i in self.dados.keys():
            if self.dados[i][1] == 'float':
                if ',' in self.dados[i][0]:
                    self.dados[i][0] = self.dados[i][0].replace(',','.')
                    
        


    def limpar_historico(self):
        self.Scrolledlistbox1.delete(0, END)
    
    def mostrar_printar_action(self):
        if self.mostrarprint:
            self.mostrarprint = False
            self.printar("Print desabilitado")
            
        else:
            self.mostrarprint = True
            
            self.printar("Print Habilitado")
               
        self.printar('')   
    def limpar_dados(self):
        self.ent_num_iter.delete(0, END)
        self.ent_dim.delete(0, END)
        self.ent_CR.delete(0, END)
        self.ent_F.delete(0, END)
        self.ent_pop_size.delete(0, END)
        self.ent_upper_lim.delete(0, END)
        self.ent_lower_lim.delete(0,END)
        self.TProgressbar1['value'] = 0
        self.select_strategy.current(0)
        self.select_funcao.current(0)

    ############## TEST DADOS ###################
    def test_dados(self):
       # num_iterations=200, dim=10, CR=0.4, F=0.48, population_size=75, print_status=False, func='ackley',upper_limit=5.12,lower_limit=-5.12)
        self.limpar_dados()
        self.ent_num_iter.insert(INSERT, '100')
        self.ent_dim.insert(INSERT, '10')
        self.ent_CR.insert(INSERT, '0,4')
        self.ent_F.insert(INSERT, '0,48')
        self.ent_pop_size.insert(INSERT, '75')
        self.ent_upper_lim.insert(INSERT, '5,12')
        self.ent_lower_lim.insert(INSERT, '-5,12')
        self.select_strategy.current(0)
        self.select_funcao.current(1)

class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):

        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if True:
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() \
                  | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                  + Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, Listbox):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()
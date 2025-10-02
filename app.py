import customtkinter as ctk

# Variaveis 
VALORES_FAIXAS = {
    'Preto': 0, 'Marrom': 1, 'Vermelho': 2, 'Laranja': 3,
    'Amarelo': 4, 'Verde': 5, 'Azul': 6, 'Violeta': 7,
    'Cinza': 8, 'Branco': 9
}

MULTIPLICADORES = {
    'Preto': 1, 'Marrom': 10, 'Vermelho': 100, 'Laranja': 1_000,
    'Amarelo': 10_000, 'Verde': 100_000, 'Azul': 1_000_000,
    'Violeta': 10_000_000, 
    'Dourado': 0.1, 'Prata': 0.01
}

TOLERANCIAS = {
    'Marrom': 1.0, 'Vermelho': 2.0, 'Verde': 0.5, 'Azul': 0.25,
    'Violeta': 0.1, 'Cinza': 0.05, 
    'Dourado': 5.0, 'Prata': 10.0, 'Sem Cor': 20.0
}

faixa1 = 0
faixa2 = 0
mult = 1.0
tol = 0.0

# Aparência 
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

# Janela Principal
app = ctk.CTk()
app.title('Calculadora de Cores de Resistores')
app.geometry('1020x300')

# Funções

def opcaoSelecionadaUm(choice):
    global faixa1
    faixa1 = VALORES_FAIXAS.get(choice, 0)
    return faixa1
        
def opcaoSelecionadaDois(choice):
    global faixa2
    faixa2 = VALORES_FAIXAS.get(choice, 0)
    return faixa2
        
def multiplicador(choice):
    global mult
    mult = MULTIPLICADORES.get(choice, 0)
    return mult
        
def tolerancia(choice):
    global tol
    tol = TOLERANCIAS.get(choice, 0)
    return tol


def resposta():
    num = (faixa1*10+faixa2)*mult
    unidade = "Ω"
    if(num>=1_000_000_000):
        num=num/1_000_000_000
        unidade="GΩ"
    elif(num>=1_000_000):
        num=num/1_000_000
        unidade="MΩ"
    elif(num>=1_000):
        num=num/1_000
        unidade="KΩ"

    resultado.configure(text= f"Resistor {num}{unidade} com {tol}%")


# Campos

#Listar os campos
faixas_valores = list(VALORES_FAIXAS.keys())
faixas_mult = list(MULTIPLICADORES.keys())
faixas_tol = list(TOLERANCIAS.keys())

#Fonte
fonteTitulo = ctk.CTkFont(family="Arial", size=16)
fonteResposta = ctk.CTkFont(family="Arial", size=14)

frame = ctk.CTkFrame(master=app, corner_radius=15, border_width=2, border_color="#3399ff", fg_color="#292436")
frame.pack(pady=10, padx=10, fill="both", expand=True)

faixaUm = ctk.CTkLabel(frame, text='Faixa 1', font=fonteTitulo)
faixaUm.grid(row=0, column=0, padx=30, pady=30)

faixaDois = ctk.CTkLabel(frame, text='Faixa 2', font=fonteTitulo)
faixaDois.grid(row=0, column=1, padx=30, pady=30)

faixaTres = ctk.CTkLabel(frame, text='Faixa 3', font=fonteTitulo)
faixaTres.grid(row=0, column=2, padx=30, pady=30)

faixaQuatro = ctk.CTkLabel(frame, text='Faixa 4', font=fonteTitulo)
faixaQuatro.grid(row=0, column=3, padx=30, pady=30)

opcaoUm = ctk.CTkComboBox(master=frame, values=faixas_valores, command=opcaoSelecionadaUm)
opcaoUm.grid(row=1, column=0, padx=30)

opcaoDois = ctk.CTkComboBox(master=frame, values=faixas_valores, command=opcaoSelecionadaDois)
opcaoDois.grid(row=1, column=1, padx=30)

opcaoTres = ctk.CTkComboBox(master=frame, values=faixas_mult, command=multiplicador)
opcaoTres.grid(row=1, column=2, padx=30)

opcaoQuatro = ctk.CTkComboBox(master=frame, values=faixas_tol, command=tolerancia)
opcaoQuatro.grid(row=1, column=3, padx=30)

botao = ctk.CTkButton(frame, text='Calcular', command=resposta, hover_color="#014588",)
botao.grid(row=1, column=4, padx=30)

resultado = ctk.CTkLabel(frame, text=" ", font=fonteResposta)
resultado.grid(row=2, column=2, padx=20, pady=40)

# Inicialização
app.mainloop()


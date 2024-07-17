#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip  # Biblioteca para copiar texto para a área de transferência

# Criando a janela principal

window = tk.Tk()
window.title("Skin Code")
window.geometry("800x600")  # Ajuste conforme necessário


# Configurações de cores
cores = {
    "clave_of_skin": "#FFD700",  # Amarelo
    "dermatoscopia": "#ADFF2F",  # Verde claro
    "paciente": "#87CEEB",       # Azul claro
    "tecnica": "#FFA07A",        # Salmão
    "esch": "#FFB6C1",           # Rosa claro
    "botao": "#F0F8FF",          # Azul bebê
    "alerta": "#FF6347",         # Vermelho Tomate para alerta
    "normal": "#90EE90"          # Verde claro para normal
}

# Dicionários para os escores
clave_of_skin_scores = {"Vermelha": 1, "Marrom": 2}
dermatoscopia_scores = {"Ausente/NA": 0, "Vermelha": 1, "Marrom": 2, "Cinza": 3}
paciente_scores = {"Sem Bronze": 1, "Com Bronze": 3}
tecnica_scores = {"Glicose": 1, "Laser": 2, "Espuma": 2, "Espuma + Glicose": 3}

# Variáveis para armazenar as escolhas do usuário
clave_of_skin_var = tk.StringVar(value="Vermelha")
dermatoscopia_var = tk.StringVar(value="Ausente/NA")
paciente_var = tk.StringVar(value="Sem Bronze")
tecnica_var = tk.StringVar(value="Glicose")
esch_var = tk.StringVar(value="+/4+")

# Modificação no widget receita_label para utilizar melhor o espaço disponível
receita_label = tk.Label(window, text="", wraplength=750)  # Ajuste o wraplength conforme necessário
receita_label.pack(expand=True, fill='both')

# Função para calcular o escore e mostrar o resultado
def calculate_score():
    score = clave_of_skin_scores[clave_of_skin_var.get()] + \
            dermatoscopia_scores[dermatoscopia_var.get()] + \
            paciente_scores[paciente_var.get()] + \
            tecnica_scores[tecnica_var.get()]

    esch_scale = esch_var.get()
    receita = ""
    if esch_scale == "+/4+":
        receita = "Receita A: Uréia 10% + Ácido glicólico 4% + ..."
    elif esch_scale == "++/4+":
        receita = "Receita B: Ácido Glicólico 5% + Vitamina C 5% + ..."
    elif esch_scale in ["+++/4+", "++++/4+"]:
        receita = "Receita C: Ácido glicólico 8% + Hidroquinona 2% + ..."

    if score > 4:
        escore_label.config(text=f"Escore: {score} - Risco de hiperpigmentação!", bg=cores["alerta"])
    else:
        escore_label.config(text=f"Escore: {score}", bg=cores["normal"])

    receita_label.config(text=receita)

# Função para mostrar a receita com base na escala ESCH
def show_recipe():
    esch_scale = esch_var.get()
    receita = ""
    if esch_scale == "+/4+":
        receita = ("Receita para +/4+: Uréia 10% + Ácido glicólico 4% + Ácido Lático 4% + "
                   "Alfa bisabolol 2% + Óleo Essência Lavanda qsq + Creme não iônico qsq 100 g / "
                   "Aplicar 1 a 2 vezes por dia nas áreas com hiperpigmentação. "
                   "Usar fotoprotetor de amplo espectro e evitar exposição à luz solar durante cerca de dois meses.")
    elif esch_scale == "++/4+":
        receita = ("Receita para ++/4+: Ácido Glicólico 5% + Vitamina C 5% + Ácido Fítico 2% + "
                   "Ácido Kójico 2% + Alfa bisabolol 2% + Ácido glicirrizico 1,5% + Óleo Essencia Lavanda qsq "
                   "creme base + Emoliente qsq 100 g / Aplicar a noite nas áreas com hiperpigmentação e lavar pela manhã. "
                   "Usar fotoprotetor de amplo espectro e evitar exposição à luz solar durante cerca de dois meses.")
    elif esch_scale in ["+++/4+", "++++/4+"]:
        receita = ("Receita para +++/4+ ou ++++/4+: Ácido glicólico 8% + Hidroquinona 2% + Alfa bisabolol 2% + "
                   "Óleo Essência Litsea cubeba qsq + Óleo de amêndoas 5% + Aveia coloidal 5% qsq + Creme não iônico qsq 30 g / "
                   "Aplicar a noite nas áreas com hiperpigmentação e lavar pela manhã, por no máximo 4 semanas. "
                   "Usar fotoprotetor de amplo espectro e evitar exposição à luz solar durante cerca de dois meses.")
    else:
        receita = "Por favor, selecione uma escala ESCH."

    receita_label.config(text=receita)



# Função para copiar a receita para a área de transferência
def copy_recipe():
    receita = receita_label.cget("text")
    pyperclip.copy(receita)
    messagebox.showinfo("Copiado", "Receita copiada para a área de transferência.")

# Função para reiniciar o formulário
def reset_form():
    clave_of_skin_var.set("Vermelha")
    dermatoscopia_var.set("Ausente/NA")
    paciente_var.set("Sem Bronze")
    tecnica_var.set("Glicose")
    esch_var.set("+/4+")
    escore_label.config(text="", bg=cores["normal"])
    receita_label.config(text="")

# Definindo 'receita_label' em um escopo acessível
receita_label = tk.Label(window, text="", wraplength=750)
receita_label.pack(expand=True, fill='both')

def show_recipe():
    esch_scale = esch_var.get()
    receita = ""
    if esch_scale == "+/4+":
        receita = ("Receita para +/4+: Uréia 10% + Ácido glicólico 4% + Ácido Lático 4% + "
                   "Alfa bisabolol 2% + Óleo Essência Lavanda qsq + Creme não iônico qsq 100 g / "
                   "Aplicar 1 a 2 vezes por dia nas áreas com hiperpigmentação. "
                   "Usar fotoprotetor de amplo espectro e evitar exposição à luz solar durante cerca de dois meses.")
    # O restante do código permanece o mesmo...

    receita_label.config(text=receita)

# Adicionando widgets para cada item com cores
tk.Label(window, text="CLAVE of SKIN:", bg=cores["clave_of_skin"]).pack(fill='x')
for option in clave_of_skin_scores:
    ttk.Radiobutton(window, text=option, variable=clave_of_skin_var, value=option).pack()

tk.Label(window, text="Dermatoscopia:", bg=cores["dermatoscopia"]).pack(fill='x')
for option in dermatoscopia_scores:
    ttk.Radiobutton(window, text=option, variable=dermatoscopia_var, value=option).pack()

tk.Label(window, text="Paciente:", bg=cores["paciente"]).pack(fill='x')
for option in paciente_scores:
    ttk.Radiobutton(window, text=option, variable=paciente_var, value=option).pack()

tk.Label(window, text="Técnica:", bg=cores["tecnica"]).pack(fill='x')
for option in tecnica_scores:
    ttk.Radiobutton(window, text=option, variable=tecnica_var, value=option).pack()

tk.Label(window, text="ESCH - Escala de Semiologia de Hiperpigmentação:", bg=cores["esch"]).pack(fill='x')
for option in ["+/4+", "++/4+", "+++/4+", "++++/4+"]:
    ttk.Radiobutton(window, text=option, variable=esch_var, value=option).pack()

# Botões
calculate_button = tk.Button(window, text="Calcular Escore", command=calculate_score, bg=cores["botao"])
calculate_button.pack(fill='x')

show_recipe_button = tk.Button(window, text="Mostrar Receita", command=show_recipe, bg=cores["botao"])
show_recipe_button.pack(fill='x')

copy_button = tk.Button(window, text="Copiar Receita", command=copy_recipe, bg=cores["botao"])
copy_button.pack(fill='x')

reset_button = tk.Button(window, text="Reiniciar", command=reset_form, bg=cores["botao"])
reset_button.pack(fill='x')

# Label para mostrar o escore
escore_label = tk.Label(window, text="", bg=cores["normal"], font=("Helvetica", 12))
escore_label.pack(fill='x')

    
# Função para iniciar a GUI
def run_app():
    window.mainloop()

if __name__ == "__main__":
    run_app()


# In[ ]:





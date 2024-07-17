#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk

# Função para calcular o ITB e avaliar o escore de gravidade
def calcular_itb():
    try:
        # Obter os valores de pressão arterial do formulário
        PAs_MS = float(pas_ms_entry.get())
        PAs_MID_ATA = float(pas_mid_ata_entry.get())
        PAs_MID_ATP = float(pas_mid_atp_entry.get())
        PAs_MIE_ATA = float(pas_mie_ata_entry.get())
        PAs_MIE_ATP = float(pas_mie_atp_entry.get())

        # Calcular o ITB
        ITBd_ATA = PAs_MID_ATA / PAs_MS
        ITBd_ATP = PAs_MID_ATP / PAs_MS
        ITBe_ATA = PAs_MIE_ATA / PAs_MS
        ITBe_ATP = PAs_MIE_ATP / PAs_MS

        # Função para avaliar o escore de gravidade
        def avaliar_escore(ITB, lado, arteria):
            if ITB >= 1.3:
                return f"Não compressível na {arteria} {lado}"
            elif 0.91 <= ITB <= 1.29:
                return f"Normal na {arteria} {lado}"
            elif 0.41 <= ITB <= 0.90:
                return f"DAP leve a moderada na {arteria} {lado}"
            else:
                return f"DAP Grave na {arteria} {lado}"

        # Atualizar os rótulos do resultado com o ITB e o escore de gravidade
        itb_results["text"] = (
            f"ITB à direita na ATA é: {ITBd_ATA}\n"
            f"ITB à direita na ATP é: {ITBd_ATP}\n"
            f"ITB à esquerda na ATA é: {ITBe_ATA}\n"
            f"ITB à esquerda na ATP é: {ITBe_ATP}\n\n"
            f"{avaliar_escore(ITBd_ATA, 'direita', 'ATA')}\n"
            f"{avaliar_escore(ITBd_ATP, 'direita', 'ATP')}\n"
            f"{avaliar_escore(ITBe_ATA, 'esquerda', 'ATA')}\n"
            f"{avaliar_escore(ITBe_ATP, 'esquerda', 'ATP')}"
        )
    except ValueError:
        itb_results["text"] = "Por favor, insira valores válidos para todas as entradas."

# Criar a janela principal
root = tk.Tk()
root.title("Cálculo do Índice Tornozelo-Braço")

# Criar rótulos e campos de entrada para a pressão arterial
labels_texts = [
    "Digite a maior PA Sistólica no membro superior:",
    "Digite PA Sistólica da ATA direita:",
    "Digite PA Sistólica da ATP direita:",
    "Digite PA Sistólica da ATA esquerda:",
    "Digite PA Sistólica da ATP esquerda:"
]

entries = [
    tk.Entry(root) for _ in labels_texts
]

pas_ms_entry, pas_mid_ata_entry, pas_mid_atp_entry, pas_mie_ata_entry, pas_mie_atp_entry = entries

for i, text in enumerate(labels_texts):
    label = tk.Label(root, text=text)
    label.grid(row=i, column=0, sticky="e")
    entries[i].grid(row=i, column=1)

# Botão para calcular o ITB
calc_button = tk.Button(root, text="Calcular ITB", command=calcular_itb)
calc_button.grid(row=5, column=0, columnspan=2)

# Rótulo para exibir os resultados do ITB e o escore de gravidade
itb_results = tk.Label(root, text="", justify=tk.LEFT)
itb_results.grid(row=6, column=0, columnspan=2, sticky="w")

# Iniciar o loop principal do Tkinter
root.mainloop()


# In[ ]:





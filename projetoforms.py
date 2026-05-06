from tkinter import *
from tkinter import ttk
from tkinter import messagebox

janela = Tk()
janela.title("Cadastro de Pacientes")
janela.geometry("700x600") # Aumentei um pouco a altura para caber tudo

# Criando as abas
abas = ttk.Notebook(janela)
abas.pack(fill="both", expand=True)

aba1 = Frame(abas)
abas.add(aba1, text="Cadastro de Pacientes")

aba2 = Frame(abas)
abas.add(aba2, text="Pacientes Cadastrados")

# --- Campos da Aba 1 ---

Label(aba1, text="Nome Completo").pack(pady=5)
entry_nome = Entry(aba1, width=40)
entry_nome.pack()

Label(aba1, text="CPF").pack(pady=5)
entry_cpf = Entry(aba1, width=40)
entry_cpf.pack()

Label(aba1, text="Data de Nascimento").pack(pady=5)
entry_data = Entry(aba1, width=40)
entry_data.pack()

Label(aba1, text="Telefone").pack(pady=5)
entry_telefone = Entry(aba1, width=40)
entry_telefone.pack()

Label(aba1, text="Email").pack(pady=5)
entry_email = Entry(aba1, width=40)
entry_email.pack()

Label(aba1, text="Convênios / SUS").pack(pady=5)
# CORREÇÃO: Variáveis não podem ter "/" no nome. Use "_" (underline).
# A / e divisão 
entry_convenios_sus = Entry(aba1, width=40)
entry_convenios_sus.pack()

Label(aba1, text="Contatos de Emergência").pack(pady=5)
entry_contatos = Entry(aba1, width=40)
entry_contatos.pack()

# Função simples para o botão
def cadastrar():
    messagebox.showinfo("Sucesso", "Paciente cadastrado com sucesso!")

# Botão de cadastro
# CORREÇÃO: Faltava uma vírgula após o 'text'
Button(
    aba1,
    text="Cadastrar Paciente",
    bg="green",
    fg="white",
    width=20,
    command=cadastrar
).pack(pady=20)



janela.mainloop()
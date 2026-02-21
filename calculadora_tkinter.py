import tkinter as tk

# ----------------------------
# Lógica de la calculadora
# ----------------------------
def agregar(valor: str) -> None:
    """Añade un caracter a la pantalla."""
    entrada.set(entrada.get() + valor)

def limpiar() -> None:
    """Limpia toda la pantalla."""
    entrada.set("")

def borrar() -> None:
    """Borra el último caracter."""
    entrada.set(entrada.get()[:-1])

def calcular() -> None:
    """Evalúa la expresión de la pantalla."""
    expr = entrada.get().strip()
    if not expr:
        return
    try:
        # Evalúa expresión aritmética básica (ej: 2+3*4)
        resultado = eval(expr, {"__builtins__": None}, {})
        entrada.set(str(resultado))
    except Exception:
        entrada.set("Error")


# ----------------------------
# UI (Tkinter)
# ----------------------------
root = tk.Tk()
root.title("Calculadora")
root.resizable(False, False)

entrada = tk.StringVar()

pantalla = tk.Entry(
    root,
    textvariable=entrada,
    font=("Arial", 20),
    justify="right",
    bd=10,
    relief="ridge",
    width=16
)
pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botones: texto, fila, columna, comando
botones = [
    ("C", 1, 0, limpiar), ("⌫", 1, 1, borrar), ("%", 1, 2, lambda: agregar("%")), ("/", 1, 3, lambda: agregar("/")),
    ("7", 2, 0, lambda: agregar("7")), ("8", 2, 1, lambda: agregar("8")), ("9", 2, 2, lambda: agregar("9")), ("*", 2, 3, lambda: agregar("*")),
    ("4", 3, 0, lambda: agregar("4")), ("5", 3, 1, lambda: agregar("5")), ("6", 3, 2, lambda: agregar("6")), ("-", 3, 3, lambda: agregar("-")),
    ("1", 4, 0, lambda: agregar("1")), ("2", 4, 1, lambda: agregar("2")), ("3", 4, 2, lambda: agregar("3")), ("+", 4, 3, lambda: agregar("+")),
    ("0", 5, 0, lambda: agregar("0")), (".", 5, 1, lambda: agregar(".")), ("=", 5, 2, calcular),
]

for (texto, fila, col, cmd) in botones:
    # El botón "=" lo hacemos más ancho
    if texto == "=":
        b = tk.Button(root, text=texto, width=10, height=2, font=("Arial", 16), command=cmd)
        b.grid(row=fila, column=col, columnspan=2, padx=5, pady=5, sticky="we")
    else:
        b = tk.Button(root, text=texto, width=5, height=2, font=("Arial", 16), command=cmd)
        b.grid(row=fila, column=col, padx=5, pady=5)

# Tecla Enter = calcular, Escape = limpiar
root.bind("<Return>", lambda _: calcular())
root.bind("<Escape>", lambda _: limpiar())

root.mainloop()
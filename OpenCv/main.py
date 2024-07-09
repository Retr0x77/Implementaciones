from ultralytics import YOLO
from tkinter import filedialog, messagebox, Tk, Label, Button, Frame, Canvas
import cv2
import math
import os


# Función para analizar la imagen
def Analizar(imagen, op):
    model = YOLO('model/best.pt')
    result = model(imagen)
    for res in result:
        boxes = res.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            if x1 < 0: x1 = 0
            if y1 < 0: y1 = 0
            if x2 < 0: x2 = 0
            if y2 < 0: y2 = 0

            cls = int(box.cls[0])
            conf = math.ceil(box.conf[0])

            cv2.rectangle(imagen, (x1, y1), (x2, y2), (255, 0, 0), 2)
            text = f'Fuego {int(conf * 100)}%'
            cv2.putText(imagen, text, (x1, y1 - 5), cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 1)
            if conf > 0.5:
                print("INCENDIO DETECTADO!")

    cv2.imshow("Image", imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Interfaz gráfica
def main_app():
    root = Tk()
    root.title("Detector de Fuego")
    #root.iconbitmap('icon.ico')

    # Estilos
    bg_color = "#333333"
    btn_color = "#ff5722"
    text_color = "#ffffff"

    root.configure(bg=bg_color)

    # Marco para los botones y etiquetas
    frame = Frame(root, bg=bg_color)
    frame.pack(pady=20)

    # Etiqueta de bienvenida
    welcome_label = Label(frame, text="Bienvenido al Detector de Fuego", font=("Helvetica", 16), bg=bg_color,
                          fg=text_color)
    welcome_label.grid(row=0, column=0, columnspan=2, pady=10)

    # Botón para seleccionar imagen
    select_button = Button(frame, text="Seleccionar Imagen", command=lambda: seleccionar_imagen(root), bg=btn_color,
                           fg=text_color, relief='flat')
    select_button.grid(row=1, column=0, padx=10)

    # Botón para salir
    exit_button = Button(frame, text="Salir", command=root.destroy, bg=btn_color, fg=text_color, relief='flat')
    exit_button.grid(row=1, column=1, padx=10)

    root.mainloop()


# Función para seleccionar imagen
def seleccionar_imagen(root):
    messagebox.showinfo(title="Aviso", message="Para mejores resultados, seleccione una imagen con resolución 416x416")
    filename = filedialog.askopenfilename(title="Buscar archivo JPG",
                                          filetypes=[("Archivos JPG", "*.jpg")])
    if filename:
        messagebox.showinfo(title="Aviso", message="Imagen seleccionada con éxito")
        imagen = cv2.imread(filename)
        Analizar(imagen, 1)
    else:
        messagebox.showerror(title="Aviso", message="No se seleccionó una imagen")


if __name__ == "__main__":
    main_app()

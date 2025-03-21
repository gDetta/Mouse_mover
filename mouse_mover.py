import pyautogui
import time
import threading
import tkinter as tk
import tkinter.messagebox as messagebox
import os
import sys


# Flag per interrompere il movimento
stop_movement = True
# GUI start/stop button
toggle_button = None


def resource_path(relative_path):
    """ Get the absolute path to the resource (icon) file. """
    try:
        # When running as a PyInstaller executable
        base_path = sys._MEIPASS
    except AttributeError:
        # When running as a regular Python script
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Example: Setting the icon path
icon_path = resource_path("mouse.ico")



# Funzione per rilevare il movimento del mouse
def detect_mouse_movement():
    global stop_movement
    last_position = pyautogui.position()
    # Soglia per rilevare il movimento manuale (in pixel)
    MOVEMENT_THRESHOLD = 10

    while not stop_movement:
        new_position = pyautogui.position()
        # Calcola la distanza tra la posizione attuale e quella precedente
        distance = ((new_position[0] - last_position[0]) ** 2 + (new_position[1] - last_position[1]) ** 2) ** 0.5

        if distance > MOVEMENT_THRESHOLD:
            toggle_movement()
            messagebox.showinfo("Info", "Mouse mover interrotto dal movimento manuale del mouse")
            print("Movimento interrotto dal movimento manuale del mouse.")

        last_position = new_position
        time.sleep(0.1)   # sec


# Funzione per muovere leggermente il mouse
def move_mouse():
    global stop_movement
    selector = True
    x, y = pyautogui.position()

    while not stop_movement:
        if selector:
            pyautogui.moveTo(x + 1, y + 1)
            selector = False
        else:
            pyautogui.moveTo(x-1, y-1)
            selector = True
        time.sleep(2)  # sec


# Funzione per avviare o fermare il movimento
def toggle_movement():
    global stop_movement
    global toggle_button
    
    # Start
    if stop_movement==True:
        stop_movement = False
        threading.Thread(target=detect_mouse_movement).start()
        threading.Thread(target=move_mouse).start()
        # Set buttons for stop
        toggle_button.config(text="Stop", bg="red")

    # Stop
    else:
        stop_movement = True
        # Set buttons for start
        toggle_button.config(text="Start", bg="green")


# Creazione dell'interfaccia grafica
def create_gui():
    global toggle_button
    root = tk.Tk()
    root.title("Mouse Mover")
    root.geometry("320x150")

    # Aggiunta di un'icona
    # icon_path = os.path.join(os.path.dirname(__file__), 'mouse.ico')
    if os.path.exists(icon_path):
        root.iconbitmap(icon_path)

    # Buttons
    toggle_button = tk.Button(root, text="Start", command=lambda: toggle_movement(), width=15, height=2, bg="green")
    toggle_button.pack(pady=5)

    exit_button = tk.Button(root, text="Exit", command=root.quit, width=15, height=2)
    exit_button.pack(pady=5)

    root.mainloop()



#===========================================================================================================================

# Avvio della GUI
if __name__ == "__main__":
    create_gui()


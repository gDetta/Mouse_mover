# 🖱️ Mouse Mover

A simple Python script that simulates mouse movement to prevent screen sleep or lock.

The script includes a GUI to easily start and stop the movement, and is able to detect manual mouse movement to stop automatically.

---

## 🚀 **Features**

* Moves the mouse slightly to prevent screen lock
* Stops automatically if manual mouse movement is detected
* GUI with start/stop button that changes color (green = ON, red = OFF)
* Notification popup when the movement stops duo to manual mouse movement

---

## 🛠️ **Usage**

1. Run the script
2. The GUI will appear:
   * **Green "Start" button** → Starts the mouse movement
   * **Red "Stop" button** → Stops the movement
   * **Exit button** → Closes the application

---

## 🖥️ Create the Executable (pyinstaller)

* Install the necessary dependencies, using  `pip`
* Create .exe with `pyinstaller`:
  `pyinstaller --noconsole --icon=mouse.ico --add-data "mouse.ico;." mouse_mover.py`




import keyboard
from pynput.mouse import Listener

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Mouse clicked at ({x}, {y})")
    

def main():
    
    started = False
    print("Press 'j' to start the loop, 'k' to stop and exit.")

    while True:
        if keyboard.is_pressed('j') and started == False :
            print("Loop started.")
            started = True
            listener = Listener(on_click=on_click)
            listener.start()    

        if keyboard.is_pressed('k') and started == True :
            print("Loop stopped and exiting.")
            listener.stop()
            break

if __name__ == "__main__":
    main()

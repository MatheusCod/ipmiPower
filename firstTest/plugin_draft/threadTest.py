import threading

glob_var = 0;

def abc():
    global glob_var
    glob_var = 5

def thr():
    # Class for threading
    class saveDB(threading.Thread):
      def __init__(self):
        threading.Thread.__init__(self)
      def run(self):
        global glob_var
        print(glob_var)
        while (True):
            print(glob_var)
            if (glob_var >= 9999999):
                break

    # Create thread
    thread = saveDB()
    thread.start()

def main():
    thr()
    global glob_var
    print("123")
    print(glob_var)

    while (True):
        glob_var += 1
        if (glob_var >= 15000000):
            print(glob_var)
            break

    print("Agora sim")    

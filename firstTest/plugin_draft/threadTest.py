import threading

glob_var = 0;

def abc():
    global glob_var
    glob_var = 5

def th_while(aux):
    aux = aux + 10
    global glob_var
    print(glob_var)
    while (True):
        print(glob_var)
        if (glob_var >= 9999999):
            break

thread_list = []
def main():
    thread = threading.Thread(target=th_while, args=(5,))
    thread_list.append(thread)
    thread.start()
    global glob_var
    print("123")
    print(glob_var)

    while (True):
        glob_var += 1
        if (glob_var >= 15000000):
            print(glob_var)
            break

    print("Agora sim")

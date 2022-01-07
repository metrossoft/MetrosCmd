import os
import sys
import metros
import shlex
import platform
import hashlib
import getpass
import smtplib
import configparser
import socket 
import traceback
from threading import Thread, Lock
from queue import Queue
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from colorama import Fore, Back
from colorama import init as colorama_init
colorama_init(autoreset=True)
__help__ = """Metros Command Line Interpreter [version 3.2 2021]
$cmd                  — Executing windows console commands.
    Syntax:
        $cmd <parameter>
Bf                    — Brudforce hash. 
    Argument:
        •   --md5
        •   --sha1
        •   --sha256
        •   --sha384
        •   --sha512
    Syntax:
        bf <argument> <hash> <filename> — Dictionary hash brute force.
Cd                    — Changes the current directory.
Clean                 — Cleaning console. Other parameters: clear or cls.
Hash                  — Hash function.
    Argument:
        •   --md5
        •   --sha1
        •   --sha256
        •   --sha384
        •   --sha512
    Syntax:
        hash <argument> <hash> — Output of the selected hash.
        hash <argument> <hash> == <parameter> — Comparing the selected hash with the text.
Help                  — Displaying help information about commands.
Mailing               — Sending messages to mail.
    Argument:
        •   --file
        •   --text
    Syntax:
        mailing <from> <to> <subject> <argument> <host> — Sending a message.
Mailing_authorization — Server authorization to send messages to mail.
Port_scanner          — Port scanner.
    Syntax:
        port_scanner <host> <port_range> — Port scanning.
Process               — Process function.
    Argument:
        •   --kill  — Completing the process.
        •   --start — Process start.
        •   --startfile — File start.
        •   --run — Checking the existence of a process.
        •   --getpid — Outputting the pid of a process.
        •   --getpid and -l — Outputting the pid of all processes.
        •   --getpath — Process location output.
        •   --injector — Dll file injection into the process.
    Syntax:
        process <argument> — Process command execution.
        process --injector <process> <file> — Injecting a dll file into a process.
Quit                  — Exit the program. Other parameters: quit or exit.
Viso                  — Text editor.
    Syntax:
        viso <filename> — Edits the selected file if you do not specify the parameter, the unnamed.txt file will be created.
Windows               — Windows activation.
Argv — The argv [] parameter is an array of pointers to strings. 
       Only string data can be passed through the command line. 
       Pointers and strings are two big topics that have separate sections for them. 
       So it is through the argv [] parameter that any information is transmitted.
    Argument:
        •   --version or -v — Displaying the program version.
    Syntax:
        {} <argument> — Execute command.""".format(sys.argv[0])
class Root:
    def __init__(self):
        super().__init__()
        os.system("cls")
        print("[*] Welcome to command line interpreter [version 3.2].")
        print("\n[*] Detailed information on the website: metros-software.ru")
        print("[*] Technical support metros:            metrostechnicalsupp0rt@gmail.com")
        self.start = True
        while self.start:
            os.system("title Command Line Interpreter [{}]".format(os.path.splitdrive(os.getcwd())[1].replace("\\", "/")))
            self.init()
    def init(self):
        self.out = input("\n"+Fore.LIGHTGREEN_EX  +"{}@{}{}:{} {}{}{} $ {}".format(os.getlogin(), platform.node(), Fore.WHITE, Fore.WHITE, Fore.LIGHTCYAN_EX, os.path.splitdrive(os.getcwd())[1].replace("\\", "/"),Fore.WHITE, Fore.WHITE)).replace("\\", "/")
        if self.out.replace(" ", "") != "":
            try:    
                self.command()
            except:
                pass
    def command(self):
        self.inp = shlex.split(self.out)
        if str(self.inp[0]).lower() == "exit" or str(self.inp[0]).lower() == "quit":
            self.start = False
        if str(self.inp[0]).lower() == "cls" or str(self.inp[0]).lower() == "clear" or str(self.inp[0]).lower() == "clean":
            os.system("cls")
        if str(self.inp[0]).lower() == "cd":
            os.chdir(self.inp[1]) 
        if str(self.inp[0]).lower() == "hash" and str(self.inp[1]).lower() == "--md5":
            print(self.inp[2]+" -> "+hashlib.md5(str(self.inp[2]).encode("utf-8")).hexdigest())
        if str(self.inp[0]).lower() == "hash" and str(self.inp[1]).lower() == "--sha1":
            print(hashlib.sha1(str(self.inp[2]).encode("utf-8")).hexdigest())
        if str(self.inp[0]).lower() == "hash" and str(self.inp[1]).lower() == "--sha224":
            print(hashlib.sha224(str(self.inp[2]).encode("utf-8")).hexdigest())
        if str(self.inp[0]).lower() == "hash" and str(self.inp[1]).lower() == "--sha256":
            print(hashlib.sha256(str(self.inp[2]).encode("utf-8")).hexdigest())
        if str(self.inp[0]).lower() == "hash" and str(self.inp[1]).lower() == "--sha384":
            print(hashlib.sha384(str(self.inp[2]).encode("utf-8")).hexdigest())
        if str(self.inp[0]).lower() == "hash" and str(self.inp[1]).lower() == "--sha512":
            print(hashlib.sha512(str(self.inp[2]).encode("utf-8")).hexdigest())
        if str(self.inp[0]).lower() == "hash" and str(self.inp[1]).lower() == "--md5" and str(self.inp[3]).replace(" ", "") == "==":
            print(str(self.inp[2])+" == "+hashlib.md5(str(self.inp[4]).encode("utf-8")).hexdigest())
            if str(self.inp[2]) == hashlib.md5(str(self.inp[4]).encode("utf-8")).hexdigest():
                print(Fore.GREEN+"True"+Fore.WHITE)
            else:
                print(Fore.RED+"False"+Fore.WHITE)
        if str(self.inp[0]).lower() == "hash" and str(self.inp[1]).lower() == "--sha1" and str(self.inp[3]).replace(" ", "") == "==":
            print(str(self.inp[2])+" == "+hashlib.sha1(str(self.inp[4]).encode("utf-8")).hexdigest())
            if str(self.inp[2]) == hashlib.sha1(str(self.inp[4]).encode("utf-8")).hexdigest():
                print(Fore.GREEN+"True"+Fore.WHITE)
            else:
                print(Fore.RED+"False"+Fore.WHITE)
        if str(self.inp[0]).lower() == "hash" and str(self.inp[1]).lower() == "--sha224" and str(self.inp[3]).replace(" ", "") == "==":
            print(str(self.inp[2])+" == "+hashlib.sha224(str(self.inp[4]).encode("utf-8")).hexdigest())
            if str(self.inp[2]) == hashlib.sha224(str(self.inp[4]).encode("utf-8")).hexdigest():
                print(Fore.GREEN+"True"+Fore.WHITE)
            else:
                print(Fore.RED+"False"+Fore.WHITE)
        if str(self.inp[0]).lower() == "hash" and str(self.inp[1]).lower() == "--sha256" and str(self.inp[3]).replace(" ", "") == "==":
            print(str(self.inp[2])+" == "+hashlib.sha256(str(self.inp[4]).encode("utf-8")).hexdigest())
            if str(self.inp[2]) == hashlib.sha256(str(self.inp[4]).encode("utf-8")).hexdigest():
                print(Fore.GREEN+"True"+Fore.WHITE)
            else:
                print(Fore.RED+"False"+Fore.WHITE)
        if str(self.inp[0]).lower() == "hash" and str(self.inp[1]).lower() == "--sha384" and str(self.inp[3]).replace(" ", "") == "==":
            print(str(self.inp[2])+" == "+hashlib.sha384(str(self.inp[4]).encode("utf-8")).hexdigest())
            if str(self.inp[2]) == hashlib.sha384(str(self.inp[4]).encode("utf-8")).hexdigest():
                print(Fore.GREEN+"True"+Fore.WHITE)
            else:
                print(Fore.RED+"False"+Fore.WHITE)
        if str(self.inp[0]).lower() == "hash" and str(self.inp[1]).lower() == "--sha512" and str(self.inp[3]).replace(" ", "") == "==":
            print(str(self.inp[2])+" == "+hashlib.sha512(str(self.inp[4]).encode("utf-8")).hexdigest())
            if str(self.inp[2]) == hashlib.sha512(str(self.inp[4]).encode("utf-8")).hexdigest():
                print(Fore.GREEN+"True"+Fore.WHITE)
            else:
                print(Fore.RED+"False"+Fore.WHITE)
        if str(self.inp[0]).lower() == "bf" and str(self.inp[1]).lower() == "--md5":
            try:
                pass_file = open (str(self.inp[3]), "r")
            except:
                pass
            for word in pass_file:
                enc_wrd = word.encode("utf-8")
                digest = hashlib.md5(enc_wrd.strip()).hexdigest()
                if digest == str(self.inp[2]):
                    print(str(self.inp[2])+" -> "+word)
                    print(Fore.GREEN+"Yes"+Fore.WHITE)
                else:
                    print(Fore.RED+"No results"+Fore.WHITE)
        if str(self.inp[0]).lower() == "bf" and str(self.inp[1]).lower() == "--sha1":
            try:
                pass_file = open (str(self.inp[3]), "r")
            except:
                pass
            for word in pass_file:
                enc_wrd = word.encode("utf-8")
                digest = hashlib.sha1(enc_wrd.strip()).hexdigest()
                if digest == str(self.inp[2]):
                    print(str(self.inp[2])+" -> "+word)
                    print(Fore.GREEN+"Yes"+Fore.WHITE)
                else:
                    print(Fore.RED+"No results"+Fore.WHITE)   
        if str(self.inp[0]).lower() == "bf" and str(self.inp[1]).lower() == "--sha224":
            try:
                pass_file = open (str(self.inp[3]), "r")
            except:
                pass
            for word in pass_file:
                enc_wrd = word.encode("utf-8")
                digest = hashlib.sha224(enc_wrd.strip()).hexdigest()
                if digest == str(self.inp[2]):
                    print(str(self.inp[2])+" -> "+word)
                    print(Fore.GREEN+"Yes"+Fore.WHITE)
                else:
                    print(Fore.RED+"No results"+Fore.WHITE)   
        if str(self.inp[0]).lower() == "bf" and str(self.inp[1]).lower() == "--sha256":
            try:
                pass_file = open (str(self.inp[3]), "r")
            except:
                pass
            for word in pass_file:
                enc_wrd = word.encode("utf-8")
                digest = hashlib.sha256(enc_wrd.strip()).hexdigest()
                if digest == str(self.inp[2]):
                    print(str(self.inp[2])+" -> "+word)
                    print(Fore.GREEN+"Yes"+Fore.WHITE)
                else:
                    print(Fore.RED+"No results"+Fore.WHITE)   
        if str(self.inp[0]).lower() == "bf" and str(self.inp[1]).lower() == "--sha384":
            try:
                pass_file = open (str(self.inp[3]), "r")
            except:
                pass
            for word in pass_file:
                enc_wrd = word.encode("utf-8")
                digest = hashlib.sha384(enc_wrd.strip()).hexdigest()
                if digest == str(self.inp[2]):
                    print(str(self.inp[2])+" -> "+word)
                    print(Fore.GREEN+"Yes"+Fore.WHITE)
                else:
                    print(Fore.RED+"No results"+Fore.WHITE)       
        if str(self.inp[0]).lower() == "bf" and str(self.inp[1]).lower() == "--sha512":
            try:
                pass_file = open (str(self.inp[3]), "r")
            except:
                pass
            for word in pass_file:
                enc_wrd = word.encode("utf-8")
                digest = hashlib.sha512(enc_wrd.strip()).hexdigest()
                if digest == str(self.inp[2]):
                    print(str(self.inp[2])+" -> "+word)
                    print(Fore.GREEN+"Yes"+Fore.WHITE)
                    break
                else:
                    print(Fore.RED+"No results"+Fore.WHITE)    
        if str(self.inp[0]).lower() == "process" and str(self.inp[1]).lower() == "--kill":
            os.system("taskkill /im {} /f>nul".format(str(self.inp[2])))
        if str(self.inp[0]).lower() == "process" and str(self.inp[1]).lower() == "--start":
            os.system("start {}".format(str(self.inp[2])))
        if str(self.inp[0]).lower() == "process" and str(self.inp[1]).lower() == "--startfile":
            os.startfile(str(self.inp[2]))
        if str(self.inp[0]).lower() == "process" and str(self.inp[1]).lower() == "--run":
            if metros.process_running(str(self.inp[2])) == True:
                print(Fore.GREEN+"True"+Fore.WHITE)
            else:
                print(Fore.RED+"False"+Fore.WHITE)
        if str(self.inp[0]).lower() == "process" and str(self.inp[1]).lower() == "--getpid":
            print(str(self.inp[2])+" -> "+str(metros.getpid(str(self.inp[2]))[0]))
        if str(self.inp[0]).lower() == "process" and str(self.inp[2]).lower() == "--getpid" and str(self.inp[1]).lower() == "-l":
            print(str(self.inp[3])+" -> "+str(metros.getpid(str(self.inp[3]))))
        if str(self.inp[0]).lower() == "process" and str(self.inp[1]).lower() == "--getpath":
            print(str(self.inp[2])+" -> "+str(metros.getpid_path(str(self.inp[2]))))
        if str(self.inp[0]).lower() == "process" and str(self.inp[1]).lower() == "--injector":
            injector = metros.injector()
            injector.load_from_pid(int(metros.getpid(str(self.inp[2]))[0]))
            injector.inject_dll(str(self.inp[3]))
            injector.unload()
        if str(self.inp[0]).lower() == "viso":
                try:
                    print("[*] Editing a file {} to exit press the keyboard shortcut Ctrl + Z.\n".format(str(self.inp[1])))
                    os.system("copy con {}".format(self.inp[1]))
                except:
                    print("[*] Editing a file {} to exit press the keyboard shortcut Ctrl + Z.\n".format("unnamed.txt"))
                    os.system("copy con {}".format("unnamed.txt"))
        if str(self.inp[0]).lower() == "windows":
            print("\nMetros windows activation version 1.1\n")
            print("+========================================================================+=================================+")
            print("| Windows                                                                | Key                             |")
            print("+====+===================================================================+=================================+")
            print ("| 1 | Windows 10 home activation                                         | TX9XD-98N7V-6WMQ6-BX7FG-H8Q99   |")
            print ("| 2 | Home Single Language                                               | 7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH   |")
            print ("| 3 | Educational (1)                                                    | NW6C2-QMPVW-D7KKK-3GKT6-VCFB2   |")
            print ("| 4 | Educational (2)                                                    | 72RPG-7NV8T-TVQKR-7RRRW-78RBY   |")
            print ("| 5 | Enterprise                                                         | ND4DX-39KJY-FYWQ9-X6XKT-VCFCF   |")
            print ("| 6 | Enterprise LSTB                                                    | 7YMNV-PG77F-K66KT-KG9VQ-TCQGB   |")
            print ("| 7 | Windows 10 Enterprise (Core)                                       | KTNPV-KTRK4-3RRR8-39X6W-W44T3   |")
            print ("| 8 | Windows 10 Enterprise for Core Single Language                     | BT79Q-G7N6G-PGBYW-4YWX6-6F4BT   |")
            print ("| 9 | Windows 10 Pro Activation (1)                                      | W269N-WFGWX-YVC9B-4J6C9-T83GX   |")
            print ("|10 | Windows 10 Pro Activation (2)                                      | 8N67H-M3CY9-QT7C4-2TR7M-TXYCV   |")
            print ("| 0 | Enter your activation key                                          | XXXXX-XXXXX-XXXXX-XXXXX-XXXXX   |")
            print("+====+===================================================================+=================================+")
            print("| Quit or Exit - exit.                                                                                     |")
            print("+========================================================================+=================================+")
            try:
                ui = input("Choice: ")
            except:
                pass
            if ui == "1":
                os.system("slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99")
                os.system("slmgr /skms kms.xspace.in")
                os.system("slmgr /ato")
                print("\n============================================================================================================")
                print("Windows 10 Home Activation")
                print("============================================================================================================")
                print("slmgr / ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99")
                print("slmgr / skms kms.xspace.in")
                print("slmgr / ato")
                print("============================================================================================================\n")
            if ui == "2":
                os.system("slmgr /ipk 7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH")
                os.system("slmgr /skms kms.xspace.in")
                os.system("slmgr /ato")
                print("\n============================================================================================================")
                print("Home Single Language")
                print("============================================================================================================")
                print("slmgr /ipk 7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH")
                print("slmgr /skms kms.xspace.in")
                print("slmgr /ato")
                print("============================================================================================================\n")
            if ui == "3":
                os.system("slmgr /ipk NW6C2-QMPVW-D7KKK-3GKT6-VCFB2")
                os.system("slmgr /skms kms.xspace.in")
                os.system("slmgr /ato")
                print("\n============================================================================================================")
                print("For educational institutions (1)")
                print("============================================================================================================")
                print("slmgr /ipk NW6C2-QMPVW-D7KKK-3GKT6-VCFB2")
                print("slmgr /skms kms.xspace.in")
                print("slmgr /ato")
                print("============================================================================================================\n")
            if ui == "4":
                os.system("slmgr /ipk 72RPG-7NV8T-TVQKR-7RRRW-78RBY")
                os.system("slmgr /skms kms.xspace.in")
                os.system("slmgr /ato")
                print("\n============================================================================================================")
                print("For educational institutions (2)")
                print("============================================================================================================")
                print("slmgr /ipk 72RPG-7NV8T-TVQKR-7RRRW-78RBY")
                print("slmgr /skms kms.xspace.in")
                print("slmgr /ato")
                print("============================================================================================================\n")
            if ui == "5":
                os.system("slmgr /ipk ND4DX-39KJY-FYWQ9-X6XKT-VCFCF")
                os.system("slmgr /skms kms.xspace.in")
                os.system("slmgr /ato")
                print("\n============================================================================================================")
                print("For enterprises (Enterprise)")
                print("============================================================================================================")
                print("slmgr /ipk ND4DX-39KJY-FYWQ9-X6XKT-VCFCF")
                print("slmgr /skms kms.xspace.in")
                print("slmgr /ato")
                print("============================================================================================================\n")
            if ui == "6":
                os.system("slmgr /ipk 7YMNV-PG77F-K66KT-KG9VQ-TCQGB")
                os.system("slmgr /skms kms.xspace.in")
                os.system("slmgr /ato")
                print("\n============================================================================================================")
                print("For enterprises (Enterprise LSTB)")
                print("============================================================================================================")
                print("slmgr /ipk 7YMNV-PG77F-K66KT-KG9VQ-TCQGB")
                print("slmgr /skms kms.xspace.in")
                print("slmgr /ato")
                print("============================================================================================================\n")
            if ui == "7":
                os.system("slmgr /ipk KTNPV-KTRK4-3RRR8-39X6W-W44T3")
                os.system("slmgr /skms kms.xspace.in")
                os.system("slmgr /ato")
                print("\n============================================================================================================")
                print("Windows 10 Enterprise (Core)")
                print("============================================================================================================")
                print("slmgr /ipk KTNPV-KTRK4-3RRR8-39X6W-W44T3")
                print("slmgr /skms kms.xspace.in")
                print("slmgr /ato")
                print("============================================================================================================\n")
            if ui == "8":
                os.system("slmgr /ipk BT79Q-G7N6G-PGBYW-4YWX6-6F4BT")
                os.system("slmgr /skms kms.xspace.in")
                os.system("slmgr /ato")
                print("\n============================================================================================================")
                print("Windows 10 Enterprise for one language (Core Single Language)")
                print("============================================================================================================")
                print("slmgr /ipk BT79Q-G7N6G-PGBYW-4YWX6-6F4BT")
                print("slmgr /skms kms.xspace.in")
                print("slmgr /ato")
                print("============================================================================================================\n")
            if ui == "9":
                os.system("slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
                os.system("slmgr /skms kms.xspace.in")
                os.system("slmgr /ato")
                print("\n============================================================================================================")
                print("Windows 10 Pro Activation (1)")
                print("============================================================================================================")
                print("slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
                print("slmgr /skms kms.xspace.in")
                print("slmgr /ato")
                print("============================================================================================================\n")
            if ui == "10":
                os.system("slmgr /ipk 8N67H-M3CY9-QT7C4-2TR7M-TXYCV")
                os.system("slmgr /skms kms.xspace.in")
                os.system("slmgr /ato")
                print("\n============================================================================================================")
                print("Activating Windows 10 Pro (Pro) (2)")
                print("============================================================================================================")
                print("slmgr /ipk 8N67H-M3CY9-QT7C4-2TR7M-TXYCV")
                print("slmgr /skms kms.xspace.in")
                print("slmgr /ato")
                print("============================================================================================================\n")
            if ui == "0":
                try:
                    uis = input("Ключ: ")
                except:
                    pass
                os.system("slmgr /ipk {}".format(uis))
                os.system("slmgr /skms kms.xspace.in")
                os.system("slmgr /ato")
                print("\n============================================================================================================")
                print("{}".format(uis))
                print("============================================================================================================")
                print("slmgr /ipk {}".format(uis))
                print("slmgr /skms kms.xspace.in")
                print("slmgr /ato")
                print("============================================================================================================\n")
        if str(self.inp[0]).lower() == "mailing_authorization":
            if os.path.isfile("email.ini") == False:
                print("[*] Authorization.")
                self.email_user = input("Email: ")
                self.email_password = getpass.getpass("Password: ")
                self.email_host = input("smtp: ")
                print(f"[*] Authorization — {self.email_user}.")
                email_file = open("email.ini", "w+")
                email_file.write("""[user]
email = {}
password = {}
host = {}""".format(self.email_user, self.email_password, self.email_host))
                email_file.close()
            else:
                config = configparser.ConfigParser()
                config.read("email.ini")
                self.email_user = config["user"]["email"]
                self.email_password = config["user"]["password"]
                self.email_host = config["user"]["host"]
                print(f"[*] Authorization — {self.email_user}.")
        if str(self.inp[0]).lower() == "mailing" and str(self.inp[1]).lower().replace(" ", "") != "" and str(self.inp[2]).lower().replace(" ", "") != "" and str(self.inp[3]).lower().replace(" ", "") != "" and str(self.inp[4]).lower().replace(" ", "") != "" and str(self.inp[5]).lower().replace(" ", "") != "" and str(self.inp[6]).lower().replace(" ", "") != "":
            HOST = "smtp."+str(self.inp[6])
            if str(self.inp[4]).lower() == "--file":
                try:
                    with open("1.txt", encoding="utf-8") as text:
                        text = text.read()
                except:
                    pass
            elif str(self.inp[4]).lower() == "--text":
                text = str(self.inp[5])
            msg = MIMEMultipart()
            msg["From"] = str(self.inp[1])
            msg["To"] = str(self.inp[2])
            msg["Subject"] = str(self.inp[3])
            message = text
            msg.attach(MIMEText(message))
            mailserver = smtplib.SMTP(HOST,587)
            mailserver.ehlo()
            mailserver.starttls()
            mailserver.ehlo()
            mailserver.login(self.email_user, self.email_password)
            mailserver.sendmail(self.email_user,str(self.inp[2]),msg.as_string())
            mailserver.quit()
        if str(self.inp[0]).lower() == "port_scanner":
            N_THREADS = 200
            self.q = Queue()
            print_lock = Lock()
            def port_scan(port):
                try:
                    s = socket.socket()
                    s.connect((host, port))
                except:
                    with print_lock:
                        print(f"{host:15}:{port:5} is closed", end="\r")
                else:
                    with print_lock:
                        print(f"{host:15}:{port:5} is open")
                finally:
                    s.close()
            def scan_thread():
                while True:
                    worker = self.q.get()
                    port_scan(worker)
                    self.q.task_done()
            def main(host, ports):
                print("Port scan in progress...")
                for t in range(N_THREADS):
                    t = Thread(target=scan_thread)
                    t.daemon = True
                    t.start()
                for worker in ports:
                    self.q.put(worker)
                self.q.join()
            host, port_range = str(self.inp[1]), str(self.inp[2])
            start_port, end_port = port_range.split("-")
            start_port, end_port = int(start_port), int(end_port)
            ports = [p for p in range(start_port, end_port)]
            main(host, ports)
        if str(self.inp[0]).lower() == "$cmd":
            os.system(self.out.replace("$cmd", ""))
        if str(self.inp[0]).lower() == "help":
            print(__help__)
class Main:
    def __init__(self):
        try:
            try:
                if sys.argv[1] == "--version" or "-v":
                    print("Command Line Interpreter [version 3.2].")
            except:
                Root()
                print("[*] Work with Metros Command Line Interpreter 3.2 completed.")
        except Exception as e:
            print(traceback.format_exc())
            print(Fore.RED+"[*] Having problems, what are the problems? you can contact the technical support metrostechnicalsupp0rt@gmail.com or look for information on the website metros-software.ru."+Fore.WHITE)
if __name__ == "__main__":
    Main()
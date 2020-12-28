import hashlib
from base64 import *
import compileall
from os import system, path
from time import sleep


def logo():
    system("echo -e \"\e[92m               .           .          \"")
    system("echo -e \"\e[92m              M.          .M          \"")
    system("echo -e \"\e[92m               MMMMMMMMMMM.           \"")
    system("echo -e \"\e[92m           .MMM\MMMMMMM/MMM.          \"")
    system("echo -e \"\e[92m           .MMM.7MMMMMMM.7MMM.        \"")
    system("echo -e \"\e[92m          .MMMMMMMMMMMMMMMMMMM        \"")
    system("echo -e \"\e[92m          MMMMMMM.......MMMMMMM       \"")
    system("echo -e \"\e[92m          MMMMMMMMMMMMMMMMMMMMM       \"")
    system("echo -e \"\e[92m     MMMM MMMMMMMMMMMMMMMMMMMMM MMMM  \"")
    system("echo -e \"\e[92m    dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD \"")
    system("echo -e \"\e[92m    dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD \"")
    system("echo -e \"\e[92m    dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD \"")
    system("echo -e \"\e[92m    dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD \"")
    system("echo -e \"\e[92m    dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD \"")
    system("echo -e \"\e[92m    dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD \"")
    system("echo -e \"\e[92m    dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD \"")
    system("echo -e \"\e[92m     MMM8 MMMMMMMMMMMMMMMMMMMMM 8MMM  \"")
    system("echo -e \"\e[92m          MMMMMMMMMMMMMMMMMMMMM       \"")
    system("echo -e \"\e[92m          MMMMMMMMMMMMMMMMMMMMM       \"")
    system("echo -e \"\e[92m              MMMMM   MMMMM           \"")
    system("echo -e \"\e[92m              MMMMM   MMMMM           \"")
    system("echo -e \"\e[92m              MMMMM   MMMMM           \"")
    system("echo -e \"\e[92m              MMMMM   MMMMM           \"")
    system("echo -e \"\e[92m              .MMM.   .MMM.           \"")
    system("echo -e \"\e[92m          $ by.Oliver -- XHTeam         \"")


def mth1(type, path):
    logo()
    sleep(1)
    """
 'md5',
 'sha1',
 'sha224',
 'sha256',
 'sha384',
 'sha3_224',
 'sha3_256',
 'sha3_384',
 'sha3_512',
 'sha512',
	"""
    typee = ""

    if type == 1:
        typee = "md5"
    elif type == 2:
        typee = "sha1"
    elif type == 3:
        typee = "sha224"
    elif type == 4:
        typee = "sha256"
    elif type == 5:
        typee = "sha384"
    elif type == 6:
        typee = "sha3_224"
    elif type == 7:
        typee = "sha3_256"
    elif type == 8:
        typee = "sha3_384"
    elif type == 9:
        typee = "sha3_512"
    elif type == 10:
        typee = "sha512"
    else:
        print("\n{!} Type number wrong !")

    with open(path, "rb")as p:
        f = p.read()
    hashh = hashlib.new(typee)
    hashh.update(f)
    output = hashh.hexdigest()

    with open(path, "w") as pp:
        pp.write(output)


# mth1("sha3_384", "newfile.py")


def mth2(path, type):
    logo()
    sleep(1)

    """
	b85encode ,
	b64encode,
	b32encode,
	b16encode,
	a85encode,
	"""
    if type == 1:
        with open(path, 'rb') as m:
            file = m.read()

        hash = b85encode(file)

        with open(path, 'wb') as n:
            data = n.write(hash)

        with open(path, 'r')as r:
            encoded = r.read()

        with open(path, 'w') as w:
            w.write('import base64\n')
            w.write('x=("')
            w.write(encoded)
            w.write('")')
            w.write('\nexec(base64.b85decode(x))')

    #####################

    elif type == 2:
        with open(path, 'rb') as m:
            file = m.read()

        hash = b64encode(file)

        with open(path, 'wb') as n:
            data = n.write(hash)

        with open(path, 'r')as r:
            encoded = r.read()

        with open(path, 'w') as w:
            w.write('import base64\n')
            w.write('x=("')
            w.write(encoded)
            w.write('")')
            w.write('\nexec(base64.b64decode(x))')
    ######################
    elif type == 6:
        if path.exists(filess):
            with open(filess, 'rb') as file:
                f = file.read()
                f = f.replace(b'import base64', b'')
                f = f.replace(b'x=("', b'')
                f = f.replace(b'")', b'')
                f = f.replace(b'exec(base64.b64decode(x))', b'')

            decoded = b64decode(f)

            with open(filess, 'wb') as b:
                b.write(decoded)
    ######################

    elif type == 3:
        with open(path, 'rb') as m:
            file = m.read()

        hash = b32encode(file)

        with open(path, 'wb') as n:
            data = n.write(hash)

        with open(path, 'r')as r:
            encoded = r.read()

        with open(path, 'w') as w:
            w.write('import base64\n')
            w.write('x=("')
            w.write(encoded)
            w.write('")')
            w.write('\nexec(base64.b32decode(x))')
    ###############$$###$

    elif type == 4:
        with open(path, 'rb') as m:
            file = m.read()

        hash = b16encode(file)

        with open(path, 'wb') as n:
            data = n.write(hash)

        with open(path, 'r')as r:
            encoded = r.read()

        with open(path, 'w') as w:
            w.write('import base64\n')
            w.write('x=("')
            w.write(encoded)
            w.write('")')
            w.write('\nexec(base64.b16decode(x))')
    ########################

    elif type == 5:
        with open(path, 'rb') as m:
            file = m.read()

            hash = a85encode(file)

            with open(path, 'wb') as n:
                data = n.write(hash)

            with open(path, 'r')as r:
                encoded = r.read()

            with open(path, 'w') as w:
                w.write('import base64\n')
                w.write('x=("')
                w.write(encoded)
                w.write('")')
                w.write('\nexec(base64.a16decode(x))')

    else:
        print("\n{!} Type number wrong!!")


######################


def mth3(dir):
    logo()
    sleep(1)

    system("echo -e \"\e[35m\"")
    compileall.compile_dir(dir)
    system("echo -e \"\e[0m\"")


# mth3("/sdcard/null")

# +++++++++++++++++++++++++++++
def mth4(type, path):
    logo()
    sleep(1)

    system("echo -e \"\e[35m\"")

    if type == 1:
        with open(path, 'rb') as m:
            file = m.read()

        hash = b85encode(file)

        with open(path, 'wb') as n:
            data = n.write(hash)

        with open(path, 'r')as r:
            encoded = r.read()

        with open(path, 'w') as w:
            w.write(encoded)

    if type == 2:
        with open(path, 'rb') as m:
            file = m.read()

        hash = b64encode(file)

        with open(path, 'wb') as n:
            data = n.write(hash)

        with open(path, 'r')as r:
            encoded = r.read()

        with open(files, 'w') as w:
            w.write(encoded)

    if type == 3:
        with open(files, 'rb') as m:
            file = m.read()

        hash = b32encode(file)

        with open(files, 'wb') as n:
            data = n.write(hash)

        with open(files, 'r')as r:
            encoded = r.read()

        with open(files, 'w') as w:
            w.write(encoded)

    if type == 4:
        with open(files, 'rb') as m:
            file = m.read()

        hash = b16encode(file)

        with open(files, 'wb') as n:
            data = n.write(hash)

        with open(files, 'r')as r:
            encoded = r.read()

        with open(files, 'w') as w:
            w.write(encoded)

    if type == 5:
        with open(files, 'rb') as m:
            file = m.read()

        hash = a85encode(file)

        with open(files, 'wb') as n:
            data = n.write(hash)

        with open(files, 'r')as r:
            encoded = r.read()

        with open(files, 'w') as w:
            w.write(encoded)
    system("echo -e \"\e[0m\"")


# *******************************
# apt install : 1- cmatrix       \
#               2- figlet         |
#               3- toilet        /
# *******************************

system("clear")
system("echo \"\e[31m\n\t|| 3ELC0ME T0 ||\e[0m\n\"")
system("toilet -f mono12 -F gay XHT")
print(chr(98), chr(121), chr(46), sep='', end='')

print(chr(79), chr(108), chr(105), chr(118), chr(101), chr(114), sep='')
system("echo \"\e[38;5;82m\"")
system("echo \"\e[0m\"")
load = "..."
loa = "loading"
print("loading", end='')
for k in range(3):
    for l in load:
        print(l, end='')
        sleep(.1)

    print("\b\b\b", end='')
print("\b"*len(loa))

system("clear")

system(
    "echo \"\n\e[38;5;198mWhat do you to hash \e[0m?\n\n\t\e[7m[1]\e[0m Python Script \e[34m(.py)\e[0m\n\t\e[7m[2]\e[0m Shell Script \e[34m(.sh)\n\n\t\e[1m\"")

inp = int(input("[XHT]==> "))
system("echo \"\e[0m\"")
sleep(.3)

if inp == 1:
    system("clear")
    system("echo \"\t\t\n\n\e[30;48;5;82m\"")
    print("Enter for Skip...!")
    system("echo \"\e[0m\"")

    sleep(1)
    system("clear")
    system("cmatrix -C green -s")
    system("echo \"\e[0m\"")
    system(f"echo \"\e[34;107m{chr(9762)} Select Hash Method {chr(9762)}\"")
    system("echo \"\n\n\t\e[104;30m[1]\e[0m\e[93m One Way Hash. \e[36m{Machine language}\"")
    system("echo \"\n\t\e[104;30m[2]\e[0m\e[93m Normal Encode. \e[36m{Base64 Library}\"")
    system("echo \"\n\t\e[104;30m[3]\e[0m\e[93m One Way Hash. \e[36m{Hashlib Library}\"")
    system("echo \"\e[34;1m\"")
    enc_py = int(input("[XHT]==> "))
    system("echo \"\e[0m\"")

    if enc_py == 1:
        system("echo \"\e[92m\"")
        path0 = input("\nEnter Scripts Path [: ")
        system("echo \"\e[0m\"")

        if system("cd " + path0 + " && ls *.py") == "":
            system("echo \"\e[101;5;97m\"")
            print("\nNo Python Scripts In This Path...!")
            system("echo \"\e[0m\"")
        else:
            system("echo \"\e[103;40m\"")
            print("\nPython Files Found...!")
            system("echo \"\e[0m\"")

            mth3(path0)

            system("echo \"\e[42m\"")
            print(f"\n{chr(9608)} Scripts encoded sucess {chr(9608)}")
            system("echo \"\e[0m\"")

    elif enc_py == 2:
        system("echo \"\e[92m\"")
        path0 = input("Enter Script Path [: ")
        sleep(.2)

        if path.exists(path0):

            system("clear")
            system(
                f"echo \"\n\e[0m\e[101;5m {chr(11621)} \e[0m\e[30;107;1m Select Encode Type \e[0m\e[101;5m {chr(11621)} \e[0m\n\n\"")
            system(
                f"echo \"\t\e[104;30m[1]\e[0m\e[42mB85encode\e[0m\t \e[5m{chr(10702)}\t\e[0m\e[104;30m[2]\e[0m\e[42mB64encode\n\"")
            system(
                f"echo \"\t\e[104;30m[3]\e[0m\e[42mB32decode\e[0m\t \e[5m{chr(10702)}\t\e[0m\e[104;30m[4]\e[0m\e[42mB16encode\n\"")
            system(
                f"echo \"\t\e[104;30m[5]\e[0m\e[42mA85encode\e[0m\t \e[5m{chr(10702)}\t\e[0m\e[104;30m[6]\e[0m\e[42mB64encode\e[0m\n\"")
            system("echo \"\e[33m\"")
            mth = int(input("Enter Hash Type Number [: "))
            system("echo \"\e[0m\"")
            mth2(path0, mth)
        else:
            system("echo \"\e[41;5m[!] File not exists [!]\e[0m\"")

    elif enc_py == 3:
        system("echo \"\e[33;1m\"")
        path0 = input("Enter Script Path [: ")
        system("echo \"\e[0m\"")

        if path.exists(path0):
            system("clear")
            system(
                f"echo \"\n\e[0m\e[101;5m {chr(11621)} \e[0m\e[30;107;1m Select Hash Type \e[0m\e[101;5m {chr(11621)} \e[0m\n\n\"")
            system(
                f"echo \"\t\e[104;30m[1]\e[0m\e[42mmd5\e[0m \t\t\e[5m{chr(10702)}\t\e[0m\e[104;30m[2]\e[0m\e[42msha1\n\"")
            system(
                f"echo \"\t\e[104;30m[3]\e[0m\e[42msha224\e[0m \t\e[5m{chr(10702)}\t\e[0m\e[104;30m[4]\e[0m\e[42msha256\n\"")
            system(
                f"echo \"\t\e[104;30m[5]\e[0m\e[42msha384\e[0m \t\e[5m{chr(10702)}\t\e[0m\e[104;30m[6]\e[0m\e[42msha3_224\n\"")
            system(
                f"echo \"\t\e[104;30m[7]\e[0m\e[42msha3_256\e[0m \t\e[5m{chr(10702)}\t\e[0m\e[104;30m[8]\e[0m\e[42msha3_384\n\"")
            system(
                f"echo \"\t\e[104;30m[9]\e[0m\e[42msha3_512\e[0m \t\e[5m{chr(10702)}\t\e[0m\e[104;30m[10]\e[0m\e[42msha512\e[0m\n\"")

            system("echo \"\e[33;1m\"")

            mth = int(input("\nEnter hash type number [: "))
            system("echo \"\e[0m\"")

            mth1(mth, path0)
            sleep(1)
            system(f"echo \"\n\e[45m{chr(10731)}..Done..{chr(10731)}\e[0m\"")

        else:
            system("echo \"\e[41;5m[!] Script path not exists [!]\e[0m\"")


elif inp == 2:
    system("clear")
    system("echo \"\t\t\n\n\e[30;48;5;82m\"")
    print("Enter for Skip...!")
    system("echo \"\e[0m\"")

    sleep(1)
    system("clear")
    system("cmatrix -C red -s")
    system("echo \"\e[0m\"")

    system("clear")

    system(
        f"echo \"\n\e[30;107;5m {chr(9762)} \e[0m\e[101;97m Select Hash Or Encode Lib \e[0m\e[30;107;5m {chr(9762)} \e[0m\"")
    system("echo \"\n\n\t\e[0m\e[105;30m[1]\e[0m\e[107;30m  Hashlib library.\"")
    system("echo \"\n\t\e[0m\e[105;30m[2]\e[0m\e[107;30m  Base64 library.\"")
    system("echo \"\n\e[101;97;1m\"")
    lib = int(input("[XHT]==> "))
    system("echo \"\e[0m\"")

    if lib == 1:
        system("clear")
        """        system(f"echo \"\t\t\e[93mloading...\n\t\e[0m {chr(12304)}\e[43m\"")
                sleep(.2)
                loading = str(chr(9608))
                for load in range(10):
                    print(loading, end='')
                    sleep(.4)
                system(f"echo \"\"\e[0m{chr(12305)}\n")
        """
        sleep(.2)
        system("clear")
        system("echo \"\e[0m\"")

        system(
            f"echo \"\n\e[0m\e[107;30;5m {chr(11621)} \e[0m\e[101;97m Select Hash Method \e[0m\e[30;107;5m {chr(11621)} \e[0m\n\n\"")
        system(
            f"echo \"\t\e[104;30m[1]\e[0m\e[42mMd5\e[0m \t\t\e[107;30;5m {chr(10702)} \t\e[0m\e[104;30m[2]\e[0m\e[42mSha1\n\"")
        system(
            f"echo \"\t\e[104;30m[3]\e[0m\e[42mSha224\e[0m \t\e[107;30;5m {chr(10702)} \t\e[0m\e[104;30m[4]\e[0m\e[42mSha256\n\"")
        system(
            f"echo \"\t\e[104;30m[5]\e[0m\e[42mSha384\e[0m\t\e[107;30;5m {chr(10702)} \t\e[0m\e[104;30m[6]\e[0m\e[42mSha3_224\n\"")
        system(
            f"echo \"\t\e[104;30m[7]\e[0m\e[42mSha3_256\e[0m \t\e[107;30;5m {chr(10702)} \t\e[0m\e[104;30m[8]\e[0m\e[42mSha3_384\n\"")
        system(
            f"echo \"\t\e[104;30m[9]\e[0m\e[42mSha3_512\e[0m \t\e[107;30;5m {chr(10702)} \t\e[0m\e[104;30m[10]\e[0m\e[42mSha512\e[0m\n\"")

        system("echo \"\e[33;1m\"")

        typ = int(input("\nEnter Type Number [: "))
        path0 = input("\nEnter §cript path [: ")
        system("echo \"\e[0m\"")

        if path.exists(path0):
            mth1(typ, path0)
            sleep(1)
            system(f"echo \"\n\e[45m{chr(10731)}..Done..{chr(10731)}\e[0m\"")
        else:
            sleep(.5)
            system("echo \"\e[41;5m[!] Script not found [!]\e[0m\"")

    elif lib == 2:
        system("clear")
        sleep(.5)

        # system(f"echo \"\n\e[0m\e[107;30;5m {chr(11621)} \e[0m\e[101;97m Select Hash Method \e[0m\e[30;107;5m {chr(11621)} \e[0m\n\n\"")
        # system(
        #   f"echo \"\t\e[104;30m[1]\e[0m\e[42mMd5\e[0m \t\t\e[107;30;5m {chr(10702)} \t\e[0m\e[104;30m[2]\e[0m\e[42mSha1\n\"")

        system(
            f"echo \"\n\e[0m\e[107;30;5m {chr(11621)} \e[0m\e[101;97m Select Encode Method \e[0m\e[30;107;5m {chr(11621)} \e[0m\n\n\"")
        system(
            f"echo \"\t\e[104;30m[1]\e[0m\e[42mB85encode\e[0m \t\e[107;30;5m {chr(10702)} \t\e[0m\e[104;30m[2]\e[0m\e[42mB64encode\n\"")
        system(
            f"echo \"\t\e[104;30m[3]\e[0m\e[42mB32encode\e[0m \t\e[107;30;5m {chr(10702)} \t\e[0m\e[104;30m[4]\e[0m\e[42mB16encode\n\"")
        system(
            f"echo \"\t\t\e[104;30m[5]\e[0m\e[42mA85encode\e[0m\e[0m\n\"")
        system("echo \"\e[33;1m\"")

        typ = int(input("Enter Type Number [: "))
        path0 = input("\nEnter §cript path <: ")
        system("echo \"\e[0m\"")

        typee = ""

        if typ == 1:
            typee = b85encode
        elif typ == 2:
            typee = b64encode
        elif typ == 3:
            typee = b32encode
        elif typ == 4:
            typee = b16encode
        elif typ == 5:
            typee = a85encode
        else:
            system("echo \"\e[41;5m[!] Type Number Wrong [!]\e[0m\"")

        if path.exists(path0):
            with open(path0, 'rb') as m:
                file = m.read()

            hash = typee(file)

            with open(path0, 'wb') as n:
                data = n.write(hash)

            with open(path0, 'r')as r:
                encoded = r.read()

            with open(path0, 'w') as w:
                w.write(encoded)
            sleep(1.5)
            system(f"echo \"\n\e[45m{chr(10731)}..Done..{chr(10731)}\e[0m\"")

        else:
            sleep(.5)
            system("echo \"\n\e[41;5m[!] Script Not Found [!]\e[0m\"")

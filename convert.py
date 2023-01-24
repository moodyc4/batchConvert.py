#!/usr/bin/env python
import os
import sys

#List of current commands:
h = ["-h", "\n--------------------\nUsage: \nconvert.py [Path to folder containing files] [Name for new files]\n\nNew Files will be saved in a folder named 'Converted'\n--------------------\n"]
c = ["-c [path]", "converts files in given dir. If none specified, current working dir will be used."]

def help():
    print(h[1])

def convert(prefix, path, outName):
    i = 1
    for filename in os.listdir(path):
        if (filename.endswith(".mp4")):
            if (outName == ""):
                x = filename.split('.')
                newName = prefix + x[0] + "_" + str(i) + ".mp4"
            else:
                newName = prefix + outName + "_" + str(i) + ".mp4"
            try:
                os.system("ffmpeg -i '{0}' '{1}'".format(filename, newName))
                i = i + 1
            except:
                print("ffmpeg bro chunked!")
        else:
            continue
    print("Done")

def getInput(args):
    i = 0
    prefix = ""
    path = ""
    outName = ""

    for arg in args:
        if (len(args) > 5):
            print("Too many arguments. '-h' for help.")
            break
        elif (len(args) < 3):
            a = input("No folder or output name specified, default location and names will be used. \nContinue? [Y/N] ")
            if (a.lower() == "y" or a.lower() == ""):
                convert()
            else:
                break
        elif (i == 2):
            print(arg)
        elif (i == 3):
            print(arg)
        elif (i == 4):
            print(arg)
        i = i + 1

    if (path == ""):
        path = os.getcwd()
    try:
        os.chdir(path)
    except:
        print("Bad Path?")
        path = ""

    outputDir = path + "/" + "Converted"
    try:
        os.mkdir(outputDir)
    except:
        print("Folder exists... Continuing...")
    prefix = outputDir + "/"
    convert(prefix, path, outName)

def main():
    if (len(sys.argv) == 1):
        getInput(sys.argv)
    elif (sys.argv[1] == "-h"):
        help()
    elif (sys.argv[1] == "-c"):
        getInput(sys.argv)
    else:
        huh = sys.argv[1]
        print("\nI'm not sure what you want me to do with '{0}'\n'-h' for help\n".format(huh))

main()
#!/usr/bin/python3
import os
import sys

#List of current commands:
c = ["'-c' [Directory] [Name] | Converts files in given directory. If not specified, current dir will be used.", "'-h' | Shows help"]
h = "\n--------------------\nBatch Converter Usage\nCommands:\n\n{0}\n\n{1}\n\nNew Files will be saved in a folder named 'Converted'\n--------------------\n".format(c[0], c[1])

def help():
    print(h)

def convert(*args):
    i = 1
    outName = ""
    if (len(args) == 1):
        path = args[0]
    elif (len(args) == 2):
        path = args[0]
        outName = args[1]
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
    for filename in os.listdir(path):
        if (filename.endswith(".mp4")):
            if (outName == ""):
                x = filename.split('.')
                newName = prefix + x[0] + "_" + str(i) + ".mp4"
            else:
                newName = prefix + outName + "_" + str(i) + ".mp4"
            try:
                os.system("ffmpeg -i '{0}' '{1}'".format(filename, newName))
            except:
                print("ffmpeg bro chunked!")
        else:
            continue
        i = i + 1
    print("Done")

def getInput(args):
    path = ""
    if (len(args) > 5):
        print("Too many arguments. '-h' for help.")
    elif (len(args) < 3):
        a = input("No folder or output name specified, default location and names will be used. \nContinue? [Y/N] ")
        if (a.lower() == "y" or a.lower() == ""):
            path = os.getcwd()
            convert(path)
    else:
        path = args[2]
        if (len(args) > 3):
            outName = args[3]
            convert(path, outName)
        else:
            convert(path)


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
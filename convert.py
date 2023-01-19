import os


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
                os.system("ffmpeg -i '{0}' {1}".format(filename, newName))
                i = i + 1
            except:
                print("ffmpeg bro chunked!")
        else:
            continue
    print("Done")


path = input("Path to convert: ")

if (path == ""):
    path = os.getcwd()
elif (path == "1"):
    path = "/Users/cmoody/Desktop/20230113"
try:
    os.chdir(path)
except:
    print("Bad Path?")
    path = ""

outputDir = path + "/" + "Converted"
outName = input("Name for output files: ")
#if not (os.path.isdir(outputDir)):
try:
    os.mkdir(outputDir)
except:
    print("Folder exists... Continuing...")
prefix = outputDir + "/"
convert(prefix, path, outName)
#print("Couldn't create output folder")
    

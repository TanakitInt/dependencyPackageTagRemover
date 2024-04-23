print("Dependency Package Tag Remover")
print("")

try:
    def main():

        #get input
        print("Please enter filename: ")
        fileName = str(input())

        #read file
        text = open(fileName, encoding="utf-8")
        text = text.readlines()

        #clear context
        open('output.txt', 'w').close()

        #write lines
        for line in text:
            line = line.split(":", 1)[0]
            #print(line)

            f = open("output.txt", "a")
            f.write(line + '\n')

    main()

except Exception as e:
    print("Error! " + str(e))
    main()


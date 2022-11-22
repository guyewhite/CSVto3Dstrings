# csvto3dstrings.py
# CSV to 3D-Array of Strings in C, v1
#
# G. Elvin White
# 20 November 2022
#
# Usage:    python csvto3dstrings.py INPUTFILE OUTPUTFILE STRUCTURENAME
# Example:  python csvto3dstrings.py scales.csv scales.h myScales
#

import csv
import sys

def main():
    # Verify file present
    if len(sys.argv) != 4:
        print("Usage: python csvto3dstrings.py INPUTFILE OUTPUTFILE STRUCTURENAME")
        exit()

    inputfile = sys.argv[1]
    outputfile = sys.argv[2]
    structureName = sys.argv[3]

    # open csv
    with open(inputfile, "r") as inFile:
        csvreader = csv.reader(inFile)

        # create the C header file
        with open(outputfile, "w") as outFile:

            # discover number of columns and skip first line
            columns = len(next(csvreader))

            #discover number of rows
            rows = sum(1 for row in csvreader)

            # find the largest item in the cells
            inFile.seek(0)
            next(csvreader)
            itemSize = 0
            for row in csvreader:
                for item in row:
                    if len(item) > itemSize:
                        itemSize = len(item)
            itemSize = itemSize + 1

            # Write first row of outfile
            line = "char " + structureName + "[" + str(rows) + "][" + str(columns) + "][" + str(itemSize) + "] = {\n"
            outFile.write(line)

            # return to top and iterate through each row
            inFile.seek(0)
            next(csvreader)
            currentRow = 0
            for row in csvreader:

                # write opening of row
                line = "\t{"
                outFile.write(line)

                # for each item in a row
                itemCount = 0
                for item in row:

                    #start quote
                    quote = "\""
                    outFile.write(quote)

                    #item
                    outFile.write(item)

                    #end quote
                    quote = "\""
                    outFile.write(quote)
                    if itemCount < columns-1:
                        line = ", "
                        outFile.write(line)
                    itemCount = itemCount + 1

                # write closing of row
                line = "}"
                outFile.write(line)

                # add comma if not last row
                if currentRow != rows:
                    line = ","
                    outFile.write(line)

                # new line
                line = "\n"
                outFile.write(line)

                currentRow = currentRow + 1

            # write the last line
            line = "};"
            outFile.write(line)

if __name__ == "__main__":
    main()

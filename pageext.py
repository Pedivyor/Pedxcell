import sys

# path to file
pdf = open("C:\\Documents and Settings\\ivan\\Desktop\\scan0001.pdf", "rb").read()


startmark = "\xff\xd8"
startfix = 0
endmark = "\xff\xd9"
endfix = 2
i = 0

istream = pdf.find("stream")
if istream < 0:
exit()
istart = pdf.find(startmark, istream, istream+20)
if istart < 0:
exit()
iend = pdf.find("endstream", istart)
if iend < 0:
raise Exception("Didn't find end of stream!")
iend = pdf.find(endmark, iend-20)
if iend < 0:
raise Exception("Didn't find end of JPG!")

istart += startfix
iend += endfix
# print "JPG {0} from {1} to {2}".format(njpg, istart, iend)
jpg = pdf[istart:iend]
jpgfile = open("C:\\Documents and Settings\\ivan\\Desktop\\pdfpic.jpg", "wb")
jpgfile.write(jpg)
jpgfile.close()

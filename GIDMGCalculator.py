from tkinter import *
from PIL import Image, ImageTk

main = Tk()



#variables
buildOne_TTATK = DoubleVar()
buildTwo_TTATK = DoubleVar()
buildOne_BonusDMG = DoubleVar()
buildTwo_BonusDMG = DoubleVar()

buildOne_TTATK.set(1)
buildTwo_TTATK.set(1)
buildOne_BonusDMG.set(1)
buildTwo_BonusDMG.set(1)


# 1st Wrapper - Start
outFrame1 = LabelFrame(main, bg="white",  borderwidth=0)
outFrame1.pack()

importedImage = Image.open('./paimon.png')
importedImage.thumbnail((80, 80), Image.ANTIALIAS)
png = ImageTk.PhotoImage(importedImage)
inFrame1 = Label(outFrame1, image=png, bg="white")
inFrame1.grid(row = 0, column = 0, padx = 10, pady = 10)

inFrame2 = LabelFrame(outFrame1, bg="white", borderwidth=0)
inFrame2.grid(row = 0, column = 1, padx = 20, pady = 20)
inFrame2_1 = Label(inFrame2, text="Genshin Impact DMG Calculator", bg="white", underline=0)
inFrame2_1.grid(row = 0, column = 0, padx = 10, pady = 10)

inFrame2_2 = Label(inFrame2, text=">The program is dumb, but that doesn't mean you have to be<", bg="white")
inFrame2_2.grid(row = 1, column = 0, padx = 10, pady = 10)

# 1st Wrapper - End

titleFrame = LabelFrame(main, bg="white", borderwidth=0)
titleFrame.pack(fill="both")
titleFrameCol0 = Label(titleFrame, bg="white", width="40")
titleFrameCol0.grid(row = 0, column = 0, padx = 10, pady = 10)

titleFrameCol1 = Label(titleFrame, bg="white", width="40", text="Build One")
titleFrameCol1.grid(row = 0, column = 1, padx = 10, pady = 10)

titleFrameCol2 = Label(titleFrame, bg="white", width="40", text="Build Two")
titleFrameCol2.grid(row = 0, column = 2, padx = 10, pady = 10)


# 2nd Wrapper - Start
outFrame2 = LabelFrame(main, bg="white")
outFrame2.pack(fill="both")

col0 = Label(outFrame2, bg="white", width="40", text="Talents and Percentages")
col0.grid(row = 0, column = 0, padx=10, pady = 10)

col1ATK = Label(outFrame2, bg="white", text="Total ATK: ", width="20")
col1ATK.grid(row = 0, column = 1)
col1ATKEntry = Entry(outFrame2, bg="white", width="20", textvariable=buildOne_TTATK)
col1ATKEntry.grid(row = 0, column = 2)
col1BonusDMG = Label(outFrame2, bg="white", text="Bonus DMG%: ", width="20")
col1BonusDMG.grid(row = 1, column = 1)
col1BonusDMGEntry = Entry(outFrame2, bg="white", width="20", textvariable=buildOne_BonusDMG)
col1BonusDMGEntry.grid(row = 1, column = 2)


col2ATK = Label(outFrame2, bg="white", text="Total ATK: ", width="20")
col2ATK.grid(row = 0, column = 3)
col2ATKEntry = Entry(outFrame2, bg="white", width="20", textvariable=buildTwo_TTATK)
col2ATKEntry.grid(row = 0, column = 4)
col2BonusDMG = Label(outFrame2, bg="white", text="Bonus DMG %: ", width="20")
col2BonusDMG.grid(row = 1, column = 3)
col2BonusDMGEntry = Entry(outFrame2, bg="white", width="20", textvariable=buildTwo_BonusDMG)
col2BonusDMGEntry.grid(row=1, column= 4)

# 2nd Wrapper - End

# 3rd Wrapper - Start
outFrame3 = LabelFrame(main, bg="white", borderwidth=0)
outFrame3.pack(fill="both")

dic1 = {}
dic2 = {}

dmgPercentage = {}

for i in range(10):
    dmgPercentage[i] = DoubleVar()
    dmgPercentage[i].set(1)
    dic1[i] = DoubleVar()
    dic1[i].set(1)
    dic2[i] = DoubleVar()
    dic2[i].set(1)

    inFrame1No = Label(outFrame3, bg="white", text="No. " + str(i+1) + ":", width="20")
    inFrame1No.grid(row = i, column = 0, padx = 10, pady = 10)
    inFrame1Ent = Entry(outFrame3, bg="white", textvariable=dmgPercentage[i], width="20")
    inFrame1Ent.grid(row = i, column = 1, padx = 10, pady = 10)
    inFrame1Result1_1 = Label(outFrame3, bg="white", text="Result: ", width="20")
    inFrame1Result1_1.grid(row = i, column = 2, padx = 10, pady = 10)
    inFrame1Result1_2 = Label(outFrame3, bg="white", textvariable=dic1[i], width="20")
    inFrame1Result1_2.grid(row = i, column = 3, padx = 10)
    inFrame1Result2_1 = Label(outFrame3, bg="white", text="Result: ", width="20")
    inFrame1Result2_1.grid(row = i, column = 4, padx = 10, pady = 10)
    inFrame1Result2_2 = Label(outFrame3, bg="white", textvariable=dic2[i], width="20")
    inFrame1Result2_2.grid(row = i, column = 5, padx = 10)

# 3rd Wrapper - End

#functions
def calculateDMG():
    for i in range(10):
        dic1[i].set((buildOne_TTATK.get()*(dmgPercentage[i].get()/100.0)) * ((buildOne_BonusDMG.get()/100.0)+1.0))
        dic2[i].set((buildTwo_TTATK.get()*(dmgPercentage[i].get()/100.0)) * ((buildTwo_BonusDMG.get()/100.0)+1.0))
         

buttonWrapper = Label(main, bg="white")
buttonWrapper.pack()
calculateButton = Button(buttonWrapper, text="Calculate", command=calculateDMG, bg="white")
calculateButton.pack(pady=10)

main.geometry("1080x720")
main.title("Calculate/Compare Your Genshin Damage")
main.configure(bg="white")
main.resizable(False, False)
main.mainloop()
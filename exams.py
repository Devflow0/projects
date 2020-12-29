Answers=[]
Question_List=[]

class Examinations:
    def letters():
        return ["a","b","c","d"]
    """
    def final(answer=[]):
        choice=input('is that your final answer? "y/n" ')
        if choice=="y":
            Answers.append(answer)
        elif choice=="n":
            #print("")
            Examinations.final(answer)
        else:
            print ('\nplease input "y" to continue or "n" to re-answer the question')
            Examinations.final(answer)
    """
    def answer():
        ans=(input("input your answer:  ")).lower()
        #print(type(ans))
        if ans in Examinations.letters():
            #Examinations.final(ans)
            Answers.append(ans)
        else: print('input a letter from "A" to "D"\n ');Examinations.answer()
    def Question():
        q1=("Question 1 :what is the meaning of a PCB:\n(A): power circuit board\n(B):power circuit management\n(C)protocol control board\n(D)point control board\n")
        Question_List.append("Question 1")
        print(q1)
        Examinations.answer()
        
        q2=("\nQuestion 2 :The word 'Computer' usually refers to the Central Processing Unit plus:\n(A)Input Devices\n(B)External Memory\n(C)Internal Memory\n(D)Output Device\n")
        Question_List.append("Question 2")
        print(q2)
        Examinations.answer()

        q3=("\nQuestion 3 :All of the following are examples of storage devices except:\n(A)hard disk drives\n(B)printers\n(C)floppy disk drives\n(D)CD drives\n")
        Question_List.append("Question 3")
        print(q3)
        Examinations.answer()

        q4=("\nQuestion 4 :Which one is the secondary memory device ?:\n(A)CPU\n(B)ALU\n(C)floppy disk\n(D)Mouse\n")
        Question_List.append("Question 4")
        print(q4)
        Examinations.answer()

        q5=("\nQuestion 5 :Human beings are referred to as Homo Sapiens. Which device is called Silico Sapiens?\n(A)Monitor\n(B)Hardware\n(C)Robot\n(D)Computer\n")
        Question_List.append("Question 5")
        print(q5)
        Examinations.answer()

        q6=("\nQuestion 6 :__________________ are devices used to transmit data over telecommunications lines.\n(A)Drives\n(B)Drive bays\n(C)Modems\n(D)Platforms\n")
        Question_List.append("Question 6")
        print(q6)
        Examinations.answer()

        q7=("\nQuestion 7 :A ________________ is an electronic device that processes data, converting it into information.\n(A)processor\n(B)computer\n(C)case\n(D)stylus\n")
        Question_List.append("Question 7")
        print(q7)
        Examinations.answer()

        q8=("\nQuestion 8 :Using output devices one can ____________\n(A)input data\n(B)store data\n(C)scan data\n(D)view or print data\n")
        Question_List.append("Question 8")
        print(q8)
        Examinations.answer()

        q9=("\nQuestion 9 :A light-sensitive device that converts drawing, printed text or other images into digital form is\n(A)keyboard\n(B)plotter\n(C)scanner\n(D)OMR\n")
        Question_List.append("Question 9")
        print(q9)
        Examinations.answer()

        q10=("\nQuestion 10 :Which of the following is not an input device?\n(A)Mouse\n(B)Keyboard\n(C)Light pen\n(D)VDU\n")
        Question_List.append("Question 10")
        print(q10)
        Examinations.answer()

        q11=("\nQuestion 11 :The place where data or program goes is known as?\n(A)mouse\n(B)keyboard\n(C)CPU\n(D)CU\n")
        Question_List.append("Question 11")
        print(q11)
        Examinations.answer()

        q12=("\nQuestion 12 : ___________ is a type of input machine.\n(A)Monitor\n(B)Printer\n(C)Plotter\n(D)Keyboard\n")
        Question_List.append("Question 12")
        print(q12)
        Examinations.answer()

        q13=("\nQuestion 13 :In a computer system, which device is functionally opposite of a keyboard?\n(A)Mouse\n(B)Trackball\n(C)Printer\n(D)Joystick\n")
        Question_List.append("Question 13")
        print(q13)
        Examinations.answer()

        q14=("\nQuestion 14 :What are the two types of output devices?\n(A)Monitor and printer\n(B)Storage disks (floppy, CD)\n(C)Keyboard and mouse\n(D)Windows 2000, Windows NT\n")
        Question_List.append("Question 14")
        print(q14)
        Examinations.answer()

        q15=("\nQuestion 15 :Which of the following categories would include a keyboard?\n(A)Printing Device\n(B)Output Device\n(C)Storage Device\n(D)Input Device\n")
        Question_List.append("Question 15")
        print(q15)
        Examinations.answer()


        q16=("\nQuestion 16 :A modem that cannot be moved from its position is called ______________.\n(A)Intelligent Modem\n(B)Acoustic Coupler\n(C)Direct connect\n(D)Fixed modem\n")
        Question_List.append("Question 16")
        print(q16)
        Examinations.answer()

        q17=("\nQuestion 17 :What is output ?\n(A)What the processor takes from the user\n(B)What the user gives to the processor\n(C)What the processor gets from the user\n(D)What the processor gives to the user\n")
        Question_List.append("Question 17")
        print(q17)
        Examinations.answer()

        q18=("\nQuestion 18 :Hard Disks and Diskettes are:\n(A)Direct Access Storage Devices\n(B)Sequential Access Storage Devices\n(C)Rarely used Microcomputers\n(D)Indirect Access Storage Devices\n")
        Question_List.append("Question 18")
        print(q18)
        Examinations.answer()

        q19=("\nQuestion 19 :Which of the following is not a hardware:\n(A)processor\n(B)Monitor\n(C)Keyboard\n(D)Microsoft Word\n")
        Question_List.append("Question 19")
        print(q19)
        Examinations.answer()

        q20=("\nQuestion 20 : Main electronic part of in first generation computer was _____________.\n(A)Transistor\n(B)Microprocessor\n(C)Vacuum Tubes\n(D)Large Scale Integrated Circuits\n")
        Question_List.append("Question 20")
        print(q20)
        Examinations.answer()
        #print(Question_List)

Examinations.Question()
Results=str(dict(zip(Question_List,Answers)))
file=open("Resuts.txt","w").write("This were your answers:\n"+Results)

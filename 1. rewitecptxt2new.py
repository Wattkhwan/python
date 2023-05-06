import enum
import os
from pathlib import Path

# หาบรรทัดเริ่มจะมีคำว่า Next หรือ Manga ส่วนบรรทัดสุดท้ายจะหาจากคำว่า บทที่ หรือ ตอนที่ ต่อจากบรรทัดเริ่ม
def start(rf):
    lookup1 = 'Next'
    lookup2 = 'บทที่ '
    lookup3 = "Manga"
    lookup4 = "ตอนที่ "
    line_num1 = 0
    line_num2 = 0
    with open(rf, "r", encoding="utf8") as fr:
        for num1, line in enumerate(fr):
            #line_num += 1
            if lookup1 in line or lookup3 in line:
                line_num1 = num1
                print(line_num1)
                break
            
    fr.close()
    num2 = num1

    with open(rf, "r", encoding="utf8") as fr:
        for num2, line in enumerate(fr):
            if ((lookup2 in line or lookup4 in line) and (num2 > num1+30)):
                line_num2 = num2
                print(line_num2)
                break
    fr.close()
    return line_num1, line_num2

# ทำการ ส่งค่ามา  4 ค่า read file, write file, first line, last line เพื่อทำการ copy จาก read file ไปที่ write file 
def copy(rf,wf,start,end):
    with open(rf, "r", encoding="utf8") as fr:
        with open(wf, "w", encoding="utf8") as fw:

        #content = fr.readlines()
        #print(content[line_num1+1:line_num2-1])
        #line_cp = [line_num1+1:line_num2-1]
            readfile = fr.readlines()
            for line in range(start+1, end):
                fw.write(readfile[line])
                print(readfile[line])
        fw.close()
    fr.close()

def rename():
    # Create a path object
    pathraw = Path("d:/txt/raw")
    #pathout = Path("d:/txt/out/")
    for file in pathraw.iterdir():
    #print(file)
        # Set up key variables for the parent path and the file extensions
        directory = file.parent
        extension = file.suffix

        # Use unpacking by splitting the old name on the '-' character
        old_name = file.stem
        names, step, noneed = old_name.split(' - ')

        # Format as DATE - REGION - REPORT TYPE
        new_name = f'{names} - {step}{extension}'

        # Rename the file
        file.rename(Path(directory, new_name))

def main():
    pathraw = "d:/txt/raw/"
    pathout = "d:/txt/out/"
    for rf in os.listdir(pathraw):
        if rf.endswith(".txt"):
            start_line, end_line = start(os.path.join(pathraw,rf))
            #end_line = end(os.path.join(pathraw,rf))
            wf = os.path.join(pathout,rf)
            copy(os.path.join(pathraw,rf),wf,start_line,end_line)

if __name__ == "__main__":
    #rename()
    main()


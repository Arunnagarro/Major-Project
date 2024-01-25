import datetime as dt

def open_file(User):
    fileopen=False
    try :
        file=open(User+"log"+f'{dt.date.today()} '+".txt","at")
        fileopen=True
    except Exception as e :
        print("can not open file ! \n"+ str(e))
    finally :
        if fileopen==True:
            print("File opened succeffuly !")
            return file
def write_file(File,Message):
     file=File
     message=Message
     file.write(message)
     print("file written successfully !")

def read_file(User):
    fileread=False
    try :
        file=open(User+"log"+f'{dt.date.today()} '+".txt","rt")
        fileread=True
    except Exception as e :
        print("can not open file ! \n"+ str(e))
    finally :
        if fileread==True:
            print("File read succeffuly !")
            return file

def close_file(File):
    file=File
    log_data="-------------------- File is closed here at "+f"{dt.datetime.now()}"+"---------------------- \n\n\\n\n"
    file.close()
    print("File closed successfully !")
try:
    #put code here that you expect to raise exceptions or fail
    file = open("a_file.txt")
except FileNotFoundError:
    #better to use specific exceptions to look for, otherwise a lone except block will run for any exception
    print("file not found")
#except:
    #put code here to run in the event of an exception
else:
    #put code here to run when there are NO exceptions
    content = file.read()
    print(content)
finally:
    #the HONEYBADGER of code blocks
    #code in here runs NO MATTER WHAT HAPPENS in the above blocks
    #(useful for things like clean up)
    file.close()

    #you can force any type of error you want to with the 'raise' keyword
    #raise TypeError
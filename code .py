print("welcome to technosolutions soft.")
a = "technosolutions"
b = "this code is written by "
c = "for code of this type e-mail or comment us on youtube or instagram","https://www.youtube.com/@technosolutions2008"
x = (input("enter your name ! :"))
print("dear",x,b,a,c)


# this above code is not important you can cut ths ^^^^^^

import webbrowser
# this is module that connect  this code to broweser

def open_in_browser(url): # this is function to open input in browser
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
command = input("Enter your command====>   ")
open_in_browser(command)


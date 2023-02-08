def main():
    import requests, datetime, time
    from bs4 import BeautifulSoup
    from colorama import Fore as color
    import tkinter as tk
    from tkinter import filedialog

    #set up tkinter
    root = tk.Tk()
    root.withdraw()

    def getdata(url):
        # Make a GET request to the URL
        r = requests.get(url)
        # Return the text of the response
        return r.text

    print(f"""
    {color.YELLOW} ______        {color.BLUE}______                               
    {color.YELLOW}(_____ \      {color.BLUE}/ _____)                              
    {color.YELLOW} _____) )   _ {color.BLUE}( (____   ____  ____ _____ ____  _____ 
    {color.YELLOW}|  ____/ | | |{color.BLUE}|\____ \ / ___)/ ___|____ |  _ \| ___ |
    {color.YELLOW}| |    | |_| |{color.BLUE}|_____) | (___| |   / ___ | |_| | ____|
    {color.YELLOW}|_|     \__  |{color.BLUE}(______/ \____)_|   \_____|  __/|_____)
    {color.YELLOW}       (____/                           {color.BLUE}|_|
    {color.RESET}
    """)

    #prompt the user to input a valid url to parse until a valid url is given
    while True:
        siteInput = input("Enter Site: https://")
        site = f"https://{siteInput}"
        try:
            # Get the HTML data from the URL
            html_data = getdata(site)
            # Create a BeautifulSoup object from the HTML data
            soup = BeautifulSoup(html_data, 'html.parser')
            break
        except requests.exceptions.RequestException as e:
            print(f"\n{color.RED}Invalid URL, please try again.")
            print(f"Error {e}{color.RESET}\n")

    htmlTag = input("(Optional) Enter html tag: ")
    idInput = input("(Optional) Enter id: ")
    classInput = input("(Optional) Enter class: ")
    #textInput = input("(Optional) Enter text: ") *Make later*

    try:
        print("\nWhere would you like to store your output?\n")
        file_path = filedialog.askdirectory()
        # Initialize an empty list to store the elements
        item_list = []

        if htmlTag == "" and idInput == "" and classInput == "":
            items = soup.find('html')
            item_list.append(items)
        else:
            items = soup.find_all(htmlTag, id=idInput, class_=classInput)

            for item in items:
                item_list.append(item)

        nowTime = datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
        # Open a file with a name based on the current time and date

        with open(f"{file_path}/output-{nowTime}.txt", "w", encoding='utf-8') as file:
            # Write the list of elements to the file as a string
            file.write(str(item_list))
    except PermissionError:
        print("You closed the folder selection window. Please try again")

    print(f"{color.GREEN}Done, your output has been saved to \"{file_path}\"{color.RESET}")
    print("The program will close now.")
    time.sleep(2)
    quit()

if __name__ == "__main__":
    main()
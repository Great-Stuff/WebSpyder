def main():
    import datetime, requests, webbrowser, tkinter
    from bs4 import BeautifulSoup
    from tkinter import filedialog, messagebox

    def internet_on():
        try:
            requests.head('https://example.com', timeout=1)
            return True
        except requests.ConnectionError: 
            messagebox.showerror("Connection Error", "PyScrape requires internet to function. Please connect to the internet to use PyScrape")

            return False

    def getdata(url):
        # Make a GET request to the URL
        website = requests.get(url)
        # Return the text of the response
        return website.text
    def openPage(url):
        webbrowser.open_new_tab(url)
    def versionWindow():
        vWindow = tkinter.Toplevel(window)
        vWindow.title("About PyScrape")
        vWindow.geometry("300x200")
        vWindow.resizable(False, False)

        vFrame = tkinter.Frame(vWindow)
        vFrame.pack(fill="both", expand=True)

        infoFrame = tkinter.Frame(vFrame)
        infoFrame.pack(fill="both", expand= True, padx=5, pady=5)

        name = tkinter.Label(infoFrame, text="PyScrape")
        name.grid(row=0, column=0, sticky="w")

        version = tkinter.Label(infoFrame, text="v2.0 | Feb 15, 2023")
        version.grid(row=1, column=0, sticky="w")

        tkVersion = tkinter.Label(infoFrame, text="Tkinter 8.6")
        tkVersion.grid(row=2, column=0, sticky="w")

        pyVersion = tkinter.Label(infoFrame, text="Python 3.11.0")
        pyVersion.grid(row=3, column=0, sticky="w")

        madeBy = tkinter.Label(infoFrame, text="Made by @Great-Stuff on GitHub", cursor="hand2", font=("Helvetica 9 underline"))
        madeBy.bind("<Button-1>", lambda e: openPage("https://github.com/Great-Stuff"))
        madeBy.grid(row=4, column=0, sticky="w")

        bug = tkinter.Label(infoFrame, text="Found a bug?", cursor="hand2", font=("Helvetica 9 underline"))
        bug.bind("<Button-1>", lambda e: openPage("https://github.com/Great-Stuff/PyScrape/issues"))
        bug.grid(row=5, column=0, sticky="w")

    def saveDirectory():
            global filePath
            filePath = filedialog.askdirectory()
            if filePath == "":
                saveDirectory()
            else:
                filePathOut = tkinter.Label(saveFrame, text=f"Your file has been saved to {filePath}", cursor="hand2", wraplength=380)
                filePathOut.grid(row=1, column=0)
                filePathOut.bind("<Button-1>", lambda e: openPage(fr"file://{filePath}"))
    def correctUrl():
        global siteName
        siteName = siteInput.get(1.0, "end-1c")
        if siteName.startswith("https://www.") or siteName.startswith("http://www."):
            return
        elif siteName.startswith("www."):
            siteName = f"http://{siteName}"
        else:
            siteName = f"http://www.{siteName}"
    def parse():
        global filePath
        correctUrl()
        htmlName = htmlInput.get(1.0, "end-1c")
        idName = idInput.get(1.0, "end-1c")
        className = classInput.get(1.0, "end-1c")
        stringName = stringInput.get(1.0, "end-1c")

        try:
            htmlData = getdata(siteName)
            soup = BeautifulSoup(htmlData, 'html.parser')

            item_list = []

            if htmlName == "" and idName == "" and className == "" and siteName == "" and stringName == "":
                items = soup.find('html')
                item_list.append(items)
            else:
                items = soup.find_all(htmlName, id=idName, class_=className, string=stringName)
                for item in items:
                    item_list.append(item)
                for tag in soup.find_all():
                    if tag.name != "html" and tag.name != "body" and tag.name != "head" and tag.name != "title" and tag.name != "div" and tag.name != "style" and stringName in tag.text:
                        item_list.append(tag)

            filePath = filedialog.askdirectory()
            filePathOut = tkinter.Label(saveFrame, text=f"Your file has been saved to {filePath}", cursor="hand2", wraplength=(window.winfo_width()-10))
            filePathOut.grid(row=1, column=0)
            filePathOut.bind("<Button-1>", lambda e: openPage(fr"file://{filePath}"))

            nowTime = datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S")

            with open(f"{filePath}/output-{nowTime}.txt", "w", encoding='utf-8') as file:
                # Write the list of elements to the file as a string
                file.write(str(item_list)[2:-2])

        except requests.exceptions.RequestException as r:
            siteInput.delete(1.0, "end")
            siteInput.insert(1.0, "Invalid URL")
            print(r)

    internet_on()

    window = tkinter.Tk()
    window.title("PyScrape")
    window.resizable(False,False)

    frame = tkinter.Frame(window, borderwidth=0, relief="flat")
    frame.grid(row=0, column=0)

    titleFrame = tkinter.LabelFrame(frame)
    titleFrame.grid(row=0, column=0)

    menu_bar = tkinter.Menu(window)
    window.config(menu=menu_bar)

    menuMain = tkinter.Menu(menu_bar)
    menu_bar.add_cascade(label="Help", menu=menuMain)
    menuMain.add_command(label="PyScrape GitHub", command=lambda: openPage("https://github.com/Great-Stuff/PyScrape"))
    menuMain.add_command(label="About PyScape", command= lambda: versionWindow())

    siteFrame = tkinter.LabelFrame(frame)
    siteFrame.grid(row=1, column=0)

    siteLabel = tkinter.Label(siteFrame, text="Enter Site")
    siteInput = tkinter.Text(siteFrame, height=1, width=58)
    siteLabel.grid(row=0, pady=2, sticky="w")
    siteInput.grid(row=1, sticky="news")

    paramFrame = tkinter.LabelFrame(frame)
    paramFrame.grid(row=2, column=0, padx=5)

    def params():
        global htmlInput
        global idInput
        global classInput
        htmlLabel = tkinter.Label(paramFrame, text="Enter HTML tag")
        htmlInput = tkinter.Text(paramFrame, height=1, width=19)
        htmlLabel.grid(row=0, column=0)
        htmlInput.grid(row=1, column=0)

        idLabel = tkinter.Label(paramFrame, text="Enter ID")
        idInput = tkinter.Text(paramFrame, height=1, width=19)
        idLabel.grid(row=0, column=1)
        idInput.grid(row=1, column=1)

        classLabel = tkinter.Label(paramFrame, text="Enter Class")
        classInput = tkinter.Text(paramFrame, height=1, width=19)
        classLabel.grid(row=0, column=2)
        classInput.grid(row=1, column=2)
    params()

    stringFrame = tkinter.LabelFrame(frame)
    stringFrame.grid(row=3, column=0)

    stringLabel = tkinter.Label(stringFrame, text="Enter Text")
    stringInput = tkinter.Text(stringFrame, height=2, width=58)
    stringLabel.grid(row=2, column=0, sticky="w")
    stringInput.grid(row=3, column=0)

    saveFrame = tkinter.LabelFrame(window)
    saveFrame.grid(row=3, column=0)

    fileText = "Submit".center(146, " ")
    fileInput = tkinter.Button(saveFrame, text=fileText, command=parse)
    fileInput.grid(row=0, column=0, sticky="news")


    window.mainloop()

if __name__ == "__main__":
    main()
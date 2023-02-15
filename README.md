# PyScrape

<strong>What is PyScrape:</strong>

PyScrape is a simple webscraper made in Python using the BeautifulSoup4 library


<strong>Instructions for use:</strong>

When you open PyScrape, you will be prompted to enter a website. This is the site you will scrape. Next, you will have four options: HTML tag, ID, class, and text. All of these options are optional, and leaving them all blank will result in the entire site being returned. When you enter an HTML tag, it will return all elements with that tag and its children. An ID will return the element with the given ID and its children. A class will return all elements with that class name and its children. If you enter more than one parameter, it will return only the elements that meet all the criteria.

<strong>Output:</strong>

After you enter all the parameters that you wish to input, you will be prompted to choose a directory to save your output. The output will be saved as a txt file with commas separating the different elements.

<strong>Libraries:</strong>

the libraries that PyScrape uses are `requests`, `datetime`, `time`, `bs4`, `colorama`, `tkinter`. You can install these using the `pip` command 
```poweshell
pip install requests
```
```poweshell
pip install datetime
```
```poweshell
pip install time
```
```poweshell
pip install bs4
```
```poweshell
pip install colorama
```
```poweshell
pip install tkinter
```

<strong>Images: </strong>

<img src="pictures/Site Example.png" alt="Website with inspect console open">

<img src="pictures/Web Scrape Example.jpg" alt="PyScrape console axample">

<img src="pictures/Output Example.png" alt="Content of the div of the website">

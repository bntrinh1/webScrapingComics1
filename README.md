# webscrapingComics
First Attempt Ever of Data Scraping

# 1. Introduction
Back in Spring 2018, my roommate asked me to help her attempt to get the names of all the colleges and professors in the University of Oklahoma (UO) for one of her 300 level Sociology class. With over 1000 faculty members working for the university, it was a boring and tedious task. I begun looking on the web for ways, if any, to automate this process. I then came across the concept of "data scraping", a term I have heard before but did not know how to implement. At the time, I was a complete amateur at coding and ended up manually going through every knook and cranny of the UO website in order to help my roommmate. However, I truly believed that another day will come where I will need to scrape up data in the future and took it upon myself to learn the process. Specifically, I successfully taught myself how to scrape up comic images from the XKCD website. I thought of adding a "scheduled download" feature and had plans of implementing it, but never got around to it. I also planned to further my data scraping technique by implement a similar process on Reddit, a website I go on regularly.

# 2. Features
* loads the XKCD website homepage
* Saves the comic image that is always on the homepage
* "Clicks" on the next comic link
* repeats this "clicking" until it reaches to the first comic (by default) or a certain amount of comics
* begins downloading the images with the "request" module
* Notes the url of the current comic being downloaded using "Beatiful Soup", a Python package used to scrape data from HTML sites
* Saves to the harddrive using iter_content()
* Continues this process until it gets back to the homepage comic

# 3. Notes
* In other practical practical uses, I could use this data to backup entire websites and copy all messages in a forum post (like reddit), depending on how hard it is to figure out the URL I need to pass in the request.get()

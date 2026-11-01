# WebScraper

How to use your scraper?

--I used the github code editor for this instead of the terminal; so all I had to do was run the file. However, in the terminal I would assume you would need to 
* chmod +x WebScraper.py
* Then run it or use ./WebScraper
Exactly how I used the the scraper was in the github codeeditor that runs through vscode, and I could run the code directly through the editor

--Describes the performance impact of using functional programming and concurrent.futures:
For the code I decided just to scrape the course page for CSE 20589. And within the code I made a varible called "urls".
This varible takes "base varible", which in this case is "https://pnutz.h4x0r.space/courses/cse.20589.fa26/index.html", and adds onto the url. I decided just to scrape the first 5 reading asssignments, and scrap all the urls of their data. 

* The functional programming in this code, cleans up the urls and HTML tags and removes all extra white space, as well as, applys map and lambda on all of the headers one by one.

* The concurrent.futures in this code allows us to work and make requests on all 5 urls simultaneously, instead of waiting for:
https://pnutz.h4x0r.space/courses/cse.20589.fa26/reading01.html to finish, then move onto https://pnutz.h4x0r.space/courses/cse.20589.fa26/reading02.html, and so on.
this allows for a far more time effecient scraper and proccessing speed. 

These together allow us to use map and lambda on all 5 requests simultaneously; as well as scrape multiple urls at once while removing whitespace, and making them neat and clean strings; as well as preventing
errors and printing/returning alot of unnecessary infroamtion or charaters.

--Screenshots:
<img width="545" height="706" alt="Scraper image 1" src="https://github.com/user-attachments/assets/12a32395-fcb9-4d51-966d-64bc10ce4c5f" />
<img width="602" height="671" alt="Scraper image 2" src="https://github.com/user-attachments/assets/1790e85e-810c-48d0-8142-7748f891ead0" />
<img width="555" height="816" alt="Scraper Image 3" src="https://github.com/user-attachments/assets/cd4d8ce0-6f45-46c8-8154-c9cff06cd5c2" />
<img width="590" height="820" alt="Scraper Image 4" src="https://github.com/user-attachments/assets/99c1dd88-333f-4530-8633-93b76a3bda07" />
(For better viewability and incase these dont work, I added the screenshots directly into the repository)

# Homework 4 - Web Archiving, part 2

## Assignment

### Q1. Analyze Datetimes of Mementos.

In this question, my objetive was to determine how well each URI was archived over time by examining the number and age of its mementos. To achieve this, I created a Python script that processes compressed JSON files containing the TimeMaps. These files were saved as part of [Homework 3 (Web Archiving Part 1)](https://github.com/jgbotello/Web-Science/tree/main/HW3-Web%20Archiving/get%20Timemaps/timemaps).

The script decompresses each .json.gz file and extracts the datetime of the earliest memento for each URI-R. Using the date when the TimeMaps were collected as a reference point, I calculate the age in days between the collection date and the earliest memento datetime. The script also counts the total number of mementos for each URI-R.

With this data, I generate a scatterplot using Matplotlib and Pandas. The x-axis represents the age of each URI-R in days, and the y-axis shows the number of mementos. This visualization allows me to observe patterns in the archival frequency of different URIs.

the output of the scrips shows the scatter plot, The URI-R and date of the oldest memento, and the number of URI-Rs with an age of less than 1 week. The image below shows the output.

<img src="Images/output.png" height="500" alt="">

**Q: What can you say about the relationship between the age of a URI-R and the number of its mementos?**
The correlation between the age of a URI-R (in days) and the number of its mementos is 0.384. This suggests a positive but moderate correlation.

Interpretation: Older URI-Rs tend to have more mementos, but the relationship is not very strong. This means that while age contributes to the number of mementos, other factors (like importance, popularity, or frequency of updates) may also influence how often a URI-R is archived.


**Q: What URI-R had the oldest memento? Did that surprise you?**
The URI-R with the oldest memento is: https://www.washington.edu/

The date of the oldest memento is October 18, 1996.
Does it surprise me?
Yes, it is somewhat surprising because 1996 represents an early period in web history when web archiving efforts were just starting (e.g., the Internet Archive was founded in 1996). The fact that a memento from 1996 exists indicates that this URI-R is likely a well-established and historically significant website.


**Q: How many URI-Rs had an age of < 1 week, meaning that their first memento was captured the same week you collected the data?**                                                              
The number of URI-Rs with an age of less than 1 week is 0.

Interpretation: This means that none of the analyzed URI-Rs had their first memento captured in the same week as the data collection (July 2024). This could indicate that the analyzed URI-Rs have all been archived at least once in the past and are not newly observed web pages.


### Q2. Explore Conifer and ReplayWeb.Page

Create an account at [Conifer](https://conifer.rhizome.org) and create a collection.  Archive at least 10 webpages related to a common topic that you find interesting. Make the collection public and include the link to your collection in your report.

*Q: Why did you choose this particular topic?*

*Q: Did you have any issues in archiving the webpages?*

*Q: Do the archived webpages look like the original webpages?*

After creating your collection at Conifer, download the collection as a WARC file (see [Exporting or Downloading Content](https://guide.conifer.rhizome.org/docs/manage-sessions/exporting-warc/)).

Then load this WARC file into [ReplayWeb.page](https://replayweb.page), a tool from the Webrecorder Project (folks who developed Conifer).  From <https://webrecorder.net/tools>:

<blockquote>ReplayWeb.page provides a web archive replay system as a single web site (which also works offline), allowing users to view web archives from anywhere, including local computer or even Google Drive. See the <a href="https://replayweb.page/docs">User guide</a> for more info.</blockquote>

Once the WARC file has loaded, click on the "Pages" tab.  Take a screenshot that includes the list of pages and the browser address bar (showing `replayweb.page/?source=file%3A%2F%2F`..., which indicates that the WARC file is being loaded from your local computer).

Then click on the "URLs" tab and choose "All URLs" from the dropdown menu.  

*Q: How many URLs were archived in the WARC file?  How does this compare to the number of Pages?*

Create a bar chart showing the number of URLs in the WARC file for each of the file types in the dropdown menu.

*Q: Which file type had the most URLs?  Were you surprised by this?*

## Submission

You should be working in the private GitHub repo that I created for you in the [odu-cs432-websci organization](https://github.com/odu-cs432-websci/) (your repo URL should look something like https<nolink>://github.com/odu-cs432-websci/spr24-*username*/). 

If you are working locally, make sure that you have committed and pushed your local repo, including `HW4-report.md` and any images you reference, to GitHub. 

Submit the URL of your report (*not the URL of your repo*) in Canvas under HW4. This should be something like  
https<nolink>://github.com/odu-cs432-websci/spr24-*username*/blob/main/HW4-report.md

*If you make changes to your report after submitting in Canvas, I will use the last commit time in your repo as your assignment submission time.*

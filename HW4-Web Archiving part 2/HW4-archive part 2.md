# Homework 4 - Web Archiving, part 2

## Assignment

**Important:** This assignment is a continuation of HW3. If you did not complete HW3 satisfactorily, contact me for instructions on how to proceed. This **cannot** be done at the last minute.

### Q1. Analyze Datetimes of Mementos.

In Q1 of Homework 4, I conducted an analysis of the archival quality of the URIs collected in HW1 by leveraging the TimeMaps saved previously. My objective was to determine how well each URI was archived over time by examining the number and age of mementos. To achieve this, I created a Python script that processed the compressed JSON files containing the TimeMaps. The script first decompressed each .json.gz file and extracted the datetime of the earliest memento for each URI-R. Using the collection date as a reference point, I calculated the age in days between the collection date and the earliest memento datetime. Additionally, the script counted the total number of mementos for each URI-R. With this data, I generated a scatterplot using Matplotlib and Pandas, where the x-axis represented the age of the URI-R in days, and the y-axis depicted the number of mementos. This visualization allowed me to observe patterns in the archival frequency of different URIs, revealing insights into the persistence and accessibility of web resources over time.

**Q: What can you say about the relationship between the age of a URI-R and the number of its mementos?**

**Q: What URI-R had the oldest memento? Did that surprise you?**

**Q: How many URI-Rs had an age of < 1 week, meaning that their first memento was captured the same week you collected the data?**                                                              
                                                                      
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

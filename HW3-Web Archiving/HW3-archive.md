# Homework 3 - Web Archiving, part 1 

The purpose of this assignment is to introduce the concept of web archiving and mementos by obtaining TimeMaps through the installation and use of Memgator.

## Downloading Memgator

To start, I tested the installation of Memgator in my computer using the specific command showed below.

**Test out my installation of memgator**
./memgator-darwin-amd64 -a https://raw.githubusercontent.com/odu-cs432-websci/public/main/archives.json -F 2 -f JSON https://www.cs.odu.edu/~mweigle/ > mweigle-tm.jsonon

The result showed a timemap for the website of Dr. Weigle.

<img src="Images/test_install_memgator.PNG" height="500" alt="">

**What do the -F 2 and -f JSON options do?**
According to the documentation provided by the creators of Memgator in their Github F an f have the following funtionalities:

-**F 2:** Sets the failure tolerance limit for each archive. This determines how many failures are acceptable before stopping the process. In this case two.

-**f JSON:** This option specifies the output format of the aggregated TimeMap. By setting -f JSON, we instruct Memgator to output the TimeMap in JSON format.

## Q1. Get TimeMaps for Each URI.

In this part of the process, I obtained the [TimeMaps](http://www.mementoweb.org/guide/quick-intro/) for each of the unique URIs I collected in HW1 using the [MemGator Memento Aggregator](https://github.com/oduwsdl/MemGator). For this task I made a [python script] (https://github.com/jgbotello/Web-Science/blob/main/HW3-Web%20Archiving/get%20Timemaps/get_timemaps.py) that was then executed from the command line. 

The process included generating the TimeMaps in JSON format for each URI and saving them, making sure to include a 15-second break between each request to avoid connection errors or crashes from the web archives. During the process, I encountered some URI-Rs that had no mementos, which was expected. For very large TimeMaps, I opted to compress the files individually using a python [gzip](https://github.com/jgbotello/Web-Science/blob/main/HW3-Web%20Archiving/get%20Timemaps/compress.py) to better manage storage space and facilitate further analysis. Finally, I uploaded all the generated TimeMaps to a [repository on GitHub] (https://github.com/jgbotello/Web-Science/tree/main/HW3-Web%20Archiving/get%20Timemaps/timemaps), organizing them in a separate folder from the report for use in future tasks.

### Q2. Analyze Mementos Per URI-R.

Use the TimeMaps you saved in Q1 to analyze how well the URIs you collected in HW1 are archived.

Create a table showing how many URI-Rs have certain number of mementos.  For example

|Mementos | URI-Rs |
|---------:|--------:|
|   0     |  250   |
|   1     |  100   |
|   7     |   50   |
|   12     |   25   |
|   19     |   25   |
|   24     |  20  |
|   30     |   27   |
|  57     |    3   |

If you are using LaTeX, you should create a [LaTeX table](https://www.overleaf.com/learn/latex/tables) -- don't submit a spreadsheet or image of a table created in something else.  If you are using Markdown, you can view the source of this file for an example of how to generate a table.

If you will end up with a very large table of memento counts, you can bin the number of mementos.  Just make sure that the bin sizes are reasonable and that you specify how many had 0 mementos individually. The target is to have no more than 15-20 rows so that your table can fit on a single page.  For example

|Mementos | URI-Rs |
|---------:|--------:|
|   0     |  250   |
|   1-10     |  150   |
|   11-20     |   50   |
|   21-30     |   47   |
|  57     |    3   |

*Q: What URI-Rs had the most mementos?  Did that surprise you?*
 


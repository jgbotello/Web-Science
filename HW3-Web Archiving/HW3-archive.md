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

-F 2: Sets the failure tolerance limit for each archive. This determines how many failures are acceptable before stopping the process. In this case two.

-f JSON: This option specifies the output format of the aggregated TimeMap. By setting -f JSON, we instruct Memgator to output the TimeMap in JSON format.

## Q1. Get TimeMaps for Each URI.

In this part of the process, I obtained the [TimeMaps](http://www.mementoweb.org/guide/quick-intro/) for each of the unique URIs I collected in HW1 using the [MemGator Memento Aggregator](https://github.com/oduwsdl/MemGator). para esta tarea se realizo un script de python que luego fue ejecutado desde la linea de comando (See image of the script below).  


Notes:
* As described in [EC-memgator](https://github.com/odu-cs432-websci/public-spr24/blob/main/getting-started/EC-memgator.md), you **must** include the `-c` and `-a` options to specify your contact information and to use the alternate `archives.json` file.
* When running this for all of your URIs, you might want to use the MD5 hash that you recorded earlier as part of the filename to help keep track of which TimeMaps you have.
* You will want to add a sleep (at least 10-20 seconds) between each call to MemGator because if you make too many requests too quickly, you will get "connection refused" errors (or worse, get blocked by an archive). 

**Important:** Obtaining TimeMaps requires contacting several different web archives for each URI-R.  *This process will take time.*

Look at the MemGator options and figure out how to process the output before running the entire process. 

Note that if there are no mementos for a URI-R, MemGator will return nothing. *Don't be surprised if many of your URI-Rs return 0 mementos.*  Remember the ["How Much of the Web is Archived" slides](https://docs.google.com/presentation/d/132sObERXgzGbxVETIc8QblUyuXB6X7lDbrbhCKmAKzU/edit#slide=id.g80c031ceb5_0_91) -- there are lots of things on the web that are not archived.  If you want to do a sanity check on a few, you can manually use the Wayback Machine and see what you get from the Internet Archive.  (Remember though that MemGator is going to query several web archives, not only the Internet Archive.)

If you uncover TimeMaps that are very large (e.g., for popular sites like <https://www.cnn.com/>) and swamp your filesystem, you have two options:
* Manually remove those URI-Rs from your dataset (but note this in your report), or
* Compress each TimeMap file individually (using pipe to `gzip` in the same command when downloading or after the download is completed). These compressed files can be used for further analysis by decompressing on the fly using commands like `zcat` or `zless` (or using gzip libraries in Python).

Finally, upload the TimeMaps to your GitHub repo -- you'll also use these for Q2 and HW4.  Put them in a separate folder, not the same folder as your report.
* To upload/commit a large number of files to GitHub, [use the command line](https://docs.github.com/en/github/managing-files-in-a-repository/adding-a-file-to-a-repository-using-the-command-line).

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
 


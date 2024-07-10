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

In this part of the process, I obtained the [TimeMaps](http://www.mementoweb.org/guide/quick-intro/) for each of the unique URIs I collected in HW1 using the [MemGator Memento Aggregator](https://github.com/oduwsdl/MemGator). For this task I made a [python script](https://github.com/jgbotello/Web-Science/blob/main/HW3-Web%20Archiving/get%20Timemaps/get_timemaps.py) that was then executed from the command line. 

The process included generating the TimeMaps in JSON format for each URI and saving them, making sure to include a 15-second break between each request to avoid connection errors or crashes from the web archives. During the process, I encountered some URI-Rs that had no mementos, which was expected. For very large TimeMaps, I opted to compress the files individually using [gzip](https://github.com/jgbotello/Web-Science/blob/main/HW3-Web%20Archiving/get%20Timemaps/compress.py) in python to better manage storage space and facilitate further analysis. Finally, I uploaded all the generated TimeMaps to a [repository on GitHub](https://github.com/jgbotello/Web-Science/tree/main/HW3-Web%20Archiving/get%20Timemaps/timemaps), organizing them in a separate folder from the report for use in future tasks.

### Q2. Analyze Mementos Per URI-R.

I used the TimeMaps saved in Q1 to analyze the archival quality of the URIs collected in HW1. By examining the TimeMaps, I was able to determine how well each URI was archived over time. The table below displays the number of URI-Rs (original resource URIs) and the corresponding number of mementos (archived versions) they have. Notese que 70 de las URI-R no contenian informacion de Mementos. 

|Mementos | URI-Rs |
|---------:|--------:|
0        | 70
1        | 6
2        | 19
3        | 7
4        | 8
5        | 4
6        | 3
7        | 5
8        | 3
10       | 2
11       | 3
12       | 3
13       | 4
15       | 1
16       | 1
18       | 6
19       | 9
20       | 1
21       | 4
23       | 2
24       | 4
25       | 5
26       | 2
27       | 6
28       | 7
29       | 4
30       | 5
31       | 5
32       | 5
33       | 6
34       | 2
35       | 4
36       | 6
37       | 4
38       | 3
39       | 3
41       | 3
42       | 1
43       | 1
44       | 3
45       | 3
46       | 2
48       | 1
49       | 3
50       | 1
51       | 1
52       | 1
54       | 1
55       | 1
57       | 2
58       | 1
59       | 4
60       | 2
62       | 2
64       | 2
65       | 3
68       | 1
69       | 1
70       | 1
73       | 1
74       | 1
75       | 1
76       | 3
79       | 1
80       | 2
82       | 1
93       | 2
96       | 2
102      | 1
104      | 1
105      | 1
106      | 2
107      | 1
109      | 2
110      | 1
116      | 2
117      | 2
122      | 3
125      | 2
126      | 1
129      | 1
130      | 2
133      | 1
136      | 2
139      | 2
140      | 1
144      | 1
148      | 1
156      | 1
158      | 1
159      | 1
162      | 1
183      | 1
191      | 1
193      | 1
199      | 2
201      | 1
207      | 1
208      | 2
209      | 1
210      | 1
219      | 1
229      | 1
235      | 1
236      | 1
237      | 1
240      | 1
242      | 1
246      | 1
252      | 1
259      | 1
260      | 1
267      | 1
268      | 1
273      | 1
274      | 1
277      | 1
285      | 1
291      | 1
298      | 1
313      | 2
325      | 1
341      | 1
343      | 2
347      | 1
376      | 1
388      | 1
392      | 1
393      | 1
423      | 1
448      | 3
460      | 1
462      | 1
543      | 1
547      | 1
584      | 1
606      | 1
696      | 1
731      | 1
862      | 1
877      | 1
1138     | 1
1454     | 1
1600     | 1
1609     | 2
1789     | 1
1973     | 1
2185     | 1
2768     | 1
3339     | 1
3688     | 1
3907     | 1
4455     | 1
4920     | 1
5660     | 1
5791     | 1
6024     | 1
6073     | 1
7593     | 1
8306     | 1
8456     | 1
8698     | 1
9262     | 1
11592    | 1
13271    | 2
24203    | 1
25546    | 1
30853    | 1
41899    | 1
44551    | 1
52667    | 1
56325    | 1
58170    | 1
60878    | 1
63045    | 1
68569    | 1
78476    | 1
84159    | 1
101919   | 1

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
 


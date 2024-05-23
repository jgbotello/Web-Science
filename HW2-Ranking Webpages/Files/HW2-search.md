# Homework 2 - Ranking Webpages

Read through the entire assignment before starting.  *Do not wait until the last minute to start working on it!* 
 
## Assignment

This assignment will have you investigate different ways to rank webpages based on a query.  

### Q1. Data Collection

To perform the tasks of this assignment, several Python scripts were used, executed through the Command Prompt of the Windows 11 operating system.

*Link Collection:*
A Python script ('collect-webpages_HW2') was used to collect the links, which, using the requests module and BeautifulSoup, obtains URIs of web pages. The script was executed from the command line by providing the initial URL as an argument. [This was done in assignment one where the URIs were stored in a .txt file.]

*Download HTML Content:*
Another script ('Download_html') was used to download the HTML content of the collected URIs. This script uses the requests module to perform the HTTP requests and saves the HTML content in individual files by hashing the URIs. The execution of the script was performed from the command line by providing the text file containing the links. The HTML files were stored in a folder named 'html_files'. An additional file was also created in text format containing the URIs with the respective HTML document name for future mapping.

*Removing Standard HTML Text:*
Another script was used to process the HTML content and remove the standard HTML text, using the boilerpy3 library. This script was run from the command line providing the folder containing the downloaded HTML files. However, the result of this was a folder that resulted in 0B size file. After reviewing the HTML files I could conclude that this was because it is all boilerplate.

*Word Occurrence Counting:*
A python script was developed to search for HTML files containing a particular word. In this case I had obtained URIs using as seed the ODU home page (https://www.odu.edu/), so I searched the documents for the word 'payment'. The script counts how many HTML documents contain the word, displays the name of the document and in front displays a count of the occurrences of the word. The execution was carried out from the command line, providing the search word and the folder containing the processed files.

*Cálculo de TF-IDF:*
Finalmente, se utilizó un script para calcular los valores de TF-IDF para una palabra de consulta en los documentos procesados. Este script realiza cálculos basados en TF (frecuencia del término), IDF (frecuencia inversa del documento) y TF-IDF. La ejecución se realizó desde la línea de comandos, proporcionando la palabra de consulta y la carpeta que contiene los archivos procesados.


*Q: How many of your 500 URIs produced useful text?  If that number was less than 500, did that surprise you?* 


### Q2. Rank with TF-IDF

Se utilizo la palabra payment para realizar el query. Se encontro que 55 docuemntos contenian la palabra por lo que se seleccionaron 10 de ellos para ser analizados, es decir, realizar el calculo de TF-IDF. A continuacion se presenetan los titulos de los archivos seleccionados.


Para calculo de TF:
$$ TF =  Occurrences in doc / Words in doc $$

Para calculo de IDF: 

$$ log2(total docs in corpus / docs with term) $$

Para calculo de TF- IDF:
$$ TF-IDF = TF x IDF  $$

I used 4 Billion as the total size of the corpus

I found 55 files with the word payment

|File	|Occurrences| TF | IDF  | TF-IDF |URI
|------:|---:|---:|-----:|---
|1. b888c1304aad38d83cbdc0cf8313b56a.html| 31 |  0.0068 | 26.12 | 0.1776 |https://www.odu.edu/tuition-aid/tuition/military
|2. f375ea5621c5676f9d431daed8eb50fc.html| 16 |  0.0146 | 26.12 | 0.3813 |https://www.odu.edu/tuition-aid/tuition
|3. 0cee0fbd65390f0fe2d5dae4aa68f7de.html| 11 |  0.0089 | 26.12 | 0.2324 |https://www.odu.edu/article/class-of-2022-ivan-santiago-finds-his-calling-for-leadership-through-cybersecurity
|4. 8057ae4fb4d69d9340b85eab38d07124.html| 9  |  0.0042 | 26.12 | 0.1097 |https://www.odu.edu/about/visitors/parking-information
|5. 46d8bc4647e77b3a654414e53eabf6c9.html| 6  |  0.0046 | 26.12 | 0.1201 |https://www.odu.edu/vendors
|6. 3eb83f607322576033c342f42e6a27eb.html| 3  |  0.0037 | 26.12 | 0.0966 |https://www.odu.edu/procurement
|7. fa158ea5eff0cda03a838fbac842da20.html| 5  |  0.0028 | 26.12 | 0.0731 |https://www.odu.edu/academics/academic-records/transcripts
|8. d7c9ec6ecc6e5f8b40585220930eb6f5.html| 2  |  0.0010 | 26.12 | 0.0261 |https://www.odu.edu/finaidoffice/summer
|9. c9f449e22a840379b0b87df9b4fd4618.html| 2  |  0.0016 | 26.12 |  0.0417 |https://www.odu.edu/admission/admitted/graduate
|10. c4dbeeb75d56d35d0dcaa57e71384d8d.html| 2  |  0.0020 | 26.12 | 0.0522 | https://www.odu.edu/honors

10 Hits for the term "payment", ranked by TF-IDF.
2. https://www.odu.edu/tuition-aid/tuition
3. https://www.odu.edu/article/class-of-2022-ivan-santiago-finds-his-calling-for-leadership-through-cybersecurity
1. https://www.odu.edu/tuition-aid/tuition/military
5. https://www.odu.edu/vendors
4. https://www.odu.edu/about/visitors/parking-information
6. https://www.odu.edu/procurement
7. https://www.odu.edu/academics/academic-records/transcripts
10. https://www.odu.edu/honors
9. https://www.odu.edu/admission/admitted/graduate
8. https://www.odu.edu/finaidoffice/summer
 

### Q3. Rank with PageRank

Now rank the *domains* of those 10 URIs from Q2 by their PageRank.  Use any of the free PR estimators on the web,
such as:
* https://searchenginereports.net/google-pagerank-checker
* https://dnschecker.org/pagerank.php
* https://smallseotools.com/google-pagerank-checker/
* https://www.duplichecker.com/page-rank-checker.php

Note that these work best on domains, not full URIs, so, for example, submit things `https://www.cnn.com/` rather than `https://www.cnn.com/world/live-news/nasa-mars-rover-landing-02-18-21`.

If you use these tools, you'll have to do so by hand (most have anti-bot captchas), but there are only 10 to do.  

Normalize the values they give you to be from 0 to 1.0.  Use the same tool on all 10 (again, consistency is more important than accuracy). 

Create a table similar to Table 1:

Table 2.  10 hits for the term "shadow", ranked by PageRank of domain.

|PageRank	|URI
|-----:|---
|0.9|		http://bar.com/
|0.5	|	http://foo.com/

*Q: Briefly compare and contrast the rankings produced in Q2 and Q3.*

## Extra Credit

### Q4. *(2 points)* 
Compute the [Kendall Tau_b score](https://en.wikipedia.org/wiki/Kendall_rank_correlation_coefficient#Tau-b) for the lists from Q2 and Q3 (use "b" because there will likely be tie values in the rankings). Report both the Tau value and the "p" value.

### Q5. *(3 points)*  
Build a simple (i.e., no positional information) inverted file (in ASCII) for all the words from your 500 URIs.  Upload the entire file your GitHub repo and discuss an interesting portion of the file in your report.
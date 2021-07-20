# Well_list

When:
Summer of 2021, Internship at Scout Energy Patners 

Task:
Populate a excel sheet from old COP files (pdf files). Extract information from the pdfs, and put the info into the designated cell.

Column Headers:
Name,	API #,	Tax Group,	Accounting ID,	'Fully Screen, has been fraced?',	Potential Hazards,	Spud Date,	Zone Stimulated,	Frac Date,	Casing Type,	Perforated (y/n),	Feet of Perfs,	Open Hole Feet,	Number of Stages,	Total Load (bbls),	Total Sand (#s),	Total N2 (SCF),	Comments,	Stg 1Sand (#s),	Stg 1 Stg Feet,	Stg 1 Sand type,	Stg 1 Avg. Pressure (PSI),	Stg 1 Max Pressure (PSI),	Stg 1 Avg. Pump Rate (BPM),	Stg 1 Max Pump Rate (BPM),	Stg1 ISIP (PSI),	Stg 2 Sand (#s),	Stg 2 Sand type,	Stg 2 Stg Feet,	Stg 2 Avg. Pressure,	Stg2 Max Pressure,	Stg 2 Avg. Pump Rate, 	Stg 2 Max Pump Rate,	Stg 2 ISIP,	Stg 3 Sand (#s),	Stg 3 Sand type,	Stg 3 Stg Feet,	Stg 3 Avg. Pressure,	Stg 3 Max Pressure,	Stg 3 Avg. Pump Rate, 	Stg 3 Max Pump Rate,	Stg 3 ISIP

Background:
This was my main and my first project at my internship for Scout Energy Patners. 

Process:
To complete this project, I broke down the steps into multiple parts. For each different column title, I was to extract the information from the pdfs. Even though this strategy is not efficient as extracting row by row, it still saved me time from manually filling out the cells. Each row had the API #, which could be found the pdf. Thus, I was able to locate the cell by using the API # to get the row and column name to get the column. 

To extract the info, I used PyPDF2 to extract text from the pdf. Then, I was able to parse the information based on date format and keywords. Once I got the information that I needed, I used openpyxl to populate the cell. I repeated this process until all the cells were filled. Then I saved this workbook.

To make sure that I filled the excel sheet correctly, I manually verified the data and put it the minor details that I missed with my python script. Manually doing this would be around 12 days. I was able to complete the work & code in less than a week or so, meaning that we were able to save 5+ days b/c of automation.

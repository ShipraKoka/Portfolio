### Studio Ghibli Reports


##### Report 1 - Films Per Decade
------
The first report is a column chart that displays the number of movies released every decade since the 1960s.

**Lessons Learned**  
The chart initially displayed each year of the ReleaseDate along the x-axis. 19 columns were displayed, with 2 of them representing 2 films each for the year they were released, thus accounting for all 21 films in the database. Since I wanted the chart to display the number of movies released each decade, I initially modified the horizontal axis properties. I set the x-axis type to scalar and set the axis range with a minimum of 1960, maximum of 2020, and interval of 10. This adjustment resulted in each decade being displayed along the axis instead of each year. However, the 19 columns still remained. 

To get each column to represent the total number of movies per decade I found that I needed to write expressions for the category group properties. I wrote a SWITCH statement that would aggregate the values for each decade:  
```  
    =Switch(Fields!ReleaseDate.Value >= 1960 and Fields!ReleaseDate.Value < 1970, 1, Fields!ReleaseDate.Value >= 1970 and 
    Fields!ReleaseDate.Value < 1980, 2, Fields!ReleaseDate.Value >= 1980 and Fields!ReleaseDate.Value < 1990, 3,  
    Fields!ReleaseDate.Value >= 1990 and Fields!ReleaseDate.Value < 2000, 4, Fields!ReleaseDate.Value >= 2000 and 
    Fields!ReleaseDate.Value < 2010, 5, Fields!ReleaseDate.Value >= 2010 and Fields!ReleaseDate.Value < 2020, 6)
```
and then wrote another one to set labels that would correspond to those aggregated values:  
```  
    =Switch(Fields!ReleaseDate.Value >= 1960 and Fields!ReleaseDate.Value < 1970, "1960s", Fields!ReleaseDate.Value >= 1970 and
    Fields!ReleaseDate.Value < 1980, "1970s", Fields!ReleaseDate.Value >= 1980 and Fields!ReleaseDate.Value < 1990, "1980s",
    Fields!ReleaseDate.Value >= 1990 and Fields!ReleaseDate.Value < 2000, "1990s", Fields!ReleaseDate.Value >= 2000 and
    Fields!ReleaseDate.Value < 2010, "2000s", Fields!ReleaseDate.Value >= 2010 and Fields!ReleaseDate.Value < 2020, "2010s",
    true, 0)  
```  
As a result, the chart now displays columns, each representing the number of films released every ten years.

##### Report 2 - Film Ratings
------
The second report is a matrix that displays the rating for each film.

**Lessons Learned**  
I set the Column Group to Rating and Row Group to Title. Since I wanted the appropriate rating highlighted for each title, I set the Data text box to Rating as well. As a result, the boxes contained text instead of the light purple highlight you now see on the report. It seemed redundant to have a G, PG or PG-13 in every row, with the column headings already providing that information. I thought of replacing the text with check marks, but ultimately decided to control the fill color with an expression using an IIF statement:  
```  
    =IIF(IsNothing(Fields!Rating.Value), Nothing, "Plum")  
```

##### Report 3 - Ghibli Movies
------
The third report is a table that displays the film title, its director, rating, runtime and release date, and has interactive sorting enabled for each column. 

**Lessons Learned**  
I wanted to export the report to a pdf file to push onto my Github, but noticed extra blank pages being saved. Most of the table took up the first page, while the last row ended up on the third page. The second and fourth pages were blank, despite the fact that the preview showed the entire table on one page. I found that decreasing the width of the body properties, as well as the right and left margins of the report properties got rid of those extra pages and kept the table from splitting up after exporting it to pdf.

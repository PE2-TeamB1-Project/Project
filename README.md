# <u>manual</u>

## __Introduction__

+ The Program Engineering 2 : Team Project to make analysis package
+ Team B1
    * Choi il-gyu
    * Kim Kang Seok
    * Song jun su

## Objective of project

Analysing the data in xml files and show the contents to <u>csv file</u> and <u>graphs plotting data</u>(_I-V graph, transmission-wavelength graph_)

## Structure of Package

+ document : .gitignore and README.md(explaining how to use our package)
+ module 
    - error : find the error(out to standard)
    - extract : bring the wafer name, experiment date, TestSiteinfo, wavelength
    - filter : filter the unuseful xml file
    - fitting : fit and show the approximation from IV graph and transmission spectra-wavelngth graph
    - get_result : make the dataframe and stored by csv file and images
    - i_none : the current value at -1V on IV graph
    - i_one : the current value at 1V on IV graph
    - option : selective messages to run the package
    - plot : plot the graph from extracted data(ex..I-V graph, transmission spectra-wavelength graph)
    - png_signal : If there is no png file, we can't make Hyperlink, so we need to know the existence of png files
    - rsq_fit : R Square value of Current data and Voltage data
    - rsq_ref : R Square value of transmission and 7th wavelength
+ run.py : the last move button

## Example of analysis Result
<img src="./document/B1_1.png" width="400">
<img src="./document/B1_2.png" width="400">
<img src="./document/B1_3.png" width="400">

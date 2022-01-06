# Election_Analysis

## Project Overview
A Colorado Board of Elections has asked that an audit be completed for a recent congressional election. The board of election has asked that the audit verify the following:

- Total number of votes cast in the election
- A complete list of candidates who received votes
- Total number of votes each candidate received
- Percentage of votes each candidate received
- The winner of the election based on popular vote

The audit will review a data file provided by the board of election. This file contains the following data:

- a number for the ballot ID
- name for the county
- The name of the candidate receiving the vote


![](Resources/data-3-3-1-first-10-rows.png)


## Summary of Results

The audit found that there were **369,711 total votes** cast in the congressional precinct. 

The precinct consisted of the following counties: 

<table>
<tr>
<th>County</th>
<th>Percent of votes cast</th>
<th>Count of votes cast</th>
<th>Largest County to Vote</th>
</tr>
<tr>
<td>Jefferson</td>
<td>10.5%</td>
<td>38,855</td>
<td></td>
</tr>
<tr>
<td>Denver</td>
<td>82.8%</td>
<td>306,055</td>
<td>&#10004</td>
</tr>
<tr>
<td>Arapahoe</td>
<td>6.7%</td>
<td>24,801</td>
<td></td>
</tr>
</table>


The audit found the following candidates received votes in the audited election:

<table>
<tr>
<th>Candidate </th>
<th>Percent of votes cast</th>
<th>Count of votes cast</th>
<th>Winner of Vote</th>
</tr>
<tr>
<td>Charles Casper Stockham</td>
<td>23.0%</td>
<td>85,213</td>
<td></td>
</tr>
<tr>
<td>Diana DeGette</td>
<td>73.8%</td>
<td>272,892</td>
<td>&#10004</td>
</tr>
<tr>
<td>Raymon Anthony Doane</td>
<td>3.1%</td>
<td>11,606</td>
<td></td>
</tr>
</table>

## Audit Summary

The solution utilized for this audit was built specifically for the Colorado congressional election. The solution built for the Colorado congressional election is generic enough that with a couple of easy changes it could work for any election.

1. Currently the solution has the input file hard coded into the application. With a rather simple addition of a file selection utility any file in the defined election format can be analyzed and audited.
2. The current solution was built with a very limited scope. A single race for a single congressional seat. This could be addressed by adding a couple of new fields to the data file: 
	- This solution would work for any state level election. It would not work for a national level election, like president or vice president. If another column were added to the data file for state, and some analysis of the state data column added to the solution, this solution could be utilized to audit just about any election from city mayor all the way up to president.
	- This solution assumes a data file per race. If a field for race were added to the data file, and some analysis which would analyze the race data. This solution could much more useful.


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

<ol>
<li>One easy way this solution could be improved is to utilize a file selection utility. Currently the solution has the input file hard coded into the solution. With a change in the solution from  a coded value of Resources\election_results.csv to utilizing a askopenfilename command to open a windows file dialog and allow the user to identify the file to be process. As long as the selected file was in the identified election format the data could be analyzed, audited, and reported.</li>
<li>A change that would be a little more work would be to change the scope of the solution. The current solution was built with a very limited scope. A single race for a single congressional seat. The current  could data file contains the following fields:
<ul>
<li>a number for the ballot ID</li>
<li>name for the county</li>
<li>The name of the candidate receiving the vote</li>
</ul>
There are a couple of ways the scope of the solution could be changed:
<ul>
<li>The scope could grow to process a national race, but keep the solution processing a single file per race
<ul>
<li>This solution would work for any state level election. It would not work for a national level election, like president or vice president. If we kept the solution to be a single file for a single race, but allowed that race to be a national race like for the president or vice president. If another column were added to the data file for state, and some analysis of the state data column added to the solution, this solution could be utilized to audit just about any election from city mayor all the way up to president. The new data file would like:
<ul>
<li>a number for the ballot ID</li>
<li>name for the county</li>
<li>The name of the candidate receiving the vote</li>
<li>State where the vote was cast</li>
</ul>
</ul>
<li>The scope could grow to allow multiple races per file, but within a single state
<ul>
<li>The other change which could be made to this solution is to support multiple races per file. The current  solution assumes a data file per race. If a field for race were added to the data file, and some analysis which would analyze the race data. This solution could much more useful. The new data file would look like:
<ul>
<li>a number for the ballot ID</li>
<li>name for the county</li>
<li>The name of the candidate receiving the vote</li>
<li>Race the vote is being cast for</li>
</ul>
</ul>
<li>The scope could grow to allow multiple races across states, and include national races in a single file
<ul>
<li>If we combine these two suggestions and build a solution that can take a national data file with all votes cast. The data file would have to include the addition of both of the fields mentioned previously, a state field and a race field. resulting in a new data file looking like:
<ul>
<li>a number for the ballot ID</li>
<li>name for the county</li>
<li>The name of the candidate receiving the vote</li>
<li>Race the vote is being cast for</li>
<li>State where the vote was cast</li>
</ul>
</ul>
</ul>
</ol>


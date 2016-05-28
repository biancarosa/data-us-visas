# Introduction

This is a analysis that uses data from the (United States Department of Labor that contains information about foreign labor)[https://www.foreignlaborcert.doleta.gov/performancedata.cfm] certification requests. We use (disclosure data)[https://www.foreignlaborcert.doleta.gov/docs/Performance_Data/Disclosure/FY16Q2/PERM_Disclosure_Data_FY16_Q2.xlsx] that cover determinations issued between October 1, 2015 through March 31, 2016.

# The script
1. Substituite column names because *rows* doesn't support column names starting with numbers.
2. Print field names and types
3. Print number of certified requests vs denied requests
4. Print number of requests from developers vs requests from non-developers
5. Print number of requests from developers that were certified vs requests from developers that were denied
6. Print number of requests from brazilians vs requests from non-brazilians
7. Print number of requests from brazilians that were certified vs requests from brazilians that were denied

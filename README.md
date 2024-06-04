# SPARQL Paginator

Have you ever been shackled by complex SPARQL queries which take an unacceptable amount of time? No? Oh. Well, I have. The purpose of this simple code is to divide large queries
 into smaller chunks which can be processed by the endpoint, then concatenating the results into a Dataframe.
 
 Obviously the downside to this is an increase in the number of calls, so it is recommended to test the waters previously to check what is the largest subsetting possible for the 
 desired query which still gets results, for the endpoint's sake.
 
 The approach is to first count the total number of items to extract, then get the items ordered so that using LIMIT and OFFSET, we can paginate through the results and combine them.
 
 The provided example gets all the names and surnames available in the endpoint.
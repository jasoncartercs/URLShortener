# URLShortener

This is a URL Shortener written in a Flask App.

It takes a post request on the route shorten_url.

The json should look like this:
	{
		"url": "abc.com"
	}	

It returns a json object that contains the response code the the shortened url:
{
    "code": 200,
    "data": "https://r.com/ON0Euc"
}

This code stores information in one table using a SQLite database.

The structure is: 
	CREATE TABLE IF NOT EXISTS url(
		id integer PRIMARY KEY,
		long_url text NOT NULL,
		short_url text NOT NULL,
	);

I have included the SQLite database to make it easy to run the project. Typically, I would not include this in the repo.



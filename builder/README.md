# Builder

This python script destroys and recreates the database using [MTGJson](https://mtgjson.com/) as the data source.  

## Working on
Moving any existing values on cards that need to be normalized onto their own tables. Continuing down the path of grabbing other fields to include into the ecosystem
Continue to update database service's add_card function to no longer rely on Formatter.
Formatter probably needs to just only work with the console.
* On the other hand, I could benefit from just finding the biggest individual value here.
* All these multi-value functions in cardFormatter can probably be grouped

## TODOs
* Stuff to do after the obvious first step of completing the database is complete:
* Clean up unnecessary items that existed prior to normalization.
* It'd be really nice to have some data validation.
* Additionally I'd like an entity relation diagram of some kind of the underlying database.
* 223 magic number for the progress bar needs to come from json
* All console work might need to be revisited thanks to omitted sets while building initially.
* Could make a version of displaycard that shows what it would look like if each field were maximized
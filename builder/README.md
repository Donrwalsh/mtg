# Builder

This python script destroys and recreates the database using [MTGJson](https://mtgjson.com/) as the data source.  

## TODOs
* Stuff to do after the obvious first step of completing the database is complete:
* Clean up unnecessary items that existed prior to normalization.
* It'd be really nice to have some data validation.
* Additionally I'd like an entity relation diagram of some kind of the underlying database.
* 223 magic number for the progress bar needs to come from json
* All console work might need to be revisited thanks to omitted sets while building initially.
* Could make a version of displaycard that shows what it would look like if each field were maximized
* The variant table appears to be set-specific? Mountain only shows variants within the same set.
* Every associated table except names uses 'card_id' over 'id'
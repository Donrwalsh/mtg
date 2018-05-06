#Builder

This python script destroys and recreates the database using [MTGJson](https://mtgjson.com/) as the data source.  

##TODOs
* Complete cards table import
* Sets table
* Color table
    * Some sort of hierarchy? Thinking about colorIdentity cascading down.
* Currently pulling in 32k cards with sporadic manual verification.
    * Some sort of automated sanity check
    * Error handling anticipating changes to cards in new sets.
        * New fields? Alert when something is there that is not expected
        * For error handling, it'd be nice to spit out a pretty formatted card that hit the error
        * I'm thinking an error class makes a lot of sense.
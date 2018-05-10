# Builder

This python script destroys and recreates the database using [MTGJson](https://mtgjson.com/) as the data source.  

## Do next
Normalize stuff, start with color, colorIdentity and then move on to types/supertypes/subtypes

## Adding new fields
For each new field into the database:
* Writer service's display_card needs an update
    * Alongside this, the card_formatter needs an update for db & console
* database_service add_card needs to account for the new field
* The loop that currently exists in main needs to account for the field.

## TODOs
* Database export needs to be included
    * Maybe an output or some kind of report for longest values by field
* Complete cards table import
    * Itemize remaining fields and all the places they are being added.
* Sets table
* Color table
    * Some sort of hierarchy? Thinking about colorIdentity cascading down.
* Currently pulling in 32k cards with sporadic manual verification.
    * Some sort of automated sanity check
    * Error handling anticipating changes to cards in new sets.
        * New fields? Alert when something is there that is not expected
        * I'm thinking an error class makes a lot of sense.
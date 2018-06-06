## MTG

##### Structure

* Python scripts moving to a subdirectory need to be double-checked so that they still run and put the right stuff in the database.
* How to duplicate static assets across multiple versions of the site?

##### Build the same simple API multiple times with different database connection methods
###### Attack of the Clones

* Verify the 'correctness' of Starter.
* Given that data will be offered up at the API endpoints in a similar way in all cases, maybe there's more Starter can be set up with.
* Classify the task at hand. Itemize each of the available options: 

1. JDBC
  * Driver only. JDBCSimple is an example of what this would look like.
2. JDBCTemplate
  * Take a peak at the benefits that JDBCTemplate adds above just the Driver. Cards from first_attempt utilizes this approach.
3. JPA
  * Connect to the database and deliver API data using the Java Persistence API. No available example for this just yet.
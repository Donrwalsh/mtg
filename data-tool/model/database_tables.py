SETS = ("CREATE TABLE `sets` ("
        "`id` int(11) unsigned NOT NULL AUTO_INCREMENT," 
        "`code` VARCHAR(10) NOT NULL,"
        "`name` VARCHAR(50) NOT NULL,"
        "`type` VARCHAR(50) NOT NULL,"
        "`release_date` DATE,"
        "`block` VARCHAR(50),"
        "`block_code` VARCHAR(10),"
        "`parent_set_code` VARCHAR(10),"
        "`card_count` VARCHAR(5) NOT NULL,"
        "`border` VARCHAR(50),"
        "PRIMARY KEY (`id`) ) ENGINE = InnoDB "
        "DEFAULT CHARSET = utf8;")

SETS_INSERT = ("INSERT INTO sets (code, name, type, release_date, block, "
               "block_code, parent_set_code, card_count, border) VALUES ( ")
#TODO Booster normalized table.
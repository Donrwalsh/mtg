SETS = ("CREATE TABLE `sets` ("
        "`id` int(11) unsigned NOT NULL AUTO_INCREMENT," 
        "`code` VARCHAR(10) NOT NULL,"
        "`name` VARCHAR(50) NOT NULL,"
        "`type` VARCHAR(50) NOT NULL,"
        "`release_date` DATE NOT NULL,"
        "`block` VARCHAR(50) NOT NULL,"
        "`block_code` VARCHAR(10) NOT NULL,"
        "`parent_set_code` VARCHAR(10) NOT NULL,"
        "`card_count` VARCHAR(5) NOT NULL,"
        "`border` VARCHAR(50) NOT NULL,"
        "PRIMARY KEY (`id`) ) ENGINE = InnoDB "
        "DEFAULT CHARSET = utf8;")

#TODO Booster normalized table.
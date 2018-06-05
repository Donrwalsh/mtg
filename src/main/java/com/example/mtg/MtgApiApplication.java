package com.example.mtg;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.data.jpa.JpaRepositoriesAutoConfiguration;
import org.springframework.boot.autoconfigure.domain.EntityScan;
import org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration;
import org.springframework.boot.autoconfigure.jdbc.DataSourceTransactionManagerAutoConfiguration;
import org.springframework.boot.autoconfigure.jms.JndiConnectionFactoryAutoConfiguration;
import org.springframework.boot.autoconfigure.orm.jpa.HibernateJpaAutoConfiguration;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;

@EnableAutoConfiguration(exclude = {JndiConnectionFactoryAutoConfiguration.class,DataSourceAutoConfiguration.class,
        HibernateJpaAutoConfiguration.class,DataSourceTransactionManagerAutoConfiguration.class})

@SpringBootApplication(scanBasePackages={"com.example.mtg"})
@EnableJpaRepositories({"com.example.mtg.repository"})
@EntityScan( basePackages = {"com.example.mtg.persistence.model"})
//@EnableJpaRepositories("com.example.mtg.repository")
public class MtgApiApplication {

    public static void main(String[] args) {
        SpringApplication.run(MtgApiApplication.class, args);
    }
}

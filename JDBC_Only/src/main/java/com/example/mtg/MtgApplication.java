package com.example.mtg;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@EnableAutoConfiguration
public class MtgApplication {

    public static void main(String[] args) {
        SpringApplication.run(MtgApplication.class, args);
    }
}

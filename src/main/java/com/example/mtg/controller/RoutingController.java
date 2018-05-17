package com.example.mtg.controller;

import java.util.concurrent.atomic.AtomicLong;

import com.example.mtg.Helloworld;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@Controller
public class RoutingController {

    private static final String template = "Hello, %s!";
    private final AtomicLong counter = new AtomicLong();

    @RequestMapping("/card")
    public String card() {
        return "card.html";
    }

//    @RequestMapping("/greeting")
//    public Helloworld greeting(@RequestParam(value = "name", defaultValue = "World") String name) {
//        return new Helloworld(counter.incrementAndGet(),
//                String.format(template, name));
//    }
}
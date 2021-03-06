package com.example.mtg.controller;

import com.example.mtg.model.Card;
import com.example.mtg.service.CardService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class APIController {

    @Autowired
    private CardService cardService;

    @RequestMapping("v0/card")
    public List<Card> card(@RequestParam(value="id", defaultValue="0") String id) {
        Long longId;
        try {
            longId = Long.parseLong(id);
        } catch (NumberFormatException e) {
            longId = 0L;
        }

        if (longId == 0L) {
            return cardService.ConstructRandomCard();
        } else {
            return cardService.ConstructCardById(longId);
//            return cardService.ConstructRandomCard();
        }


    }

//    @RequestMapping("v0/cards")
//    public List<Card> cards(@RequestParam(value="name", defaultValue="") String name,
//                            @RequestParam(value="set", defaultValue="") String set) {
//
//    }
}

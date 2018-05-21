package com.example.mtg.controller;

import com.example.mtg.dao.MultiValuesDAO;
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
    private MultiValuesDAO ND;
    @Autowired
    private CardService CS;

    @RequestMapping("v0/cards")
    public List<Card> cards(@RequestParam(value="name", defaultValue="") String name,
                            @RequestParam(value="set", defaultValue="") String set) {
        String constructed_set = "";
        Long longSet;
        try {
            longSet = Long.parseLong(set);
        } catch (NumberFormatException e) {
             longSet = 0L;
        }
        if (longSet != 0L) {
            constructed_set = "and `set` = " + Long.toString(longSet);
        }
        String constructed_name = "\"%" + name + "%\"";
        System.out.println(constructed_name);
        System.out.println(constructed_set);
        List<Card> response = CS.GetAllCards(constructed_name, constructed_set);
        return response;
    }

    @RequestMapping("v0/card")
    public List<Card> card(@RequestParam(value="id", defaultValue="0") String id) {
        Long longId;
        try {
            longId = Long.parseLong(id);
        } catch (NumberFormatException e) {
            longId = 0L;
        }

        if (longId == 0L) {
            return CS.ConstructRandomCard();
        } else {
            return CS.ConstructCardByID(longId);
        }

//        return response;
    }

}


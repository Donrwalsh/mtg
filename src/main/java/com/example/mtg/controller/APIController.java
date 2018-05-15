package com.example.mtg.controller;

import com.example.mtg.dao.CardDAO;
import com.example.mtg.model.Card;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class APIController {

    @Autowired
    private CardDAO CD;

    @RequestMapping("v0/card")
    public Card card() {
        Card result = CD.getACard((long)1);
        return result;
    }

//    @RequestMapping("v1/user")
//    public List<User> user(@RequestParam(value="id", defaultValue="0") String id) {
//        Long longId;
//        try {
//            longId = Long.parseLong(id);
//        } catch (NumberFormatException e) {
//            longId = 0L;
//        }
//        List<User> response = UD.getUserById(longId);
//        return response;
//    }
//
//    @RequestMapping("v1/question")
//    public List<Question> question(@RequestParam(value="id", defaultValue="0") String id) {
//        Long longId;
//        try {
//            longId = Long.parseLong(id);
//        } catch (NumberFormatException e) {
//            longId = 0L;
//        }
//        List<Question> response = QD.getQuestionById(longId);
//        return response;
//    }

}


package com.example.mtgapi.controller;

import com.example.mtgapi.dao.CardDAO;
import com.example.mtgapi.model.Card;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class APIController {

    @Autowired
    private CardDAO CD;

    @RequestMapping("v0/card")
    public Card card() {
        Card result = CD.getACard((long)5500);
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


package com.example.mtg.controller;



import com.example.mtg.dao.SetDAO;
import com.example.mtg.model.Card;
import com.example.mtg.persistence.model.Set;
import com.example.mtg.service.CardService;
import org.hibernate.SessionFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class APIController {

    @Autowired
    private SetDAO setDAO;
    @Autowired
    private CardService cardService;
    @Autowired
    SessionFactory sessionFactory;

    @RequestMapping("v0/cards")
    public List<Card> cards(@RequestParam(value="name", defaultValue="") String name,
                            @RequestParam(value="set", defaultValue="") String set) {
        Long longSet;
        try {
            longSet = Long.parseLong(set);
        } catch (NumberFormatException e) {
             longSet = 0L;
        }
        String constructed_name = "%" + name + "%";

        return cardService.GetAllCards(constructed_name, longSet);
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
            return cardService.ConstructRandomCard();
        } else {
            return cardService.ConstructCardByID(longId);
        }

    }

    @RequestMapping("v0/sets")
    public List<Set> sets() {
//        Session session;
//        try {
//            session = sessionFactory.getCurrentSession();
//        } catch (HibernateException e) {
//            session = sessionFactory.openSession();
//        }
////        Session session session= this.sessionFactory.getCurrentSession();
//        List<Set> sets = session.createQuery("FROM Set").getSets();
        return setDAO.getSets();
    }

    @RequestMapping("v0/set")
    public List<Set> set(@RequestParam(value="id", defaultValue="0") String id) {
        Long longId;
        try {
            longId = Long.parseLong(id);
        } catch (NumberFormatException e) {
            longId = 0L;
        }

        return setDAO.getASet(longId);
    }

}


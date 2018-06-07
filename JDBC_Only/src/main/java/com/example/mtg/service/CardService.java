package com.example.mtg.service;

import com.example.mtg.dao.CardDAO;
import com.example.mtg.model.Card;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CardService {

    @Autowired
    private CardDAO cardDAO;

    public List<Card> ConstructRandomCard() {
        List<Card> response = null;
        try {
            response = cardDAO.getRandomCard();
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

        //append multi-values
        return response;
    }
}

package com.example.mtg.service;

import com.example.mtg.dao.CardDAO;
import com.example.mtg.dao.NamesDAO;
import com.example.mtg.model.Card;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CardService {

    @Autowired
    private CardDAO CD;
    @Autowired
    private NamesDAO ND;

    public List<Card> ConstructCardByID(Long id) {

        List<Card> response = CD.getACard(id);
        for (Card card : response) {
            card.setNames(ND.GetNamesByID(card.getId()));
        }
        return response;
    }



}

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

    public List<Card> ConstructCardById(Long id) {
        List<Card> response = null;
        try {
            response = cardDAO.getACard(id);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        for (Card card : response) {
            AppendMultiValues(card);
        }
        return response;
    }

    public List<Card> ConstructRandomCard() {
        List<Card> response = null;
        try {
            response = cardDAO.getRandomCard();
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

        for (Card card : response) {
            AppendMultiValues(card);
        }
        return response;
    }

    private void AppendMultiValues(Card card) {
        try {
            card.setNames(cardDAO.getNamesById(card.getId()));
            card.setColors(cardDAO.getColorsById(card.getId()));
            card.setColorIdentity(cardDAO.getColorIdentityById(card.getId()));
            card.setSuperTypes(cardDAO.getSuperTypesById(card.getId()));
            card.setTypes(cardDAO.getTypesById(card.getId()));
            card.setSubTypes(cardDAO.getSubTypesById(card.getId()));
            card.setVariations(cardDAO.getVariationsById(card.getId()));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

    }


}

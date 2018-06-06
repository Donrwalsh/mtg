package com.example.mtg.service;

import com.example.mtg.dao.CardDAO;
import com.example.mtg.dao.MultiValuesDAO;
import com.example.mtg.model.Card;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CardService {

    @Autowired
    private CardDAO cardDAO;
    @Autowired
    private MultiValuesDAO multiValuesDAO;

    private void AppendMultivalues(Card card) {
        card.setNames(multiValuesDAO.GetNamesByID(card.getId()));
        card.setColors(multiValuesDAO.GetColorsByID(card.getId()));
        card.setColorIdentity(multiValuesDAO.GetColorIdentityByID(card.getId()));
        card.setSuperTypes(multiValuesDAO.GetSuperTypesByID(card.getId()));
        card.setTypes(multiValuesDAO.GetTypesByID(card.getId()));
        card.setSubTypes(multiValuesDAO.GetSubTypesByID(card.getId()));
        card.setVariations(multiValuesDAO.GetVariationsByID(card.getId()));
    }

    public List<Card> ConstructCardByID(Long id) {

        List<Card> response = cardDAO.getACard(id);
        for (Card card : response) {
            AppendMultivalues(card);
        }
        return response;
    }

    public List<Card> GetAllCards(String name, Long set) {
        System.out.println(name);
        System.out.println(set);

        List<Card> response = cardDAO.getCards(name, set);
        for (Card card : response) {
            AppendMultivalues(card);
        }
        return response;
    }

    public List<Card> ConstructRandomCard() {

        List<Card> response = cardDAO.getRandomCard();
        for (Card card : response) {
            AppendMultivalues(card);
        }
        return response;
    }
}

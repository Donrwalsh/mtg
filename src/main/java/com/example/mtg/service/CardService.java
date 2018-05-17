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
    private CardDAO CD;
    @Autowired
    private MultiValuesDAO MVD;

    public List<Card> ConstructCardByID(Long id) {

        List<Card> response = CD.getACard(id);
        for (Card card : response) {
            card.setNames(MVD.GetNamesByID(card.getId()));
            card.setColors(MVD.GetColorsByID(card.getId()));
            card.setColorIdentity(MVD.GetColorIdentityByID(card.getId()));
            card.setSuperTypes(MVD.GetSuperTypesByID(card.getId()));
            card.setTypes(MVD.GetTypesByID(card.getId()));
            card.setSubTypes(MVD.GetSubTypesByID(card.getId()));
            card.setVariations(MVD.GetVariationsByID(card.getId()));
        }
        return response;
    }



}

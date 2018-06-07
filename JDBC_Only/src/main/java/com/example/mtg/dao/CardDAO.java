package com.example.mtg.dao;

import com.example.mtg.model.Card;

import java.util.List;

public interface CardDAO {
    List<Card> getACard(Long id) throws Exception;
//    List<Card> getCards(String name, Long set);
    List<Card> getRandomCard() throws Exception;

    List<String> getNamesById(Long id) throws Exception;
    List<String> getColorsById(Long id) throws Exception;
    List<String> getColorIdentityById(Long id) throws Exception;
    List<String> getSuperTypesById(Long id) throws Exception;
    List<String> getTypesById(Long id) throws Exception;
    List<String> getSubTypesById(Long id) throws Exception;
    List<Integer> getVariationsById(Long id) throws Exception;
}

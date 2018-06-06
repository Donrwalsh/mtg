package com.example.mtg.dao;

import com.example.mtg.model.Card;

import java.util.List;

public interface CardDAO {
    List<Card> getACard(Long id);
    List<Card> getCards(String name, Long set);
    List<Card> getRandomCard();
}

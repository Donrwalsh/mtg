package com.example.mtg.dao;

import com.example.mtg.model.Card;
import org.springframework.stereotype.Component;

import java.util.List;

public interface CardDAO {
    List<Card> getACard(Long id);
    List<Card> getCards(String name);
    List<Card> getRandomCard();
}

package com.example.mtg.dao;

import com.example.mtg.model.Card;

import java.util.List;

public interface CardDAO {
    List<Card> getACard(Long id);

}

package com.example.mtg.dao;

import com.example.mtg.model.Card;
import com.example.mtg.service.DatabaseService;
import org.springframework.beans.factory.annotation.Autowired;

import javax.inject.Named;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

@Named
public class CardDAOImpl implements CardDAO {

    @Autowired
    private DatabaseService databaseService;

    @Override
    public List<Card> getRandomCard() throws Exception {
        ResultSet response = databaseService.performQuery("SELECT * FROM `cards` ORDER BY RAND() LIMIT 1");
        List<Card> result = new ArrayList<>();
        while (response.next()) {
            Card responseCard = new Card(
                    response.getLong("id"),
                    response.getString("name"),
                    response.getString("manaCost"),
                    response.getInt("cmc"),
                    response.getInt("set"),
                    response.getString("rarity"),
                    response.getString("text"),
                    response.getString("flavor"),
                    response.getString("artist"),
                    response.getString("number"),
                    response.getString("power"),
                    response.getString("toughness"),
                    response.getString("loyalty"),
                    response.getInt("multiverseid"),
                    response.getString("watermark"),
                    response.getString("border"),
                    response.getString("layout"),
                    response.getBoolean("timeshifted"),
                    response.getBoolean("reserved"),
                    response.getBoolean("starter")
            );
            result.add(responseCard);
        }
        return result;
    }
}

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

    private Card responseToCard(ResultSet response) throws Exception {
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
        return responseCard;
    }

    @Override
    public List<Card> getACard(Long id) throws Exception {
        ResultSet response = databaseService.performQuery("SELECT * FROM `cards` WHERE id = " + id.toString());
        List<Card> result = new ArrayList<>();
        while (response.next()) {
            result.add(responseToCard(response));
        }
        return result;
    }

    @Override
    public List<Card> getRandomCard() throws Exception {
        ResultSet response = databaseService.performQuery("SELECT * FROM `cards` ORDER BY RAND() LIMIT 1");
        List<Card> result = new ArrayList<>();
        while (response.next()) {
            result.add(responseToCard(response));
        }
        return result;
    }

    @Override
    public List<String> getNamesById(Long id) throws Exception {
        ResultSet response = databaseService.performQuery("SELECT name FROM `names` WHERE card_id = " + id.toString());
        List<String> result = new ArrayList<>();
        while (response.next()) {
            result.add(response.getString("name"));
        }
        return result;
    }

    @Override
    public List<String> getColorsById(Long id) throws Exception {
        ResultSet response = databaseService.performQuery("SELECT color FROM `colors` WHERE card_id = " + id.toString());
        List<String> result = new ArrayList<>();
        while (response.next()) {
            result.add(response.getString("color"));
        }
        return result;
    }

    @Override
    public List<String> getColorIdentityById(Long id) throws Exception {
        ResultSet response = databaseService.performQuery("SELECT color FROM `color_identities` WHERE card_id = " + id.toString());
        List<String> result = new ArrayList<>();
        while (response.next()) {
            result.add(response.getString("color"));
        }
        return result;
    }

    @Override
    public List<String> getSuperTypesById(Long id) throws Exception {
        ResultSet response = databaseService.performQuery("SELECT supertype FROM `supertypes` WHERE card_id = " + id.toString());
        List<String> result = new ArrayList<>();
        while (response.next()) {
            result.add(response.getString("supertype"));
        }
        return result;
    }

    @Override
    public List<String> getTypesById(Long id) throws Exception {
        ResultSet response = databaseService.performQuery("SELECT type FROM `types` WHERE card_id = " + id.toString());
        List<String> result = new ArrayList<>();
        while (response.next()) {
            result.add(response.getString("type"));
        }
        return result;
    }

    @Override
    public List<String> getSubTypesById(Long id) throws Exception {
        ResultSet response = databaseService.performQuery("SELECT subtype FROM `subtypes` WHERE card_id = " + id.toString());
        List<String> result = new ArrayList<>();
        while (response.next()) {
            result.add(response.getString("subtype"));
        }
        return result;
    }

    @Override
    public List<Integer> getVariationsById(Long id) throws Exception {
        ResultSet response = databaseService.performQuery("SELECT variant_id FROM `variations` WHERE card_id = " + id.toString());
        List<Integer> result = new ArrayList<>();
        while (response.next()) {
            result.add(response.getInt("variant_id"));
        }
        return result;
    }
}

package com.example.mtgapi.dao;

import com.example.mtgapi.model.Card;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;

import javax.inject.Named;
import java.sql.ResultSet;
import java.sql.SQLException;

@Named
public class CardDAOImpl implements CardDAO {

    private JdbcTemplate jdbcTemplate;

    @Autowired
    public CardDAOImpl(JdbcTemplate jdbcTemplate) { this.jdbcTemplate = jdbcTemplate; }

    private static final String GET_CARD_BY_ID =
            "SELECT id, name FROM `cards` WHERE ID = ?";

    @Override
    public Card getACard(Long id) {
        return jdbcTemplate.queryForObject(GET_CARD_BY_ID, new CardMapper(), id.toString());
    }

    private static final class CardMapper implements RowMapper<Card> {

        public Card mapRow(ResultSet rs, int rowNum) throws SQLException {

            Card card = new Card(
                    rs.getLong("id"),
                    rs.getString("name")
            );

            return card;
        }
    }
}

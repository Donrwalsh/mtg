package com.example.mtg.dao;

import com.example.mtg.model.Card;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;

import javax.inject.Named;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;

@Named
public class CardDAOImpl implements CardDAO {

    private JdbcTemplate jdbcTemplate;

    @Autowired
    public CardDAOImpl(JdbcTemplate jdbcTemplate) { this.jdbcTemplate = jdbcTemplate; }

    private static final String GET_CARDS_BY_NAME =
            "SELECT * FROM `cards` WHERE name LIKE ? LIMIT 10;";

    private static final String GET_CARD_BY_ID =
            "SELECT * FROM `cards` WHERE ID = ?";

    @Override
    public List<Card> getACard(Long id) {
        return jdbcTemplate.query(GET_CARD_BY_ID, new CardMapper(), id.toString());
    }

    @Override
    public List<Card> getCards(String name) { return jdbcTemplate.query(GET_CARDS_BY_NAME, new CardMapper(), name); }

    private static final class CardMapper implements RowMapper<Card> {

        public Card mapRow(ResultSet rs, int rowNum) throws SQLException {


            Card card = new Card(
                    rs.getLong("id"),
                    rs.getString("name"),
                    rs.getString("manaCost"),
                    rs.getInt("cmc"),
                    rs.getInt("set"),
                    rs.getString("rarity"),
                    rs.getString("text"),
                    rs.getString("flavor"),
                    rs.getString("artist"),
                    rs.getString("number"),
                    rs.getString("power"),
                    rs.getString("toughness"),
                    rs.getString("loyalty"),
                    rs.getInt("multiverseid"),
                    rs.getString("watermark"),
                    rs.getString("border"),
                    rs.getString("layout"),
                    rs.getBoolean("timeshifted"),
                    rs.getBoolean("reserved"),
                    rs.getBoolean("starter")
            );

            return card;
        }
    }
}

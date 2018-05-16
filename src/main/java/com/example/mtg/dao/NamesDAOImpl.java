package com.example.mtg.dao;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.ResultSetExtractor;
import org.springframework.jdbc.core.RowMapper;

import javax.inject.Named;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

@Named
public class NamesDAOImpl implements NamesDAO {

    private JdbcTemplate jdbcTemplate;

    @Autowired
    public NamesDAOImpl(JdbcTemplate jdbcTemplate) { this.jdbcTemplate = jdbcTemplate; }

    private static final String GET_NAMES_BY_ID =
            "SELECT name FROM `names` WHERE card = ?";

    @Override
    public List<String> GetNamesByID(Long id) {
        return jdbcTemplate.queryForList(GET_NAMES_BY_ID,String.class,id.toString());
    }
}

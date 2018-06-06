package com.example.mtg.dao;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;

import javax.inject.Named;
import java.util.List;

@Named
public class MultiValuesDAOImpl implements MultiValuesDAO {

    private JdbcTemplate jdbcTemplate;

    @Autowired
    public MultiValuesDAOImpl(JdbcTemplate jdbcTemplate) { this.jdbcTemplate = jdbcTemplate; }

    private static final String GET_NAMES_BY_ID =
            "SELECT name FROM `names` WHERE card_id = ?";

    private static final String GET_COLORS_BY_ID =
            "SELECT color FROM `colors` WHERE card_id = ?";

    private static final String GET_COLOR_IDENTITIES_BY_ID =
            "SELECT color FROM `color_identities` WHERE card_id = ?";

    private static final String GET_SUPERTYPES_BY_ID =
            "SELECT supertype FROM `supertypes` WHERE card_id = ?";

    private static final String GET_TYPES_BY_ID =
            "SELECT type FROM `types` WHERE card_id = ?";

    private static final String GET_SUBTYPES_BY_ID =
            "SELECT subtype FROM `subtypes` WHERE card_id = ?";

    private static final String GET_VARIATIONS_BY_ID =
            "SELECT variant_id FROM `variations` WHERE card_id = ?";

    @Override
    public List<String> GetNamesByID(Long id) {
        return jdbcTemplate.queryForList( GET_NAMES_BY_ID, String.class, id.toString() );
    }

    @Override
    public List<String> GetColorsByID(Long id) {
        return jdbcTemplate.queryForList( GET_COLORS_BY_ID, String.class, id.toString() );
    }

    @Override
    public List<String> GetColorIdentityByID(Long id) {
        return jdbcTemplate.queryForList( GET_COLOR_IDENTITIES_BY_ID, String.class, id.toString() );
    }

    @Override
    public List<String> GetSuperTypesByID(Long id) {
        return jdbcTemplate.queryForList( GET_SUPERTYPES_BY_ID, String.class, id.toString() );
    }

    @Override
    public List<String> GetTypesByID(Long id) {
        return jdbcTemplate.queryForList( GET_TYPES_BY_ID, String.class, id.toString() );
    }

    @Override
    public List<String> GetSubTypesByID(Long id) {
        return jdbcTemplate.queryForList( GET_SUBTYPES_BY_ID, String.class, id.toString() );
    }

    @Override
    public List<Integer> GetVariationsByID(Long id) {
        return jdbcTemplate.queryForList( GET_VARIATIONS_BY_ID, Integer.class, id.toString() );
    }
}

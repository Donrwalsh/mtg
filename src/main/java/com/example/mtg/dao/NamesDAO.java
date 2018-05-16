package com.example.mtg.dao;

import java.util.List;

public interface NamesDAO {
    List<String> GetNamesByID(Long id);
}

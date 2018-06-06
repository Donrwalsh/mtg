package com.example.mtg.dao;

import java.util.List;

import com.example.mtg.persistence.model.Set;

public interface SetDAO {

    List<Set> getSets();
    List<Set> getASet(Long id);


}

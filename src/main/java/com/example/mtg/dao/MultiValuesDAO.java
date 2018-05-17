package com.example.mtg.dao;

import java.util.List;

public interface MultiValuesDAO {
    List<String> GetNamesByID(Long id);
    List<String> GetColorsByID(Long id);
    List<String> GetColorIdentityByID(Long id);
    List<String> GetSuperTypesByID(Long id);
    List<String> GetTypesByID(Long id);
    List<String> GetSubTypesByID(Long id);
    List<Integer> GetVariationsByID(Long id);
}

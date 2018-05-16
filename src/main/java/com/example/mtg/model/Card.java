package com.example.mtg.model;

import java.util.List;

public class Card {

    // Properties ----------------------------------------------------------------------------------------------------
    private Long id;
    private String name;
    private List<String> names;

    //Constructors ----------------------------------------------------------------------------------------------------
    public Card(Long id, String name) {
        this.id = id;
        this.name = name;
    }

    //Getters ---------------------------------------------------------------------------------------------------------
    public Long getId() { return id; }
    public String getName() { return name; }
    public List<String> getNames() { return names; }

    //Setters --------------------------------------------------------------------------------------------------------
    public void setNames(List<String> names) {
        this.names = names;
    }
}

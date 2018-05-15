package com.example.mtgapi.model;

public class Card {

    // Properties ----------------------------------------------------------------------------------------------------
    private Long id;
    private String name;

    //Constructors ----------------------------------------------------------------------------------------------------
    public Card(Long id, String name) {
        this.id = id;
        this.name = name;
    }

    //Getters ---------------------------------------------------------------------------------------------------------
    public Long getId() { return id; }
    public String getName() { return name; }

    //Setters --------------------------------------------------------------------------------------------------------

}

package com.example.mtg.model;

import java.util.List;

public class Card {

    // Properties ----------------------------------------------------------------------------------------------------
    private Long id;
    private String name;
    private List<String> names;
    private List<String> colors;
    private List<String> colorIdentity;
    private String manaCost;
    private int cmc;
    private int set;
    private String rarity;
    private String text;
    private String flavor;
    private List<String> supertypes;
    private List<String> types;
    private List<String> subtypes;
    private List<Integer> variations;
    private String artist;
    private String number;
    private String power;
    private String toughness;
    private String loyalty;
    private int multiverseid;
    private String watermark;
    private String border;
    private String layout;
    private boolean timeshifted;
    private boolean reserved;
    private boolean starter;

    //Constructors ----------------------------------------------------------------------------------------------------
    public Card(Long id, String name, String manaCost, int cmc, int set, String rarity, String text, String flavor,
                String artist, String number, String power, String toughness, String loyalty, int multiverseid,
                String watermark, String border, String layout, boolean timeshifted, boolean reserved, boolean starter) {
        this.id = id;
        this.name = name;
        this.manaCost = manaCost;
        this.cmc = cmc;
        this.set = set;
        this.rarity = rarity;
        this.text = text;
        this.flavor = flavor;
        this.artist = artist;
        this.number = number;
        this.power = power;
        this.toughness = toughness;
        this.loyalty = loyalty;
        this.multiverseid = multiverseid;
        this.watermark = watermark;
        this.border = border;
        this.layout = layout;
        this.timeshifted = timeshifted;
        this.reserved = reserved;
        this.starter = starter;
    }

    //Getters ---------------------------------------------------------------------------------------------------------
    public Long getId() { return id; }
    public String getName() { return name; }
    public List<String> getNames() { return names; }
    public List<String> getColors() { return colors; }
    public List<String> getColorIdentity() { return colorIdentity; }
    public String getManaCost() { return manaCost; }
    public int getCmc() { return cmc; }
    public int getSet() { return set; }
    public String getRarity() { return rarity; }
    public String getText() { return text; }
    public String getFlavor() { return flavor; }
    public List<String> getSupertypes() { return supertypes; }
    public List<String> getTypes() { return types; }
    public List<String> getSubtypes() { return subtypes; }
    public List<Integer> getVariations() { return variations; }
    public String getArtist() { return artist; }
    public String getNumber() { return number; }
    public String getPower() { return power; }
    public String getToughness() { return toughness; }
    public String getloyalty() { return loyalty; }
    public int getMultiverseid() { return multiverseid; }
    public String getWatermark() { return watermark; }
    public String getBorder() { return border; }
    public String getLayout() { return layout; }
    public boolean getTimeshifted() { return timeshifted; }
    public boolean getReserved() { return reserved; }
    public boolean getStarter() { return starter; }

    //Setters --------------------------------------------------------------------------------------------------------
    public void setNames(List<String> names) {
        this.names = names;
    }
    public void setColors(List<String> colors) { this.colors = colors; }
    public void setColorIdentity(List<String> colorIdentities) { this.colorIdentity = colorIdentities; }
    public void setSuperTypes(List<String> supertypes) { this.supertypes = supertypes; }
    public void setTypes(List<String> types) { this.types = types; }
    public void setSubTypes(List<String> subtypes) { this.subtypes = subtypes; }
    public void setVariations(List<Integer> variations) { this.variations = variations; }
}

package com.example.mtg.model;

public class Set {

    private Long id;
    private String code;
    private String name;
    private String type;
    private String release_date;
    private String block;
    private String block_code;
    private String parent_set_code;
    private Long card_count;
    private String border;

    public Set() {
    }

    public Set(Long id, String code, String name, String type, String release_date, String block, String block_code,
               String parent_set_code, Long card_count, String border) {
        this.id = id;
        this.code = code;
        this.name = name;
        this.type = type;
        this.release_date = release_date;
        this.block = block;
        this.block_code = block_code;
        this.parent_set_code = parent_set_code;
        this.card_count = card_count;
        this.border = border;
    }

    public String getRelease_date() {
        return release_date;
    }

    public void setRelease_date(String release_date) {
        this.release_date = release_date;
    }

    public String getBorder() {
        return border;
    }

    public void setBorder(String border) {
        this.border = border;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getBlock() {
        return block;
    }

    public void setBlock(String block) {
        this.block = block;
    }

    public String getBlock_code() {
        return block_code;
    }

    public void setBlock_code(String block_code) {
        this.block_code = block_code;
    }

    public String getParent_set_code() {
        return parent_set_code;
    }

    public void setParent_set_code(String parent_set_code) {
        this.parent_set_code = parent_set_code;
    }

    public Long getCard_count() {
        return card_count;
    }

    public void setCard_count(Long card_count) {
        this.card_count = card_count;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
}

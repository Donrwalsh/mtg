package com.example.mtg.persistence.model;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "sets")
public class Set {


    private Long id;
    private String name;
    private String code;
    private String releaseDate;
    private String border;
    private String type;
    private boolean onlineOnly;

    public Set() {
    }

    public Set(Long id, String name, String code, String releaseDate, String border, String type, boolean onlineOnly) {
        this.id = id;
        this.name = name;
        this.code = code;
        this.releaseDate = releaseDate;
        this.border = border;
        this.type = type;
        this.onlineOnly = onlineOnly;
    }

    public String getReleaseDate() {
        return releaseDate;
    }

    public void setReleaseDate(String releaseDate) {
        this.releaseDate = releaseDate;
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

    public boolean isOnlineOnly() {
        return onlineOnly;
    }

    public void setOnlineOnly(boolean onlineOnly) {
        this.onlineOnly = onlineOnly;
    }

    @Id
    @Column(name = "id")
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

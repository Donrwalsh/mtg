package com.example.mtg;

public class Helloworld {

    private final long id;
    private final String content;

    public Helloworld(long id, String content) {
        this.id = id;
        this.content = content;
    }

    public long getId() {
        return id;
    }

    public String getContent() {
        return content;
    }
}

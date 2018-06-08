package com.example.mtg.service;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import java.sql.*;

@Service
public class DatabaseService {

    @Value("${datasource.url'}")
    private String url;

    @Value("${datasource.username'}")
    private String username;

    @Value("${datasource.url'}")
    private String driverClassName;

    @Value("${datasource.password}")
    private String password;

    public Connection getConnection() throws Exception {
        Class.forName(driverClassName);
        Connection con = DriverManager.getConnection(
                url,
                username,
                password);
        return con;
    }

    public ResultSet performQuery(String query) {
        Connection con = null;
        Statement stmt = null;
        ResultSet rs = null;
        try {
            con = getConnection();
            stmt = con.createStatement();
            rs = stmt.executeQuery(query);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        return rs;
    }

}

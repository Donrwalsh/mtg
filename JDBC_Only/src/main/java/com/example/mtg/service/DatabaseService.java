package com.example.mtg.service;

import org.springframework.stereotype.Service;

import java.sql.*;

@Service
public class DatabaseService {

    public Connection getConnection() throws Exception {
        Class.forName("com.mysql.cj.jdbc.Driver");
        Connection con = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/mtg?serverTimezone=UTC&useLegacyDatetimeCode=true&useSSL=false",
                "root",
                "2Potato4Me!");
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

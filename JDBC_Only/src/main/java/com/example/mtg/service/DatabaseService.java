package com.example.mtg.service;

import org.springframework.stereotype.Service;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

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

//    public DatabaseService() {
//        try {
//            Class.forName("com.mysql.cj.jdbc.Driver");
//        } catch (Exception e) {
//            System.out.println(e.getMessage());
//        }
//
//        try {
//            Connection con = DriverManager.getConnection(
//                "jdbc:mysql://localhost:3306/mtg?serverTimezone=UTC&useLegacyDatetimeCode=true&useSSL=false",
//                "root",
//                "2Potato4Me!");
//        } catch (java.sql.SQLException e) {
//            System.out.println(e.getMessage());
//        }
//    }

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
        System.out.println(rs);
        return rs;
    }

}

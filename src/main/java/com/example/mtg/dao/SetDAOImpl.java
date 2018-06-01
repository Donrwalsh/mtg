package com.example.mtg.dao;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;

import com.example.mtg.persistence.model.Set;
import org.springframework.transaction.annotation.Transactional;

import javax.inject.Named;
import java.util.List;

@Named
public class SetDAOImpl implements SetDAO {

    private SessionFactory sessionFactory;

    public void setSessionFactory(SessionFactory sessionFactory) {
        this.sessionFactory = sessionFactory;
    }

    @SuppressWarnings("unchecked")
    @Override
    public List<Set> list() {
        Session session = this.sessionFactory.openSession();
        List<Set> setList = session.createQuery("FROM Set").list();
        return setList;
    }
}

package com.example.mtg.dao;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;

import com.example.mtg.persistence.model.Set;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.transaction.annotation.Transactional;

import javax.inject.Named;
import java.util.List;
import java.util.Random;

@Named
public class SetDAOImpl implements SetDAO {

    @Autowired
    private SessionFactory sessionFactory;

    public void setSessionFactory(SessionFactory sessionFactory) {
        this.sessionFactory = sessionFactory;
    }

    @SuppressWarnings("unchecked")
    @Override
    public List<Set> getSets() {
        Session session = this.sessionFactory.openSession();
        List<Set> setList = session.createQuery("FROM Set").list();
        return setList;
    }

    public List<Set> getASet(Long id) {
        Session session = this.sessionFactory.openSession();
        if (id == 0L) {
            Random rand = new Random();
            int max = ((Number)session.createQuery("select count(*) from Set").uniqueResult()).intValue();
            int n = rand.nextInt(max) + 1;
            System.out.println(n);
            id = Long.valueOf(n);
        }
        return session.createQuery("FROM Set WHERE id = " + id).list();
    }
}

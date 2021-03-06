package com.se325.common;

import java.io.IOException;
import java.net.MalformedURLException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

import javax.xml.parsers.ParserConfigurationException;

import org.hibernate.SQLQuery;
import org.hibernate.Session;
import org.springframework.dao.DataAccessException;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.GrantedAuthorityImpl;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.xml.sax.SAXException;

import com.se325.controller.AppController;
import com.se325.persistence.HibernateUtil;


//user authenticator for logging users in using our database

@Service
@Transactional(readOnly = true)
public class CustomUserDetailsService implements UserDetailsService {

	private String steamId64;
	private String steamId;
	private String profileName ="";
	
	@Override
	public UserDetails loadUserByUsername(String openIdReturnUrl)
			throws UsernameNotFoundException, DataAccessException {

		steamId64 = AppController.get64BitSteamId(openIdReturnUrl);//gets the 64 bit user name
		steamId = AppController.convertSteamID64ToSteamID(steamId64);//get steam id
		
		try {
			profileName = AppController.getSteamUsername(steamId64);//get 64bit id
		} catch (MalformedURLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (ParserConfigurationException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (SAXException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}//gets your display name for steam

		com.se325.common.User user = null;//this has to be explicit otherwise it conflicts with org.springframework.security.core.userdetails.User
		
		List<?> results = checkUserExists(openIdReturnUrl);//checking if user already exists in database
		
		if ( !results.isEmpty() ) {//if user exists in database
			
			for ( Iterator<?> iterator = results.iterator(); iterator.hasNext(); ) {
				user = (com.se325.common.User) iterator.next();//assigning user vaiable to the found user 
			}

		}else{

			user = createNewUser(openIdReturnUrl);//creating new user

		}
		
		
		//this following code is a requried parameter for creating a org.springframework.security.core.userdetails.User
		List<GrantedAuthority> grantedAuthorities = new ArrayList<GrantedAuthority>();
		grantedAuthorities.add( new GrantedAuthorityImpl( "10" ) );//every authenticated user has a authority of 10 

		return new org.springframework.security.core.userdetails.User(
				user.getOpenIdReturnUrl(),
				user.getPassword(),
				true,
				true,
				true,
				true,
				grantedAuthorities
				);
	}
	
	private List<?> checkUserExists(String openIdReturnUrl){
		
		//querying database for user by the url returned by Valve when logging in via OpenId
		Session session = HibernateUtil.getSessionFactory().openSession();
		session.beginTransaction();

		String queryString =
				"SELECT * FROM user WHERE openId_return_url = :openId_return_url";

		SQLQuery query = session.createSQLQuery(queryString);
		query.addEntity(User.class);
		query.setParameter("openId_return_url", openIdReturnUrl);
		List<?> results = query.list();
		session.getTransaction().commit();
		
		return results;
		
	}
	
	
	
	private com.se325.common.User createNewUser(String openIdReturnUrl){
		
		//creating a new user
		Session session = HibernateUtil.getSessionFactory().openSession();
		session.beginTransaction();
		com.se325.common.User user = new User();
		user.setSteamId(steamId);
		user.setSteamId64(Long.parseLong(steamId64));
		user.setSteamProfileName(profileName);
		user.setRole(10);
		user.setSteamName(""); //TODO fill this in
		user.setPassword("");
		user.setOpenIdReturnUrl(openIdReturnUrl);
		session.save(user);
		session.getTransaction().commit();
		
		return user;
		
	}

}

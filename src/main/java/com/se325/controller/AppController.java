package com.se325.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;



@Controller
//@RequestMapping("/main")
public class AppController{
	
	protected static String username;

	@RequestMapping(value = "/home", method = RequestMethod.GET)
	public String printWelcome(ModelMap model) {
		model.addAttribute("message", "Hello! This is home page please log in to proceed.");
		return "home";
	}
	
	
	@RequestMapping(value = "/UploadReplay", method = RequestMethod.POST)
	public String upload(ModelMap model) {
//		model.addAttribute("message", "Hello! This is Spring MVC Web Controller.");
		return "uploadFile";
	}
	
	@RequestMapping(value = "/common", method = RequestMethod.GET)
	public String printLoggedIn(ModelMap model) {
		Authentication auth = SecurityContextHolder.getContext().getAuthentication();
		username = this.get64BitId(auth.getName());
		model.addAttribute("message", "Hello! "+username+" You Have Logged In choose file to upload");
		return "loggedIn_home";
	}
	
	@RequestMapping(value = "/denied", method = RequestMethod.GET)
 	public String getDeniedPage() {
		return "denied";
	}
	
	
	private String get64BitId(String claimedId){		
		return claimedId.substring(claimedId.indexOf("/id/")+4);
	}
}

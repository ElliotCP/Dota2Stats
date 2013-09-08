package com.se325.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;


@Controller
//@RequestMapping("/main")
public class AppController{

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
		model.addAttribute("message", "Hello! You Have Logged In choose file to upload");
		return "loggedIn_home";
	}
	
	@RequestMapping(value = "/denied", method = RequestMethod.GET)
 	public String getDeniedPage() {
		return "denied";
	}
}

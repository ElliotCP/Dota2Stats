package com.se325.controller;

import javax.servlet.http.HttpServletRequest;

import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@Controller
public class LoginController {
	
	@RequestMapping(value = "/", method = RequestMethod.GET)
	public String displayHomepage(ModelMap model) {
		return "index";
	}
	
	@RequestMapping(value = "/logout", method = RequestMethod.GET)
	public String logout(HttpServletRequest request, ModelMap model) {
		//invalidates current users session when user presses logout button
		request.getSession(false).invalidate();
		return "index";
	}
	
	@RequestMapping(value = "/denied", method = RequestMethod.GET)
	public String getDeniedPage(ModelMap model) {
		return "index";
	}
	
	@RequestMapping(value = "/about", method = RequestMethod.GET)
	public String getAboutPage(ModelMap model) {
		return "about";
	}
}

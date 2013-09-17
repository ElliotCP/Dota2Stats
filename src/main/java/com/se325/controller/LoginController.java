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
		model.addAttribute("message", "Hello! This is home page please log in to proceed.");
		return "index";
	}
	
	@RequestMapping(value = "/logout", method = RequestMethod.GET)
	public String logout(HttpServletRequest request, ModelMap model) {
		request.getSession(false).invalidate();
		model.addAttribute("message", "You have seccessfully logged out!");
		return "index";
	}
	
	@RequestMapping(value = "/denied", method = RequestMethod.GET)
	public String getDeniedPage(ModelMap model) {
		model.addAttribute("message", "Hello! This i42435435 to proceed.");
		return "index";
	}
}

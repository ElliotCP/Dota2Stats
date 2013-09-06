package com.se325.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;


import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.mvc.AbstractController;

@Controller
public class AppController{

	@RequestMapping(value = "/home", method = RequestMethod.GET)
	public String printWelcome(ModelMap model) {
		model.addAttribute("message", "Hello! This is Spring MVC Web Controller.");
		return "output";
	}
	
	
	@RequestMapping(value = "/UploadReplay", method = RequestMethod.POST)
	public String upload(ModelMap model) {
//		model.addAttribute("message", "Hello! This is Spring MVC Web Controller.");
		return "UploadFile";
	}
}

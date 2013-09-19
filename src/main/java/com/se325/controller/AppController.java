package com.se325.controller;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

import javax.servlet.http.HttpServletRequest;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;

import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.w3c.dom.Document;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

@Controller
@RequestMapping("/user")
public class AppController{

	private static String steamId64;
	private static String profileName;
	private static String steamId;

	@RequestMapping(value = "/home", method = {RequestMethod.GET, RequestMethod.POST})
	public String displayLoggedInHomepage(@RequestParam(value = "upload", required = false) boolean upload,
			ModelMap model, HttpServletRequest request) throws ParserConfigurationException, MalformedURLException, SAXException, IOException{

		Authentication auth = SecurityContextHolder.getContext().getAuthentication();

		steamId64 = AppController.get64BitSteamId(auth.getName());//gets the 64 bit user name
		steamId = AppController.convertSteamID64ToSteamID(steamId64);
		profileName = AppController.getSteamUsername(steamId64);//gets your display name for steam

		request.setAttribute("username", profileName);//this is so that jsp pages can use this variable

		return "user_index";
	}

	@RequestMapping(value = "/stats", method = RequestMethod.GET)
	public String getStats(@RequestParam(value = "replayId", required = true) String replayId,  HttpServletRequest request, ModelMap model) throws IOException{

		//comment out following to test-----
		URL obj = new URL("http://49.50.241.171:5000/?steamid="+steamId64+"&matchid="+replayId);//sending request to private server
		HttpURLConnection con = (HttpURLConnection) obj.openConnection();

		con.setRequestMethod("GET");

		BufferedReader in = new BufferedReader(
				new InputStreamReader(con.getInputStream()));
		String inputLine;
		StringBuffer response = new StringBuffer();

		while ((inputLine = in.readLine()) != null) {
			response.append(inputLine);
		}
		in.close();
		
		//--------
		
//StringBuffer response =  new StringBuffer();
//response.append("ok");

		
		if(response.toString().toLowerCase().equals("ok")){
			request.setAttribute("steamId64", steamId64);
			request.setAttribute("replayId", replayId);
			request.setAttribute("profileName", profileName);
			return "replay_graphs";
		}else{
			return "user_index";
		}
	}

	public static String get64BitSteamId(String claimedId){		
		//getting only the 64bit number from the returned claimed ID from steam
		//claimedId is in the format: http://steamcommunity.com/openid/id/<steamid>
		return claimedId.substring(claimedId.indexOf("/id/")+4);
	}

	public static String getSteamUsername(String steamId64) throws ParserConfigurationException, MalformedURLException, SAXException, IOException{
		//getting xml of your steam profile which contains display name
		DocumentBuilderFactory fac = DocumentBuilderFactory.newInstance();
		DocumentBuilder builder = fac.newDocumentBuilder();
		Document document = builder.parse(new URL("http://steamcommunity.com/profiles/" + steamId64 + "/?xml=1").openStream());

		//extracting the "<steamID>" tag which contains display name
		NodeList rootElement = document.getElementsByTagName("steamID");

		return rootElement.item(0).getTextContent();
	}

	public static String convertSteamID64ToSteamID(String steamId64) {
		// from https://developer.valvesoftware.com/wiki/SteamID
		Long steamID64 = Long.parseLong(steamId64); //convert steamId64 to long for use in calculations
		Long steamY = steamID64 - 76561197960265728L; //76561197960265728 is 110000100000000 in hex
		int steamX = 0;
		if(steamY % 2 == 1) {
			steamX = 1;
		}
		steamY = (steamY - steamX) / 2;
		return "STEAM_0:" + steamX + ":" + steamY; //formatting
	}
}

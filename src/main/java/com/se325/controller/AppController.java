package com.se325.controller;

import java.io.File;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

import javax.persistence.EntityManager;
import javax.persistence.Query;
import javax.servlet.http.HttpServletRequest;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;

import org.apache.commons.fileupload.FileItem;
import org.apache.commons.fileupload.disk.DiskFileItemFactory;
import org.apache.commons.fileupload.servlet.ServletFileUpload;
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
import org.hibernate.Criteria;
import org.hibernate.SQLQuery;
import org.hibernate.Session;

import com.se325.common.User;
import com.se325.common.Replay;
import com.se325.persistence.HibernateUtil;

@Controller
@RequestMapping("/user")
public class AppController{

	private static String steamId64;
	private static String profileName;
	private static String steamId;
	
	private final List<String> genImageNames = Arrays.asList(
			"playerRunePickupsGraph",
			"playerLevelGraph",
			"playerKillsGraph",
			"playerItemProgressionGraph",
			"playerGPMGraph",
			"playerGoldGraph",
			"playerDeathsGraph",
			
			"playerDamageDealtGraph",
			"playerAssistsGraph"			
		);//"playerDamageDealtTo",
	
	private static HashMap<String, String> uploadedFileList = new HashMap<String, String>();

	@RequestMapping(value = "/home", method = {RequestMethod.GET, RequestMethod.POST})
	public String displayLoggedInHomepage(@RequestParam(value = "upload", required = false) boolean upload,
			ModelMap model, HttpServletRequest request) throws ParserConfigurationException, MalformedURLException, SAXException, IOException{

		Authentication auth = SecurityContextHolder.getContext().getAuthentication();

		steamId64 = this.get64BitSteamId(auth.getName());//gets the 64 bit user name
		steamId = this.convertSteamID64ToSteamID(steamId64);
		profileName = this.getSteamUsername(steamId64);//gets your display name for steam

		request.setAttribute("username", profileName);

		if(upload){//request parameter upload is set i.e. url is .../home?upload=true , then upload file
			model.addAttribute("message", this.uploadFile(request));//method returns a string of the file uploaded
		}else{
			model.addAttribute("message", "Hello! " + profileName + " You Have Logged In choose file to upload");
		}
		
		getUploadedFiles();//get uploaded files
		request.setAttribute("uploadedFileList", uploadedFileList);
		
		Session session = HibernateUtil.getSessionFactory().openSession();
		session.beginTransaction();
		User user = new User();
		user.setSteamId(steamId);
		user.setSteamId64(Long.parseLong(steamId64));
		user.setSteamProfileName(profileName);
		user.setRank(10);
//		user.setSteamName("xiii_dragon");
		user.setSteamName(""); //TODO fill this in
		session.save(user);
		session.getTransaction().commit();
		
		return "loggedIn_home";
	}

	@RequestMapping(value = "/stats", method = RequestMethod.GET)
	public String getStats(@RequestParam(value = "replayId", required = true) String replayId,  HttpServletRequest request, ModelMap model) throws IOException{
		
		String currentDir = System.getProperty("user.dir");//directory we are in
		String replayParserLoc = currentDir+"/testReplaysAndData/DotaParser.exe";
		String replayLoc = currentDir+"/"+uploadedFileList.get(replayId);//TODO get from db
		
		if(System.getProperty("os.name").toLowerCase().contains("windows")){//Replacing front slash with back slash for windows os directories
			replayParserLoc =  replayParserLoc.replaceAll("/", "\\\\");
			replayLoc = replayLoc.replaceAll("/", "\\\\");
		}
		
		
		Runtime.getRuntime().exec(replayParserLoc+" "+replayLoc);
		
		//I just have my absolute path here for testing this - jano
		Runtime.getRuntime().exec("C:\\Python27\\python getPlayerStats.py "+steamId64+" "+replayId);

		model.addAttribute("message", replayParserLoc+" "+replayLoc);
		
		request.setAttribute("genImageNames", genImageNames);
		
		return "stats";
	}
	
	
	@RequestMapping(value = "/delete", method = RequestMethod.POST)
	public String deleteFile(@RequestParam(value = "replayName", required = true) String replayName, HttpServletRequest request, ModelMap model) {
		
		
		//deleting file from system
		String currentDir = System.getProperty("user.dir");
		String fileToDel = currentDir+"/uploads/."+steamId64+"/"+replayName;
		if(System.getProperty("os.name").toLowerCase().contains("windows")){//Replacing front slash with back slash for windows os directories
			fileToDel =  fileToDel.replaceAll("/", "\\\\");
		}
		File file = new File(fileToDel);
		file.delete();
		
		//deleting file from db
		String match_id = replayName.substring(0, replayName.lastIndexOf("."));
		
		Session session = HibernateUtil.getSessionFactory().openSession();
		session.beginTransaction();
		
		String queryString =
				"DELETE FROM replay WHERE uploader = :uploader AND match_id = :match_id";
		
		SQLQuery query = session.createSQLQuery(queryString);
		query.setParameter("uploader", Long.parseLong(steamId64));
		query.setParameter("match_id", match_id);
		query.executeUpdate();
		
        session.getTransaction().commit();
        		
        model.addAttribute("message", "deleted file with match id "+match_id+"Query: DELETE FROM replay WHERE uploader = "+steamId64+" AND match_id = "+match_id);
	
        
        getUploadedFiles();
		request.setAttribute("uploadedFileList", uploadedFileList);
        
        return "loggedIn_home";
	
	}

	private String get64BitSteamId(String claimedId){		
		//getting only the 64bit number from the returned claimed ID from steam
		//claimedId is in the format: http://steamcommunity.com/openid/id/<steamid>
		return claimedId.substring(claimedId.indexOf("/id/")+4);
	}

	private String getSteamUsername(String steamId64) throws ParserConfigurationException, MalformedURLException, SAXException, IOException{
		//getting xml of your steam profile which contains display name
		DocumentBuilderFactory fac = DocumentBuilderFactory.newInstance();
		DocumentBuilder builder = fac.newDocumentBuilder();
		Document document = builder.parse(new URL("http://steamcommunity.com/profiles/" + steamId64 + "/?xml=1").openStream());

		//extracting the "<steamID>" tag which contains display name
		NodeList rootElement = document.getElementsByTagName("steamID");

		return rootElement.item(0).getTextContent();
	}
	
	private String convertSteamID64ToSteamID(String steamId64) {
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

	private String uploadFile(HttpServletRequest request){

		File file;
		String filePath = "uploads/."+steamId64+"/";
		String fileName = "";

		if (ServletFileUpload.isMultipartContent(request)) {

			DiskFileItemFactory factory = new DiskFileItemFactory();

			// Create a new file upload handler
			ServletFileUpload upload = new ServletFileUpload(factory);

			try{ 
				// Parse the request to get file items.
				List<?> fileItems = upload.parseRequest(request);

				// Process the uploaded file items
				Iterator<?> i = fileItems.iterator();

				while ( i.hasNext () ){
					FileItem fi = (FileItem)i.next();
					if ( !fi.isFormField () ){
						fileName = fi.getName();               

						if(!fileName.substring(fileName.lastIndexOf(".")).toLowerCase().equals(".dem")){
							return "File not uploaded please upload a .DEM file";
						}
						
						//checking if path exists
						File checkPath = new File(filePath);
						if(!checkPath.exists()){
							checkPath.mkdirs();
						}

						file = new File( filePath + fileName) ;

						fi.write( file ) ;

					}
				}
			}catch(Exception ex) {
				System.out.println(ex);
			}
		}

//		uploadedFileList.put(fileName, filePath);
		
		int matchId = Integer.parseInt(fileName.substring(0, fileName.indexOf(".")));
		
		Session session = HibernateUtil.getSessionFactory().openSession();
		session.beginTransaction();
		
		Replay replay = new Replay();
		replay.setGraphOnePath("");//TODO
		replay.setGraphTwoPath("");//TODO
		replay.setMatchId(matchId);
		replay.setReplayPath(filePath+fileName);
		replay.setUploader(Long.parseLong(steamId64));
		
		session.save(replay);
		session.getTransaction().commit();

		return "file uploaded to"+filePath+fileName;
	}
	
	private void getUploadedFiles(){
		
		//getting list of files user has uploaded
		uploadedFileList.clear();		
		
		Session session = HibernateUtil.getSessionFactory().openSession();
		session.beginTransaction();
		
		String queryString =
				"SELECT match_id, replay_path FROM replay WHERE uploader = :uploader";
		
		SQLQuery query = session.createSQLQuery(queryString);
		query.setParameter("uploader", Long.parseLong(steamId64));
		query.setResultTransformer(Criteria.ALIAS_TO_ENTITY_MAP);
		List results = query.list();

		
        for(Object object : results)
        {
           Map row = (Map)object;
           uploadedFileList.put(row.get("match_id").toString()+".dem", row.get("replay_path").toString());
        }
        
        session.getTransaction().commit();
	}
}

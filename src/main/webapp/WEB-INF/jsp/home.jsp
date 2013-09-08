<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib uri="http://www.springframework.org/tags/form" prefix="form" %>
<%@ taglib uri="http://www.springframework.org/tags" prefix="spring" %>

<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<html>
	<body>
	
	<!-- -------------------------------LOGIN FORM---------------------------------------- -->
	<c:url var="openIDLoginUrl" value="/j_spring_openid_security_check" />
	<form action="${openIDLoginUrl}" method="post">
	  <input name="openid_identifier" type="hidden" value="http://steamcommunity.com/openid"/>
	  <input type="image" src="/resouces/steamlogo.png">  
	</form>
	<!-- --------------------------------------------------------------------------------- -->
	
		<p>
			${message}
		</p>	
		
	</body>


</html>
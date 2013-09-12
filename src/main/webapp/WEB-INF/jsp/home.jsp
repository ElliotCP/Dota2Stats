<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib uri="http://www.springframework.org/tags/form" prefix="form" %>
<%@ taglib uri="http://www.springframework.org/tags" prefix="spring" %>

<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>

<html>
	<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
	<script type="js/bootstrap.js"></script>
	<head>
		<title>Home Page</title>
		<meta name="viewport" content="width=devicewith, initial-scale=1.0">
		<link rel="stylesheet" href="${pageContext.request.contextPath}/css/bootstrap.css">
		<link rel="stylesheet" href="${pageContext.request.contextPath}/css/bootstrap-responsive.css">
	</head>
	<body>
		<div class="navbar navbar-static-top">
			<div class="navbar-inner">
				<div class="container">
					<a href="#" class="brand">(name goes here)</a>
					<div class="nav-collapse-collapse">
						<ul class="nav pull-right">
							<li><a href="#">Home</a></li>
							<li><a href="#">About us</a></li>
							<li>
								<!-- -------------------------LOGIN FORM---------------------------------- -->
								<c:url var="openIDLoginUrl" value="/j_spring_openid_security_check" />
								<form action="${openIDLoginUrl}" method="post">
									<input name="openid_identifier" type="hidden" value="http://steamcommunity.com/openid"/>
									<input type="image" src="/img/steamlogo.png">  
								</form>
								<!-- --------------------------------------------------------------------- -->
							</li>
						</ul>
					</div>	
				</div>
			</div>		
		</div>
		<div>
			<p>${message}</p>	
		</div>
	</body>
</html>
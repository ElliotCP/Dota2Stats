<%@ page import="com.se325.controller.*"%>   
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
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
						<li><a href="/logout" > Logout (${username})</a></li>
					</ul>
				</div>	
			</div>
		</div>		
		</div>
		<div>
			<p>${message}</p>	
		</div>
		<div>
			<ul>
				<c:forEach items="${genImageNames}" var="i">
					<li><img src="/img/steamlogo.png"></li><!--change from picture of steam logo to actual graph-->
				</c:forEach>
			</ul>
		</div>
	</body>
</html>
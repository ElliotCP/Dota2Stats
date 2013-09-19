<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib uri="http://www.springframework.org/tags/form" prefix="form" %>
<%@ taglib uri="http://www.springframework.org/tags" prefix="spring" %>

<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>

<html lang="en">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta name="description" content="">
	<meta name="author" content="">
	<link rel="shortcut icon" href="../../assets/ico/favicon.png">

	<title>drs &middot; Dota Replay Statistics</title>

	<!-- Bootstrap core CSS -->
	<link href="../dist/css/bootstrap.css" rel="stylesheet">

	<!-- Custom styles for this template -->
	<link href="../assets/css/jumbotron.css" rel="stylesheet">

	<!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
  	<!--[if lt IE 9]>
		<script src="assets/js/html5shiv.js"></script>
		<script src="assets/js/respond.min.js"></script>
		<![endif]-->
	</head>

	<body>

		<div class="navbar navbar-inverse navbar-fixed-top">
			<div class="container">
				<div class="navbar-header">
					<button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
					</button>
					<a href="/user/home"><img class="bannerLogo" src="../img/smallLogo.png"></a>
				</div>

				<div class="navbar-collapse collapse">
					<ul class="nav navbar-nav">						
						<li><a href="/user/home">Home</a></li>
						<li class="active"><a href="#">About</a></li>
					</ul>
					<c:url var="openIDLoginUrl" value="/j_spring_openid_security_check" />
					<form class="navbar-form navbar-right" action="${openIDLoginUrl}" method="post">
						<input name="openid_identifier" type="hidden" value="http://steamcommunity.com/openid"/>
						<input type="image" src="/img/steamlogo.png">  
					</form>
				</div><!--/.navbar-collapse -->
			</div>
		</div>

		<div class="jumbotron">
      		<div class="container">
        		<h1>EJK: SOFTENG325 Group Assignment</h1>
        		<p>Team members: <br> Elliot Colquhoun - ecol120 - 2782843 <br> Ken Neth Yeoh - kyeo475 - 5386221 <br> Janodya Moonamale - jmoo829 - 5457480</p>
      		</div>
    	</div>

    	<div class="container">
    	<h3>Sources</h3>
    	<p>Bootstrap - Web framework<br>Flask - Python web server<br>Python Imaging Libarary - Graph generation<br>Java Spring - Main backend<br>Tony Young - Python server hosting</p>
    	</div>

		<div class="container">

			<hr>

			<footer>
				<p>&copy; EJK 2013</p>
			</footer>
		</div> <!-- /container -->


	<!-- Bootstrap core JavaScript
	================================================== -->
	<!-- Placed at the end of the document so the pages load faster -->
	<script src="../assets/js/jquery.js"></script>
	<script src="../dist/js/bootstrap.min.js"></script>
</body>
</html>
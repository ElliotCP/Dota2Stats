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
					<a href="/"><img class="bannerLogo" src="../img/smallLogo.png"></a>
				</div>

				<div class="navbar-collapse collapse">
					<ul class="nav navbar-nav">
						<li class="active"><a href="#">Home</a></li>
						<li><a href="/about">About</a></li>
					</ul>
					<c:url var="openIDLoginUrl" value="/j_spring_openid_security_check" />
					<form class="navbar-form navbar-right" action="${openIDLoginUrl}" method="post">
						<input name="openid_identifier" type="hidden" value="http://steamcommunity.com/openid"/>
						<input type="image" src="/img/steamlogo.png">  
					</form>
				</div><!--/.navbar-collapse -->
			</div>
		</div>

		<!-- Main jumbotron for a primary marketing message or call to action -->
		<div class="jumbotron">
			<div class="container">
				<h1>Put yourself in the spotlight.</h1>
				<p>See your personal statistics for any game from any time. Last hits, denies, kills, assists, deaths, gold-per-minute, item progression. It's all here, laid out in graph form.</p>
				<p><a class="btn btn-primary btn-lg">Learn more &raquo;</a></p>
			</div>
		</div>

		<div class="container">
			<!-- Example row of columns -->
			<div class="row">
				<div class="col-lg-4">
					<h2>Damage over time</h2>
					<img class="img-circle" src="../img/damageOverTime.png" alt="Generic placeholder image">
					<p>See when you're doing damage, who you're doing damage to, how much you're doing and more. No damage until late game? Too aggressive early? Look for trends and fix your play style. </p>
					<p><a class="btn btn-default" href="#">View details &raquo;</a></p>
				</div>
				<div class="col-lg-4">
					<h2>Item progression</h2>
					<img src="../img/branch.png" alt="Generic placeholder image">
					<p>Make sure you're getting the right items by the right times. See if you're farming quick enough and getting the right items for the right game conditions. Also, divine counter.</p>
					<p><a class="btn btn-default" href="#">View details &raquo;</a></p>
				</div>
				<div class="col-lg-4">
					<h2>Gold per minute</h2>
					<img src="../img/gold.png" alt="Generic placeholder image">
					<p>Get accurate measurements of your gold per minute throughout the game. Discover trends in your farming and find your weak spots in your game play. Get that 1000gpm alchemist you've always dreamed of.</p>
					<p><a class="btn btn-default" href="#">View details &raquo;</a></p>
				</div>
			</div>

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

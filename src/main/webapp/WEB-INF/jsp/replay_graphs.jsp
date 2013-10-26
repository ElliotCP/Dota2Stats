<%@ page import="com.se325.controller.*"%>   
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
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
	<link href="jumbotron.css" rel="stylesheet">

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
						<li class="active"><a href="#">Generate Stats</a></li>
					</ul>
					<form class="navbar-form navbar-right" style="margin-top:20px;">						
						<a name="logout()" href="/logout" style="color:white;">Logout (${profileName})</a>
					</form>
				</div><!--/.navbar-collapse -->
			</div>
		</div>

		<div class="jumbotron">
      		<div class="container">
        		<h1>Graphs for ${profileName} in match number: ${replayId}</h1>
        		<p>Each graph shows the relevant data throughout the match, starting from the start of each game (before the horn blows) until the moment an ancient falls.</p>
      		</div>
    	</div>


    	<!--
    		To get the images, set the image source as http://223.27.24.159:5000/?matchid=XXXXX&steamid=XXXXXX&imagename=XXXXXXXX
			List of images: 
				playerAssistsGraph.png
				playerDamageDealtGraph.png
				playerDeathsGraph.png
				playerGoldGraph.png
				playerGPMGraph.png
				playerItemProgressionGraph.png
				playerLevelGraph.png
				playerRunePickupsGraph.png
				playerKillsGraph.png
				playerDamageTakenGraph.png

    	 -->

		<div class="container marketing" style="margin-top:50px;text-align:center;">
			<hr class="featurette-divider">

      		<div class="row featurette">
		        <div class="col-md-7">
		          <h2 class="featurette-heading">Kills. <span class="text-muted">Kills on each enemy over time.</span></h2>
		          <p class="lead"></p>
		        </div>
		        <div class="col-md-5">
		          <img class="featurette-image img-responsive" src="http://223.27.24.159:5000/?steamid=${steamId64}&matchid=${replayId}&imagename=playerKillsGraph.png" data-src="holder.js/500x500/auto" alt="No Kills This Game">
		        </div>
		    </div>

		    <hr class="featurette-divider">

      		<div class="row featurette">
      			<div class="col-md-5">
		          <img class="featurette-image img-responsive" src="http://223.27.24.159:5000/?steamid=${steamId64}&matchid=${replayId}&imagename=playerDeathsGraph.png" data-src="holder.js/500x500/auto" alt="No Deaths This Game">
		        </div>
		        <div class="col-md-7">
		          <h2 class="featurette-heading">Deaths. <span class="text-muted">Each of your deaths over time.</span></h2>
		          <p class="lead"></p>
		        </div>
		        
		    </div>

		    <hr class="featurette-divider">

      		<div class="row featurette">
		        <div class="col-md-7">
		          <h2 class="featurette-heading">Assists. <span class="text-muted">Player assists on kills over time.</span></h2>
		          <p class="lead"></p>
		        </div>
		        <div class="col-md-5">
		          <img class="featurette-image img-responsive" src="http://223.27.24.159:5000/?steamid=${steamId64}&matchid=${replayId}&imagename=playerAssistsGraph.png" data-src="holder.js/500x500/auto" alt="No Assists This Game">
		        </div>
		    </div>

		    <hr class="featurette-divider">

      		<div class="row featurette">
      			<div class="col-md-5">
		          <img class="featurette-image img-responsive" src="http://223.27.24.159:5000/?steamid=${steamId64}&matchid=${replayId}&imagename=playerDamageDealtGraph.png" data-src="holder.js/500x500/auto" alt="No Damage Dealt This Game">
		        </div>
		        <div class="col-md-7">
		          <h2 class="featurette-heading">Damage dealt. <span class="text-muted">Damage dealth throughout the game.</span></h2>
		          <p class="lead"></p>
		        </div>
		    </div>

		    <hr class="featurette-divider">

      		<div class="row featurette">
		        <div class="col-md-7">
		          <h2 class="featurette-heading">Damage taken. <span class="text-muted">Damage taken from enemy heroes over time.</span></h2>
		          <p class="lead"></p>
		        </div>
		        <div class="col-md-5">
		          <img class="featurette-image img-responsive" src="http://223.27.24.159:5000/?steamid=${steamId64}&matchid=${replayId}&imagename=playerDamageTakenGraph.png" data-src="holder.js/500x500/auto" alt="No Damage Taken This Game">
		        </div>
		    </div>

		    <hr class="featurette-divider">

      		<div class="row featurette">
      			<div class="col-md-5">
		          <img class="featurette-image img-responsive" src="http://223.27.24.159:5000/?steamid=${steamId64}&matchid=${replayId}&imagename=playerGoldGraph.png" data-src="holder.js/500x500/auto" alt="No Gold Gained This Game">
		        </div>
		        <div class="col-md-7">
		          <h2 class="featurette-heading">Gold. <span class="text-muted">Total gold gained during the game.</span></h2>
		          <p class="lead"></p>
		        </div>
		    </div>

		    <hr class="featurette-divider">

      		<div class="row featurette">
		        <div class="col-md-7">
		          <h2 class="featurette-heading">GPM. <span class="text-muted">Gold-per-minute over time.</span></h2>
		          <p class="lead"></p>
		        </div>
		        <div class="col-md-5">
		          <img class="featurette-image img-responsive" src="http://223.27.24.159:5000/?steamid=${steamId64}&matchid=${replayId}&imagename=playerGPMGraph.png" data-src="holder.js/500x500/auto" alt="No GPM This Game">
		        </div>
		    </div>

		    <hr class="featurette-divider">

      		<div class="row featurette">
      			<div class="col-md-5">
		          <img class="featurette-image img-responsive" src="http://223.27.24.159:5000/?steamid=${steamId64}&matchid=${replayId}&imagename=playerLevelGraph.png" data-src="holder.js/500x500/auto" alt="No Player Levels This Game">
		        </div>
		        <div class="col-md-7">
		          <h2 class="featurette-heading">Levels. <span class="text-muted">Player level over time.</span></h2>
		          <p class="lead"></p>
		        </div>
		    </div>

		    <hr class="featurette-divider">

      		<div class="row featurette">
		        <div class="col-md-7">
		          <h2 class="featurette-heading">Items. <span class="text-muted">Item progression throughout the game.</span></h2>
		          <p class="lead"></p>
		        </div>
		        <div class="col-md-5">
		          <img class="featurette-image img-responsive" src="http://223.27.24.159:5000/?steamid=${steamId64}&matchid=${replayId}&imagename=playerItemProgressionGraph.png" data-src="holder.js/500x500/auto" alt="No Item Progression This Game">
		        </div>
		    </div>

		    <hr class="featurette-divider">

      		<div class="row featurette">
      			<div class="col-md-5">
		          <img class="featurette-image img-responsive" src="http://223.27.24.159:5000/?steamid=${steamId64}&matchid=${replayId}&imagename=playerRunePickupsGraph.png" data-src="holder.js/500x500/auto" alt="No Runes This Game">
		        </div>
		        <div class="col-md-7">
		          <h2 class="featurette-heading">Runes. <span class="text-muted">Runes picked up as well as bottled over time.</span></h2>
		          <p class="lead"></p>
		        </div>
		    </div>
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

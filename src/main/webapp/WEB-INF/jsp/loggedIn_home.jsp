<html>
	<body>

		<p>
			${message}
		</p>	
		<form action="UploadReplay" method="post" enctype="multipart/form-data">
			<input type="file" name="file" accept=".DEM" />
			<br />
			<input type="submit" value="Upload File" />
		</form>
	</body>


</html>
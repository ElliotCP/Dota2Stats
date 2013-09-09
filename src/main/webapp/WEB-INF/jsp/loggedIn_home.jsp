<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<html>
	<body>
	
	<a href="/main/logout" > Logout</a>

		<p>
			${message}
		</p>	
		<form action="UploadReplay" method="post" enctype="multipart/form-data">
			<input type="file" name="file"/>
			<br />
			<input type="submit" value="Upload File" />
		</form>
	</body>


</html>
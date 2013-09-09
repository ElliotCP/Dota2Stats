<%@ page import="com.se325.controller.*"%>   
<%@ page import="java.io.*,java.util.*, javax.servlet.*" %>
<%@ page import="javax.servlet.http.*" %>
<%@ page import="org.apache.commons.fileupload.*" %>
<%@ page import="org.apache.commons.fileupload.disk.*" %>
<%@ page import="org.apache.commons.fileupload.servlet.*" %>
<%@ page import="org.apache.commons.io.output.*" %>


<%
   File file ;
   //ServletContext context = pageContext.getServletContext();
   //String filePath = context.getInitParameter("file-upload");
	String filePath = "uploads/."+request.getAttribute("username64Bit")+"/";
	
   // Verify the content type
   String contentType = request.getContentType();
   if (ServletFileUpload.isMultipartContent(request)) {

      DiskFileItemFactory factory = new DiskFileItemFactory();
      // Create a new file upload handler
      ServletFileUpload upload = new ServletFileUpload(factory);

      try{ 
         // Parse the request to get file items.
         List fileItems = upload.parseRequest(request);

         // Process the uploaded file items
         Iterator i = fileItems.iterator();

         out.println("<html>");
         out.println("<head>");
         out.println("<title>JSP File upload</title>");  
         out.println("</head>");
         out.println("<body>");
         while ( i.hasNext () ) 
         {
            FileItem fi = (FileItem)i.next();
            if ( !fi.isFormField () )	
            {

            String fileName = fi.getName();
            
			//checking if path exists
			File checkPath = new File(filePath);
			if(!checkPath.exists()){
				checkPath.mkdirs();
			}

            file = new File( filePath + fileName) ;


            fi.write( file ) ;
            out.println("Uploaded Filename: " + filePath + 
            fileName + "<br>");
            }
         }
         out.println("</body>");
         out.println("</html>");
      }catch(Exception ex) {
         System.out.println(ex);
      }
   }
%>
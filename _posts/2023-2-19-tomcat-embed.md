# Tomcat Embed Tutorial

** pic	

   #+BEGIN_SRC plantuml :file test_uml.png :cmdline -charset UTF-8
   title Example Sequence Diagram
   activate Client
   Client -> Server: Session Initiation
   note right: Client requests new session
   activate Server
   Client <-- Server: Authorization Request
   note left: Server requires authentication
   Client -> Server: Authorization Response
   note right: Client provides authentication details
   Server --> Client: Session Token
   note left: Session established
   deactivate Server
   Client -> Client: Saves token
   deactivate Client
   #+END_SRC
   
** start example

   #+BEGIN_SRC java
     import org.apache.catalina.*;
     import org.apache.catalina.connector.Connector;
     import org.apache.catalina.core.StandardContext;
     import org.apache.catalina.core.StandardEngine;
     import org.apache.catalina.core.StandardHost;
     import org.apache.catalina.startup.Tomcat;

     import java.io.IOException;

     public class TomcatEmbedApplication {
	 public static void main(String[] args) throws LifecycleException, IOException {

	     // create tomcat
	     Tomcat tomcat = new Tomcat();
	     Server server = tomcat.getServer();
	     Service service = server.findService("Tomcat");
	     Connector connector = new Connector();
	     connector.setPort(8080);

	     Engine engine = new StandardEngine();
	     engine.setDefaultHost("host");

	     Host host = new StandardHost();
	     host.setName("host");

	     String contextPath = "";
	     Context context = new StandardContext();
	     context.setPath(contextPath);
	     context.addLifecycleListener(new Tomcat.FixContextListener());

	     host.addChild(context);
	     engine.addChild(host);
	     service.setContainer(engine);
	     service.addConnector(connector);

	     tomcat.addServlet(contextPath, "dispatcher", new IndexServlet());
	     context.addServletMappingDecoded("/*", "dispatcher");

	     tomcat.start();
	     tomcat.getServer().await();
	 }
     }	 
   #+END_SRC
   
   Create ~Tomcat~.
	 
   Creaet ~Server~ and add ~Server~ a ~Service~ named 'Tomcat'.
   The ~tomcat.getServer()~ method creates a server containing a service named 'tomcat'.
   So service is able to be found by ~server.findService("Tomcat")~.
	 
   Create ~Connector~ add set port '8080'.
   The ~connector.setPort(8080)~ set the port.

** 	 
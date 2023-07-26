---
title: Tomcat Embed Tutorial
date: 2023-02-19
---



# Tomcat Embed Tutorial



讲一下Tomcat的容器结构

Engine -> n* Host -> n* Context -> n* Wrapper -> Servlet



```java
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
```
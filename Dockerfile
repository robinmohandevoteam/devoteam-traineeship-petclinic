FROM jetty:latest

COPY ./target/petclinic.war /var/lib/jetty/webapps/ROOT.war
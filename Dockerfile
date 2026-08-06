FROM eclipse-temurin:21-jdk

WORKDIR /app

COPY target/*.jar atmosync.jar

EXPOSE 8080

ENTRYPOINT ["java","-jar","atmosync.jar"]

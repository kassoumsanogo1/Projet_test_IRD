package myAPP_version_finale;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;


@SpringBootApplication
public class NeuralNetworkAPI {

	//permet de lancer l'application
    public static void main(String[] args) {
        SpringApplication.run(test.class, args);
    } 
}
//CONSIGNES :
//Vous envoyez une requète sur http:localhost:8080/predict 
//avec le body contenant les données xml a envoyer.
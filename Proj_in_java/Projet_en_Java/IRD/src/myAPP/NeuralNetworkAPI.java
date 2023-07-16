package myAPP;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import org.tensorflow.SavedModelBundle;
import org.tensorflow.Tensor;
import org.tensorflow.TensorFlow;

import org.nd4j.linalg.api.ndarray.INDArray;

//import io.github.thomasnield.jnumpy.*;

import org.json.JSONArray;
import org.json.JSONObject;

//Ce code correspond à l'envoie de donnée numpy directement :
//Vous avez le choix entre utilisé Tensor directement pour recevoir les données ou Jnumpy
//Les 2 fonctionnes de la mème manière

@SpringBootApplication
@RestController
public class NeuralNetworkAPI {
    private SavedModelBundle model; 

    public NeuralNetworkAPI() {
        // Chargement du modèle de réseau de neurones
        model = SavedModelBundle.load("model.h5", "serve");
    }

    @PostMapping("/predict")
    public String infer(@RequestBody float[][] inputData) {
    	//JNumPyArray<Float> npInputArray = JNumPyArray.arrayOf(inputData);
        // Effectuer l'inférence avec le modèle
        
    	//inputTensor=inputData;
        //Pour des données numpy brute entrante
    	//Tensor<Float> inputTensor = Tensor.create(npInputArray.getData(), Float.class);
    	
    	Tensor<Float> inputTensor = Tensor.create(inputData);
        Tensor<Float> outputTensor = model.session().runner()
                .feed("matrix", inputTensor) 
                .fetch("matrix")
                .run()
                .get(0)
                .expect(Float.class);

        // Traitement du résultat
        float[] outputData = new float[outputTensor.shape()[0]];
        outputTensor.copyTo(outputData);

        // Renvoyer la réponse au client
        return formatOutput(outputData); // Fonction pour formater les résultats de sortie
    }

    private String formatOutput(float[] outputData) {
        // Implémentation pour formater les résultats de sortie en une chaîne JSON 
    	JSONArray jsonArray = new JSONArray(outputData); 
        JSONObject jsonResult = new JSONObject(); 
        jsonResult.put("output", jsonArray);
        return jsonResult.toString();
    }

    public static void main(String[] args) {
        //TensorFlow.loadLibrary(System.getProperty("java.library.path"));
        SpringApplication.run(NeuralNetworkAPI.class, args);
    }
}

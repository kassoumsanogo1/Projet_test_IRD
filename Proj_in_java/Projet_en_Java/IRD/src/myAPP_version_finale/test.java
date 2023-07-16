package myAPP_version_finale; 
import java.io.StringReader;

import javax.xml.bind.JAXBContext;
import javax.xml.bind.Unmarshaller;

import org.bytedeco.tesseract.MATRIX;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import org.tensorflow.SavedModelBundle;
import org.tensorflow.Tensor;
import org.tensorflow.types.TFloat32;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

//Ce codepermet l'envoie de donnée xml qui seront convertis avant d'ètre fourni au modèle pour prédiction

@SpringBootApplication
public class test {

    // Chemin vers le fichier HDF5 contenant le modèle TensorFlow
    private static final String MODEL_PATH = "model.h5";
    private ObjectMapper objectMapper;

    public test(ObjectMapper objectMapper) {
        this.objectMapper = objectMapper;
    } 

    @RestController
    public class PredictionController {

        @PostMapping("/predict")	
        public ResponseEntity<String> predict(@RequestBody String xmlData) {
            try (SavedModelBundle model = SavedModelBundle.load(MODEL_PATH, "serve")) {
            	
            	// Convertir la chaîne XML en objet Java à l'aide de JAXB
        		JAXBContext jaxbContext = JAXBContext.newInstance(MatrixData.class);
        		Unmarshaller unmarshaller = jaxbContext.createUnmarshaller();
        		MatrixData matrixData = (MatrixData) unmarshaller.unmarshal(new StringReader(xmlData));            	              
            	
        		// Prétraitement des données si nécessaire
        		//Ici je ne traite rien car pasnécessaire, je me contente de récupérer ma matrice de points,
        		//Mais si nécessaire le prétraitement se fera dans la méthode preprocessData();
                float[][] matrix = preprocessData(matrixData);
                
             // Convertir la matrice d'entrée en un objet Tensor
            	Tensor<Float> inputTensor = Tensor.create(matrix);	
            	
                // Exécuter la prédiction avec le modèle chargé
                Tensor<Float>[] outputTensors = model.session().runner()
                		
                		.feed("shape", inputTensor)
                        .fetch("shape")
                        .run()
                        .toArray();

                // Récupérer les résultats de la prédiction sous forme de tableau de doubles
                double[] prediction = outputTensors[0].copyTo(new double[1][])[0];

                // Libérer les ressources
                inputTensor.close();
                for (Tensor<Float> outputTensor : outputTensors) {
                    outputTensor.close();
                }

                // Convertir les résultats de la prédiction en JSON
                String jsonResult = objectMapper.writeValueAsString(prediction);

                // Retourner les résultats de la prédiction en tant que réponse JSON
                return ResponseEntity.ok(jsonResult);
                
            } catch (Exception e) {
                e.printStackTrace();
                // En cas d'erreur, retourner une réponse d'erreur appropriée
                return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
            }
        }
        public float[][] preprocessData(MatrixData matrixData) { 
            return matrixData.getMatrix();
        }
    }
}


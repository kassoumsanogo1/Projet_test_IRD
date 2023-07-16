package myAPP_version_finale; 

import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;

//Traitement des données matricielles si nécessaire
@XmlRootElement(name = "MatrixData")
public class MatrixData {
    @XmlElement(name = "Matrix")
    private float[][] matrix;

    public MatrixData() {
    }

    public MatrixData(float[][] matrix) {
        this.matrix = matrix;
    }

    public float[][] getMatrix() { 
        return matrix;
    }
    

    public void setMatrix(float[][] matrix) {
        this.matrix = matrix;
    }
}


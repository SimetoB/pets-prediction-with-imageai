from imageai.Prediction.Custom import CustomImagePrediction
import os

execution_path = os.getcwd()

prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(os.path.join(execution_path, "model_ex-001_acc-0.333333.h5"))
prediction.setJsonPath(os.path.join(execution_path, "model_class.json"))
prediction.loadModel(num_objects=10)

for root, subdirs, files in os.walk("images-to-predict"):
    for filename in files:
        predictions, probabilities = prediction.predictImage(os.path.join(root, filename), result_count=1)

        for eachPrediction, eachProbability in zip(predictions, probabilities):
            print("\nFor file " + filename + "\nTop prediction:\n" + str(eachPrediction) + " : " + str(eachProbability) + "%")

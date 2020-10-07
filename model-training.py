from imageai.Prediction.Custom import ModelTraining
model_trainer = ModelTraining()
model_trainer.setModelTypeAsResNet()
model_trainer.setDataDirectory("pets")
model_trainer.trainModel(num_objects=3, num_experiments=15, enhance_data=True, batch_size=5, show_network_summary=False)

#Generate Random test cases from the dataset
echo "Generating Tests"
python generateTests.py

#Generate the prpbabilities of each word
echo "Calculating Probabilities"
python wordcount.py

#Classify the inputs
echo "Classifying the inputs"
python classifier.py

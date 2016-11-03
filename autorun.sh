#Generate Random test cases from the dataset
echo "Generating Tests"
python generateTests.py
#Generate the prpbabilities of each word
if [ $1 == 1 ]; then
    echo "Calculating Probabilities"
    python wordcount.py
    #Classify the inputs
    echo "Classifying the inputs"
    python classifier.py
fi
if [ $1 == 2 ]; then
    echo "Calculating Probabilities"
    python wordfreq.py
    #Classify the inputs
    echo "Classifying the inputs"
    python multclassifier.py
fi
if [ $1 == 3 ]; then
    echo "Calculating Probabilities"
    python wordfreq.py
    #Classify the inputs
    echo "Classifying the inputs"
    python rforest.py
fi
if [ $1 == 4 ]; then
    echo "Calculating Probabilities"
    python wordfreq.py
    #Classify the inputs
    echo "Classifying the inputs"
    python multrforest.py
fi

from flask import Flask, render_template, request, jsonify
from neo4j import GraphDatabase
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model


#model = pickle.load(open('detect.pkl','rb'))
model1 = load_model('general_model.h5')
model2 = load_model('recall1_model.h5')
model3 = load_model('precision1_model.h5')
app = Flask(__name__)

# Define the Neo4j connection parameters
uri = "neo4j+s://1c35af50.databases.neo4j.io"
user = "neo4j"
password = "Q_SHyo8GbjH_5ngURmUJctSh8z8TAWZtvlfLZw7TjTw"

# Function to fetch user details from Neo4j based on UUID
def fetch_user_details_by_uuid(uuid):
    with GraphDatabase.driver(uri, auth=(user, password)) as driver:
        with driver.session() as session:
            result = session.run(
                '''MATCH (u:User {guid: $uuid}) RETURN 
                u.sharedIdsDegree AS sharedIdsDegree,
                u.p2pSharedCardPageRank AS p2pSharedCardPageRank,
                u.p2pSentPageRank AS p2pSentPageRank,
                u.p2pReceivedWeightedPageRank AS p2pReceivedWeightedPageRank,
                u.p2pReceivedWeightedDegree AS p2pReceivedWeightedDegree,
                u.ipDegree AS ipDegree,
                u.cardDegree AS cardDegree,
                u.deviceDegree AS deviceDegree,
                u.communitySize AS communitySize,
                u.partOfCommunity AS partOfCommunity ''',
                {"uuid": uuid}
            )
            user_details = result.single()
            if user_details:
                user_array = np.array(user_details.values())
                return user_array
            else:
                return None

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def fetch_user_details():
    data = request.json
    uuid = data.get('uuid')
    if not uuid:
        return jsonify({'error': 'UUID not provided'}), 400

    # Call the function to fetch user details from Neo4j
    user_details = fetch_user_details_by_uuid(uuid)

    if user_details is None:
        return jsonify({'error': 'User not found'}), 404
    
    # Convert Neo4j record to dictionary
    pred1 = model1.predict(user_details.reshape(1,-1)).tolist()
    pred2 = model2.predict(user_details.reshape(1,-1)).tolist()
    pred3 = model3.predict(user_details.reshape(1,-1)).tolist()
    pred={'Large Transaction Fraud Detection Model: TitanShield':pred2,'Precision-focused Model for Small Transactions: NanoGuard':pred3,'General Transaction Model: OmniWatch':pred1}

    return jsonify(pred)

if __name__ == '__main__':
    app.run(debug=True)
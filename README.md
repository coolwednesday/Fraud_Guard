Fraud_Guard - Real Time Payment Fraud Detection Api deployed on Google Cloud

Below is a simple demonstration of our deployed api depicting probabilities of fraud for an User-ID, using the three Deep Learning Models developed in this project by Hyperparameter Tuning for recall, precision and accuracy for different usecases.
<video src="https://github.com/coolwednesday/Fraud_Guard/assets/98943137/d9531c94-9897-4822-9103-1512a6b8cd0f"/>



BASIC FLOW : -

We give the User-Id of the existing user in our graph database.

Api makes connection with Neo4j Graph Database and fetch the features.

Our three models give probability of User being a fraud based on its graphical features. ( For more info , read report )



USECASES

Our system uses three different models to handle different types of payment transactions:

a. General Transactional Model (OmniWatch): This model works for payment gateways handling various transaction types, from big money transfers to small daily purchases. It aims to strike a balance between accuracy and coverage, ensuring reliable performance across different transaction sizes.

b. Large Transaction Fraud Detection Model (TitanShield): Specifically designed for payment gateways dealing with large transactions, this model focuses on catching potential fraud while keeping false alarms low. It uses a carefully adjusted setup to minimize missing fraud cases and includes tools for quick problem-solving when mistakes happen.

c. Precision-focused Model For Small Transactions (NanoGuard): Tailored for payment gateways processing many small transactions, NanoGuard puts accuracy first to avoid unnecessary flags. It's crucial for maintaining customer trust and operational efficiency, especially considering the sheer volume of transactions involved.

These models can be used alone or combined based on what a business needs. By offering options tailored to different situations, our system helps payment gateways ensure secure transactions while keeping customers happy.



Our Api was Deployed on Cloud using Docker and Ml Cloud Run in GCP. The Deployment has been removed due to continuous billing charges.


Checkout The Report For Further Information on Model Summaries/Performance and Dataset Exploration using Neo4j Graph Database & Python Libraries :

https://github.com/coolwednesday/Fraud_Guard/blob/main/ProjectReport.pdf

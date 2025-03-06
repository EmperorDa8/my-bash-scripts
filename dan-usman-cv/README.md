# Dan Usman's CV Web Application

This project contains a web application that displays Dan Usman's CV in an HTML page with minimal animations. It's designed to be deployed to Google Kubernetes Engine (GKE) using Google Cloud Build and Cloud Deploy for CI/CD.

## Project Structure

```
cv-app/
├── app.py                     # Flask application to serve the CV
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Container configuration
├── static/                    # Static assets folder
│   └── index.html             # CV HTML content
├── kubernetes-manifests/      # Kubernetes configuration
│   ├── deployment.yaml        # Deployment configuration
│   └── service.yaml           # Service configuration
├── cloudbuild.yaml            # Cloud Build configuration
└── clouddeploy.yaml           # Cloud Deploy configuration
```

## Local Development

1. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application locally:
   ```
   python app.py
   ```

4. Open your browser and navigate to `http://localhost:8080`

## Deployment to GKE

### Prerequisites

1. Install the Google Cloud SDK: https://cloud.google.com/sdk/docs/install
2. Initialize the gcloud CLI:
   ```
   gcloud init
   ```
3. Create a GKE cluster (if not already created):
   ```
   gcloud container clusters create cv-app-cluster \
     --zone us-central1-a \
     --num-nodes 2 \
     --machine-type e2-small
   ```

### Manual Deployment

1. Build the Docker image:
   ```
   docker build -t gcr.io/[PROJECT_ID]/cv-app:latest .
   ```

2. Push the image to Google Container Registry:
   ```
   docker push gcr.io/[PROJECT_ID]/cv-app:latest
   ```

3. Apply the Kubernetes manifests:
   ```
   kubectl apply -f kubernetes-manifests/
   ```

### CI/CD Deployment

1. Update the `PROJECT_ID` and `REGION` placeholders in the Kubernetes manifests and Cloud Deploy configuration.

2. Set up Cloud Build trigger:
   ```
   gcloud builds triggers create github \
     --repo=[YOUR_GITHUB_REPO] \
     --branch-pattern="main" \
     --build-config=cloudbuild.yaml
   ```

3. Set up Cloud Deploy:
   ```
   gcloud deploy apply --file=clouddeploy.yaml
   ```

4. Push your code to the GitHub repository to trigger a build and deployment.

## Accessing the Deployed Application

After successful deployment, you can get the external IP of the service:

```
kubectl get service cv-app-service
```

Open your browser and navigate to `http://[EXTERNAL_IP]`

## Updating the CV

To update the CV content, simply modify the `static/index.html` file and push the changes to your GitHub repository. The CI/CD pipeline will automatically build and deploy the updated application.
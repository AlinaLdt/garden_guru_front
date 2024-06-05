# Garden Guru Documentation

## Table of Contents
   1. Introduction
   2. Features 
   3. Tech Stack 
   4. Installation 
   5. Usage 
   6. Deployment 
   7. Directory Structure 
   8. Contributing 
   9. License
 
## Introduction

Garden Guru is an AI-powered web application designed to assist plant enthusiasts in caring for their houseplants. Users can upload images of their plants to receive care tips and ask questions about plant care through a chatbot interface.

## Features 

- Image Upload: Users can upload images of their houseplants.

- Plant Classification: The application classifies the uploaded plant images using a pre-trained model from Roboflow.

- Chatbot: Based on the classified plant, an AI-powered chatbot generates detailed care tips about plant care.

## Tech Stack
- Frontend: Streamlit 
- [Backend](https://github.com/AlinaLdt/garden_guru_back): FastAPI
- AI Models: OpenAI GPT-3.5-turbo
- Containerization: Docker 
- Cloud Platform: Google Cloud Platform (GCP)
- API Integration: Roboflow for image analysis

## Installation
To set up Garden Guru locally, follow these steps: 

### Prerequisites 
- Python 3.10
- Docker 
- Google Cloud Platform account 

### Steps Frontend
   
    1. Clone the repository: 
        git clone https://github.com/AlinaLdt/garden_guru_front.git

    2. Install the required libraries:
        pip install -r requirements.txt

    3. Set up environment variables: 
            Create a .env file in both the frontend and backend directories. 
            With the following variables for the frontend:
                API_HOST=http://localhost:8000
    4. Run the frontend application: 
            cd ../garden_guru_front
            make run 

### Steps Backend
   
    1. Clone the repository: 
        git clone https://github.com/AlinaLdt/garden_guru_back
    
    2. Install the required libraries:
        pip install -r requirements.txt

    3. Set up environment variables: 
            OPENAI_API_KEY=your_openai_api_key
            ROBOFLOW_API_KEY=your_roboflow_api_key
            PORT=8000
            SYSTEM_PROMPT="You are a plant expert..."
            GENERIC_PLANT_NAME="generic plant"
            CARE_TIPS_PROMPT_SYSTEM="You are in the role of a plant expert..."
            CARE_TIPS_PROMPT_USER="Give some care tips for a {plant_class}..."
            
            ----------------------DEPLOYMENT VARIABELS------------------------
            GAR_IMAGE=garden_guru
            GCP_REGION=europe-west1
            GCP_PROJECT="Your Project-ID"
            GAR_MEMORY=2Gi

    4. Build and run the Docker container for the backend:
            cd garden_guru_back
            make docker_build 
            make docker_run 
 

## Usage 
    1. Access the application: 
            - Open your web browser and go to 'http://localhost:8501'
    
    2. Upload an image: 
            - Click "Choose an image..." to upload a photo of your plant.
            - Receive care tips for the plant.
    
    3. Ask a question: 
            - Enter your question in the text box.
            - Click "Ask" to receive an expert answer.

## Deployment Frontend
Create a [Streamlit Account](https://streamlit.io/cloud) and link it to your GitHub repository.

## Deployment Backend
Google Cloud Platform 
1. Containerize the Application: Ensure your application is Dockerized. 

2. Push Docker Image to Google Container Registry  
```
docker tag garden-guru-back gcr.io/your-project-id/garden-guru-back
docker push gcr.io/your-project-id/garden-guru-back
```

3. Deploy to Google Cloud Run:
```
gcloud run deploy garden-guru-back --image gcr.io/your-project-id/garden-guru-back --platform managed
```

# Directory Structure 

### Frontend
```
GARDEN_GURU_FRONT/
├── .env
├── .envrc
├── .gitignore
├── Makefile
├── README.md
├── front_end/
│   ├── streamlit_design.py
│   └── ...
└── requirements.txt
```
### Backend
```
GARDEN_GURU_BACK/
├── .env
├── .envrc
├── .gitignore
├── Makefile
├── README.md
├── api/
│   ├── api.py
│   └── ...
├── Dockerfile
└── requirements.txt
```
## Contributing 

1. Fork the repository.
2. Create a new branch  (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -m 'Add new feature').
5. Push to the branch (git push origin feature-branch).
6. Open a pull request.

## License 

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International Public License (CC BY-NC 4.0). You are free to share and adapt the material, but not for commercial purposes. See the [LICENSE](https://creativecommons.org/licenses/by-nc/4.0/deed.en) file for more details.

---


    
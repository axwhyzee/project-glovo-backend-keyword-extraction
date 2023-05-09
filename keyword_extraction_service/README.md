Push docker container to Google Cloud

```
gcloud builds submit --tag gcr.io/project-glovo/index
```

Deploy docker container to Google Cloud Run service

```
gcloud run deploy --image gcr.io/project-glovo/index --platform managed
```

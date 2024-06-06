## Demo
Check the API Documentation here: https://recipe-app-poc-wdx2r4wvaq-as.a.run.app/apidocs/

## Deployment to Cloud Run
- Run `deploy.sh` it will push new image to the dockerhub
- Open Google Cloud Run console, select respective Service (create a new Service if you haven't)
- Click Edit & Deploy New Revision
- Update the new docker registry url with the new one

## Docker Registry URL (Example)
docker.io/luthfihrz/recipe-app-poc:$tag
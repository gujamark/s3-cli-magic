# Custom CLI Script for Uploading files in S3 Bucket

script can be used to upload files to amazon s3 bucket in the corresponding folder of the extension. For example:
test.pdf file will be uploaded in pdf/ folder

---

### Prerequisities

- python3
- Python libraries:
  - boto3==1.26.108
  - botocore==1.29.108
  - jmespath==1.0.1
  - python-dateutil==2.8.2
  - python-dotenv==1.0.0
  - python-magic==0.4.27
  - s3transfer==0.6.0
  - six==1.16.0
  - urllib3==1.26.15

---

### Note

- Script is written in _Python3_
- install requirements using the command below:

  `pip3 install -r requirements.txt`
  OR
  `poetry install`

- rename .env.example in auth folder to .env and assign corresponding values to variables

---

Example with poetry:
`poetry run python main.py -bn YOUR_BUCKET_NAME -f FILENAME1 FILENAME2`

Example without poetry
`python3 main.py -bn YOUR_BUCKET_NAME -f FILENAME1 FILENAME2`

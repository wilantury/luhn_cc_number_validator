# Credit Card validator

  

## Credit card number validator using LUMH algorithm.

  

## Getting started with docker

1. clone repository

>  ``` https://github.com/wilantury/luhn_cc_number_validator.git ```

2. Start Docker daemon.

3. Go into root directory "luhn_cc_number_validator".

4. Make a build of the application.

>  ``` docker build -t cc_validator_api .```

5. Validate if the image has been created.

>  ``` docker images``` You'll see an image named **cc_validator_api**

6. Run the application (API) into a docker container.

>  ``` docker run --env SECRET_KEY=secure-secret -p 8000:8000 --name api_cc_validator -d cc_validator_api```

  

That's it, You have your API running into a docker container. go to *http://localhost:8000/api/v1/card_validation*

  

The app is running in DEBUG mode, therefore you can test the API using the web browser. Anyway, you can use an API client like Postman or Insomnia to make the request.

  

Put into ``` cc_number``` the card number you want to validate.

  

local API: ``` http://localhost:8000/api/v1/card_validation```

method: POST

Body:

``` 
{
	"cc_number":"4111111111111111"
}
```

Response:

``` 
{
	"Issuer": "Visa"
}
```
import kagglehub

# Download latest version
path = kagglehub.dataset_download("prachi13/customer-analytics")

print("Path to dataset files:", path)


curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{
           "Warehouse_block": "F",
           "Mode_of_Shipment": "Ship",
           "Customer_care_calls": 4,
           "Customer_rating": 2,
           "Cost_of_the_Product": 177,
           "Prior_purchases": 3,
           "Product_importance": "low",
           "Gender": "F",
           "Discount_offered": 44,
           "Weight_in_gms": 1233
         }'

docker run -d -p 8000:8000 your-dockerhub-username/ml-fastapi-app:latest

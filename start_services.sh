#!/bin/bash

echo "Starting Checkout service..."
cd Microservices/Checkout/services
python3 main.py &
CHECKOUT_PID=$!

echo "Starting Search service..."
cd ../../Search
python3 Busqueda_Productos.py &
SEARCH_PID=$!

echo "Starting User Management service..."
cd ../User_management
python3 main.py &
USER_MANAGEMENT_PID=$!


wait $CHECKOUT_PID
wait $SEARCH_PID
wait $USER_MANAGEMENT_PID

chmod +x start_services.sh
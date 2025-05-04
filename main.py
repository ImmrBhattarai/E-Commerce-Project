import streamlit as st
from azure.storage.blob import BlobServiceClient
import pymssql
import uuid
import json
import os
import pandas as pd
from dotenv import load_dotenv
from math import ceil

# Load environment variables from .env file
load_dotenv()

# Azure Storage configuration
AZURE_CONNECTION_STRING = os.getenv("BLOB_CONNECTION_STRING")
AZURE_CONTAINER = os.getenv("BLOB_CONTAINER_NAME")
AZURE_ACCOUNT_NAME = os.getenv("BLOB_ACCOUNT_NAME")

# Azure SQL Database configuration
SQL_SERVER = os.getenv("SQL_SERVER")
SQL_DATABASE = os.getenv("SQL_DATABASE")
SQL_USERNAME = os.getenv("SQL_USER")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")

# Constants
PRODUCTS_PER_PAGE = 6

st.set_page_config(page_title="Cloud E-Commerce", layout="wide")
st.title("Product Registration - Cloud E-Commerce")

# Upload image to Azure Blob Storage
def upload_image_to_blob(file):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
        container_client = blob_service_client.get_container_client(AZURE_CONTAINER)

        blob_name = f"{uuid.uuid4()}.jpg"
        blob_client = container_client.get_blob_client(blob_name)

        blob_client.upload_blob(file.read(), overwrite=True)
        image_url = f"https://{AZURE_ACCOUNT_NAME}.blob.core.windows.net/{AZURE_CONTAINER}/{blob_name}"
        return image_url
    except Exception as e:
        st.error(f"Failed to upload image: {e}")
        return None

# Insert product into Azure SQL
def insert_product(product_data):
    try:
        conn = pymssql.connect(
            server=SQL_SERVER, user=SQL_USERNAME, password=SQL_PASSWORD, database=SQL_DATABASE
        )
        cursor = conn.cursor()
        insert_query = """
            INSERT INTO dbo.Products (name, description, price, image_url)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(insert_query, (
            product_data["name"], product_data["description"],
            product_data["price"], product_data["image_url"]
        ))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        st.error(f"Error inserting product into SQL: {e}")
        return False

# Retrieve products from SQL
def get_products():
    try:
        conn = pymssql.connect(
            server=SQL_SERVER, user=SQL_USERNAME, password=SQL_PASSWORD, database=SQL_DATABASE
        )
        cursor = conn.cursor(as_dict=True)
        cursor.execute("SELECT id, name AS name, description AS description, price AS price, image_url AS image_url FROM dbo.Products")
        products = cursor.fetchall()
        cursor.close()
        conn.close()
        return products
    except Exception as e:
        st.error(f"Error fetching products: {e}")
        return []

# Clean unused blobs from storage
def clean_unused_blobs(valid_blob_names):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
        container_client = blob_service_client.get_container_client(AZURE_CONTAINER)
        blobs = container_client.list_blobs()
        for blob in blobs:
            if blob.name not in valid_blob_names:
                container_client.delete_blob(blob.name)
    except Exception as e:
        st.error(f"Error cleaning up blobs: {e}")

# Display product cards with pagination
def display_product_cards_with_pagination(products):
    if not products:
        st.info("No products found.")
        return

    total_pages = ceil(len(products) / PRODUCTS_PER_PAGE)
    page = st.number_input("Page", min_value=1, max_value=total_pages, value=1, step=1)

    start_idx = (page - 1) * PRODUCTS_PER_PAGE
    end_idx = start_idx + PRODUCTS_PER_PAGE
    current_products = products[start_idx:end_idx]

    cols_per_row = 3
    cols = st.columns(cols_per_row)
    for i, product in enumerate(current_products):
        col = cols[i % cols_per_row]
        with col:
            st.subheader(product["name"])
            st.write(f"**Description:** {product['description']}")
            st.write(f"**Price:** ${product['price']:.2f}")
            if product["image_url"]:
                st.image(product["image_url"], width=200)
            st.markdown("---")
        if (i + 1) % cols_per_row == 0 and (i + 1) < len(current_products):
            cols = st.columns(cols_per_row)

# Product form
st.header("Register New Product")

product_name = st.text_input("Product Name")
product_description = st.text_area("Product Description")
product_price = st.number_input("Product Price", min_value=0.0, format="%.2f")
uploaded_file = st.file_uploader("Product Image", type=["jpg", "jpeg", "png"])

if st.button("Submit Product"):
    if not product_name or not product_description or product_price is None:
        st.warning("Please fill all the fields.")
    else:
        with st.spinner("Uploading and saving..."):
            image_url = ""
            if uploaded_file:
                image_url = upload_image_to_blob(uploaded_file)

            product_data = {
                "name": product_name,
                "description": product_description,
                "price": product_price,
                "image_url": image_url
            }

            if insert_product(product_data):
                st.success("Product successfully registered!")
                all_products = get_products()
                display_product_cards_with_pagination(all_products)

                valid_blobs = [p["image_url"].split("/")[-1] for p in all_products if p["image_url"]]
                clean_unused_blobs(valid_blobs)
            else:
                st.error("Failed to register product.")

        # Optional: Save locally for backup
        local_file = "products.json"
        if os.path.exists(local_file):
            with open(local_file, "r", encoding="utf-8") as f:
                try:
                    local_products = json.load(f)
                except json.JSONDecodeError:
                    local_products = []
        else:
            local_products = []

        local_products.append(product_data)
        with open(local_file, "w", encoding="utf-8") as f:
            json.dump(local_products, f, ensure_ascii=False, indent=4)

        st.json(product_data)

# Product listing
st.header("Product List")

if st.button("Load Products"):
    with st.spinner("Fetching products..."):
        all_products = get_products()
        display_product_cards_with_pagination(all_products)
        valid_blobs = [p["image_url"].split("/")[-1] for p in all_products if p["image_url"]]
        clean_unused_blobs(valid_blobs)
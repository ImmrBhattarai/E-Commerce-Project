# Storing E-Commerce Data in Azure | DIO Project
Developing a solution to store and manage e-commerce data in the cloud, focusing on scalability, security and efficiency.


Read my detailed article to see how you can do this as well: [Medium Article](https://immrbhattarai.medium.com)
(I will update this link in a few day, once the article is ready)

## Challenge Completed using Visual Studio Code (VS Code)

### What I did:
1. Created a resource group and SQL Database
   ![Screenshot From 2025-05-04 16-10-20](https://github.com/user-attachments/assets/329aaaa8-a604-409a-b6db-31561b96c7a0)
   ![Screenshot From 2025-05-04 16-19-10](https://github.com/user-attachments/assets/df92018d-4b21-43d8-8f87-8a0c4e3d7f12)
   ![Screenshot From 2025-05-04 19-23-03](https://github.com/user-attachments/assets/f5d8b254-8af1-43f1-9914-3f5d45680769)

   1.1 Created Database Server
   ![Screenshot From 2025-05-04 16-27-29](https://github.com/user-attachments/assets/56e496a1-0c5c-416c-a6a8-3949b022b2dc)
   ![Screenshot From 2025-05-04 16-49-16](https://github.com/user-attachments/assets/d2733da4-2c0a-4f7f-9026-67f333b2e602)

Following the step 1, the resources are created
![Screenshot From 2025-05-04 18-17-36](https://github.com/user-attachments/assets/735cd1cc-93b3-4ed1-b59f-0f566a222229)


2. Creating a storage account (Blob Storage in Azure)
![Screenshot From 2025-05-04 18-24-01](https://github.com/user-attachments/assets/9e3e26a2-4fd4-441f-9285-61ad5486c5b4)
![Screenshot From 2025-05-04 18-25-03](https://github.com/user-attachments/assets/c802fc5d-b925-4e5a-ae74-ba77ffe6d749)


3. Setting up the database and creating the Products table
![Screenshot From 2025-05-04 19-49-13](https://github.com/user-attachments/assets/96606b27-5744-4675-b5c1-25b6e72057b7)
![Screenshot From 2025-05-04 19-57-01](https://github.com/user-attachments/assets/922dd05b-8f1e-428b-ac41-3c9c3386d946)
![Screenshot From 2025-05-04 19-59-01](https://github.com/user-attachments/assets/c88215b0-71c6-422e-b0e7-d487586ba548)


   3.1 Setting Server Firewall to allow our local test traffic
   ![Screenshot From 2025-05-04 20-03-10](https://github.com/user-attachments/assets/095e189f-1c74-49ee-9515-aeb6623d1c79)
   ![Screenshot From 2025-05-04 20-03-38](https://github.com/user-attachments/assets/b7c85f61-25bc-4591-bddd-ad7ea8c6060e)
   ![Screenshot From 2025-05-04 20-04-03](https://github.com/user-attachments/assets/206630d0-e459-47bd-b509-1826c2921cb4)


4. Implementing Image Saving to Blob storage
  4.1 Creating Cointainers to save Product Photos
   ![Screenshot From 2025-05-04 19-45-49](https://github.com/user-attachments/assets/6a7b4e7e-54c6-41e0-a7b4-d9f262dec250)
   ![Screenshot From 2025-05-04 19-47-16](https://github.com/user-attachments/assets/c768a0b5-9fdb-4da3-979b-4390cf45dfb4)

  
5. Adding more Products/ Testing the Streamlit web app
   ![Screenshot From 2025-05-04 21-30-29](https://github.com/user-attachments/assets/accfb3ed-88a1-4fe4-9251-964fcba3b29f)
   ![Screenshot From 2025-05-04 21-31-09](https://github.com/user-attachments/assets/9c74d771-3d0e-4db6-99ed-5d43726a6a5a)
   ![Screenshot From 2025-05-04 23-49-52](https://github.com/user-attachments/assets/bc32dc43-a78a-41b7-9cd9-34d3ffb6e796)
   ![Screenshot From 2025-05-05 00-08-39](https://github.com/user-attachments/assets/37a1d88b-6401-46d9-8551-ebdbdfb7064a)


---
# What I did in this project (Summary)
- Created Storage account
- Created and seting SQL server in Azure
- Added logins crediential for SQL Login and admin setup
- Created Tables and filling e-commerce data
- Pushed the project to GitHub, after hiding sensitive strings (eg: BLOB Connection string, database logins,passwords, etc.)

# What I learned in this project (Summary)
- What is SQL server and how to set it up in Azure
- How to create table and upload data
- Different ways to authenticate with the SQL server
- Set up database and database server
- Using Streamlit for web application
- Hardcoding secrets vs using environment variables for security puroses
- How gitignore files helps keep sensetive information safe

## What was my experience with this project?
Trying out the SQL Server hands-on for the very first time felt really confusing, but navigating every other settings, section, options, menus, etc made me feel comfortable in no time. The DIO challenge added new confidence in me to try out the SQL and storage options in Azure.

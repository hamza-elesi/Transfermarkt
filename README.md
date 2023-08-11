<!DOCTYPE html>
<html>
<body>
    <h1>Transfer Players Dashboard - 2023</h1>
    <p>Welcome to the Transfer Players Dashboard project! This repository contains Python code to scrape player transfer data from transfermarkt.com in 2023, perform data cleaning, and visualize the data using a dashboard built with Dash.</p>

<h2>Table of Contents</h2>
    <ul>
        <li><a href="#overview">Overview</a></li>
        <li><a href="#project-structure">Project Structure</a></li>
        <li><a href="#setup">Setup</a></li>
        <li><a href="#usage">Usage</a></li>
        <li><a href="#how_to_run_without_MongoDB">Running the Dashboard without MongoDB</a></li>
    </ul>

<h2 id="overview">Overview</h2>
    <p>The Transfer Players Dashboard is designed to provide insights into player transfers that occurred in the year 2023. The project involves scraping transfer data, performing data cleaning using Jupyter Notebook, and visualizing the results through an interactive web dashboard.</p>

<h2 id="project-structure">Project Structure</h2>
    <ul>
        <li><code>scraper.py</code>: This Python script scrapes player transfer data from transfermarkt.com for the year 2023.</li>
        <li><code>ETL.ipynb</code>: This Jupyter Notebook covers the Extract, Transform, Load (ETL) process, cleaning the data extracted by the scraper.</li>
        <li><code>main.py</code>: The main code source for the dashboard. It connects to a MongoDB database, calculates various statistics, and displays the data using Dash and Plotly.</li>
    </ul>

<h2 id="setup">Setup</h2>
    <p>To set up the project locally, follow these steps:</p>
    <ol>
        <li>Clone the repository: <code>git clone https://github.com/hamza-elesi/Transfermarkt.git</code></li>
        <li>Install required dependencies: <code>pip install -r requirements.txt</code></li>
        <li>Run the <code>scraper.py</code> script to collect transfer data.</li>
        <li>Execute the <code>ETL.ipynb</code> notebook to clean the collected data.</li>
        <li>Run the dashboard using <code>main.py</code>.</li>
    </ol>

<h2 id="usage">Usage</h2>
    <p>After setting up the project, you can use the Transfer Players Dashboard to gain insights into player transfer activities in 2023. The dashboard includes visualizations of top nationalities by total transfer amount and the most expensive transactions.</p>
    <ol>
        <li>Access the dashboard by running <code>main.py</code>.</li>
        <li>Open a web browser and navigate to <code>http://localhost:8000</code> (if not opened automatically).</li>
        <li>Explore the visualizations to understand the transfer trends and insights.</li>
    </ol>

<h2 id="how_to_run_without_MongoDB">Running the Dashboard without MongoDB</h2>
    <p>If you want to run the dashboard using CSV data instead of MongoDB, follow these steps:</p>
    <ol>
        <li>Prepare your CSV file: Make sure you have a <code>data.csv</code> file containing the necessary transfer data.</li>
        <li>Modify the script: Open <code>main.py</code> and replace the code that connects to MongoDB with code to read data from the CSV file. Refer to comments in the script for guidance.</li>
        <li>Add this line to <code>main.py</code> to load data from the CSV file:<br><code>data = pd.read_csv('data.csv')</code></li>
        <li>Run the script: In your terminal, navigate to the project directory and run <code>python main.py</code>. The dashboard will use data from the CSV file.</li>
        <li>Access the dashboard: Open a web browser and go to <code>http://localhost:8000</code> (or the specified URL) to explore the dashboard with CSV data.</li>
    </ol>
    <hr>
    <p align="center">This README was generated with ❤️ by Jawad OUCHBAR & Hamza EL MAATAOUI</p>
</body>
</html>

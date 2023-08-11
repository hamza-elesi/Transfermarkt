import pymongo
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

# Connexion à la base de données MongoDB
client = pymongo.MongoClient('localhost', 27017)
db = client['transfers_db']
collection = db['players']
data = pd.DataFrame(list(collection.find()))

# Calculer le total des transactions de transfert
total_transactions = len(data)
# Calculer le total des transactions par nationalité
nationality_totals = data.groupby('Nationality')['Fee'].sum().nlargest(5).reset_index()
nationality_totals = nationality_totals.rename(columns={'Fee': 'Total_Price'})

# Filtrer les données pour le mois d'août
data['Transfer Date'] = pd.to_datetime(data['Transfer Date'])
data_august = data[data['Transfer Date'].dt.month == 8]  # Filtrer pour le mois d'août

# Calculer le total des montants des joueurs en août
total_amount_august = data_august['Fee'].sum()

# Créer une instance de l'application Dash
app = dash.Dash(__name__)

# Analyse : Top 5 des nationalités

fig_nationalities = px.pie(nationality_totals, values='Total_Price', names='Nationality',
                           title="Top 5 Nationalities by Total Price")


# Analyse : Transactions les plus chères
data['Fee'] = data['Fee'].replace('-', 0).astype(float)  # Convertir en float
top_transactions = data.nlargest(5, 'Fee')
fig_transactions = px.bar(top_transactions, x='Player', y='Fee', title="Top 5 Expensive Transactions")

app.layout = html.Div([
    html.H1("Tableau de bord d'analyse des transferts de joueurs", className="title"),

    # Afficher le total des transactions
    html.Div([
        html.Div(f"Total des transactions de transfert en août ", className="total-message"),
        html.Span(f"{total_transactions}", className="total-value")
    ], className="content"),
    # Afficher le total des montants des joueurs en août
    html.Div([
        html.Div(f"Total des montants des joueurs en août ", className="total-message"),
        html.Span(f"{total_amount_august:.2f} $", className="total-value amount-value")
    ], className="content"),

    dcc.Graph(figure=fig_nationalities),

    dcc.Graph(figure=fig_transactions)
], className="dashboard")

if __name__ == '__main__':
    app.run_server(debug=True, port= 8000)

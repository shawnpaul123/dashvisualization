#https://www.statworx.com/de/blog/how-to-build-a-dashboard-in-python-plotly-dash-step-by-step-tutorial/

import pandas as pd
import dash
import dash_html_components as html

#charting in dash
import dash_core_components as dcc
import plotly.express as px


files = [r"C:\Users\shawn paul\Desktop\PyFinanceProj\NASDAQPrediction\Stock_Data\ATVI.parquet"]

def load_files_local(file_paths):
	dfs_list = []
	for fil in file_paths:
		

		df = pd.read_parquet(fil)
		df['Date'] = df.index
		dfs_list.append(df)


	return dfs_list


def load_from_s3():
	pass


# Creates a list of dictionaries, which have the keys 'label' and 'value'.
def get_options(list_stocks):
    dict_list = []
    for i in list_stocks:
        dict_list.append({'label': i, 'value': i})

    return dict_list





df = load_files_local(files)[0]




#############################################DASH#############################################
# Initialise the app
app = dash.Dash(__name__)

# Define the app
app.layout = html.Div(children=[
                      html.Div(className='row',  # Define the row element
                               children=[
                                  html.Div(className='four columns div-user-controls'),  # Define the left element
                                  html.Div(className='eight columns div-for-charts bg-grey'),
                                  html.H2('Dash - Time Series Data'),
                                  html.P('''Visualising time series with Plotly - Dash'''),
                                  html.P('''Pick one or more stocks from the dropdown below.''') # Define the right element
                                  ]),

                      #dropdown options
                      html.Div(className='div-for-dropdown',
	                    children=[dcc.Dropdown(id='stockselector',
	                              options=get_options(df.columns.unique()),
	                              multi=True,
	                              value=[df.columns.unique()[0]],
	                              style={'backgroundColor': '#1E1E1E'},
	                              className='stockselector')         


                      ]),



                      dcc.Graph(id='timeseries',
                                config={'displayModeBar': False},
                                animate=True,
                                figure=px.line(df,
                                               x=df.index,#set pandas index to datatime
                                               y='Close'
                        )
                                )











                      ])

	           

                


##this is to create graphs in plotly
dcc.Graph(id='timeseries',
          config={'displayModeBar': False},
          animate=True,
          figure=px.line(df,
                         x='Volume',#set pandas index to datatime
                         y='Close'
                        )
          )
                         #color='Low',#have volume here and price elsewhere
                         #template='plotly_dark').update_layout(
                          #         {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                          #          'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
                                   




##create dropdown menu for stock names

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)



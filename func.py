import pandas as pd 
import plotly.express as px 
from plotly import graph_objects as go
from plotly.subplots import make_subplots


netflix_titles = pd.read_csv("titles.csv")
disney_titles = pd.read_csv("disney_titles.csv")
hulu_titles = pd.read_csv("hulu_titles.csv")
prime_titles = pd.read_csv("prime_titles.csv")


def show_year_hist(dataframe_1, dataframe_2, dataframe_3, dataframe_4, column_name):

    fig = make_subplots(rows=2, cols=2, 
                        subplot_titles=["5,806 total titles", "1,535 total titles", "2,396 total titles", "9,871 total titles"])

    fig.add_trace(go.Histogram(x=dataframe_1[column_name],
            marker_color="darksalmon", name="Netflix", nbinsx=50),
            row=1,col=1)

    fig.add_trace(go.Histogram(x=dataframe_2[column_name],
            marker_color="mediumorchid", name="Disney+", nbinsx=50),
            row=1,col=2)

    fig.add_trace(go.Histogram(x=dataframe_3[column_name],
            marker_color="goldenrod", name="Hulu", nbinsx=50),
            row=2,col=1)

    fig.add_trace(go.Histogram(x=dataframe_4[column_name],
            marker_color="mediumseagreen", name="Prime", nbinsx=50),
            row=2,col=2)


    fig.update_layout(height=900, width=900, title_text="Streaming Service Counts by Release Year of Movie/Show")
    fig.show("png")
    
    
def print_totals():
    print("Movie & show totals by streaming services:")
    print()
    print("Netflix: ", + len(netflix_titles))
    print()
    print("Disney+: ", + len(disney_titles))
    print()
    print("Hulu: ", + len(hulu_titles))
    print()
    print("prime: ", + len(prime_titles))
    print()


def show_bar():
    netflix_type_counts = netflix_titles["type"].value_counts()
    netflix_type_counts = [["Movies", netflix_type_counts[0]],["Shows", netflix_type_counts[1]]]
    netflix_type_counts_df = pd.DataFrame(netflix_type_counts, columns=["Types", "Counts"])

    disney_type_counts = disney_titles["type"].value_counts()
    disney_type_counts = [["Movies", disney_type_counts[0]],["Shows", disney_type_counts[1]]]
    disney_type_counts_df = pd.DataFrame(disney_type_counts, columns=["Types", "Counts"])

    hulu_type_counts = hulu_titles["type"].value_counts()
    hulu_type_counts = [["Movies", hulu_type_counts[0]],["Shows", hulu_type_counts[1]]]
    hulu_type_counts_df = pd.DataFrame(hulu_type_counts, columns=["Types", "Counts"])

    prime_type_counts = prime_titles["type"].value_counts()
    prime_type_counts = [["Movies", prime_type_counts[0]],["Shows", prime_type_counts[1]]]
    prime_type_counts_df = pd.DataFrame(prime_type_counts, columns=["Types", "Counts"])


    netflix_types = netflix_type_counts_df["Types"]
    netflix_counts = netflix_type_counts_df["Counts"]

    disney_types = disney_type_counts_df["Types"]
    disney_counts = disney_type_counts_df["Counts"]

    hulu_types = hulu_type_counts_df["Types"]
    hulu_counts = hulu_type_counts_df["Counts"]

    prime_types = prime_type_counts_df["Types"]
    prime_counts = prime_type_counts_df["Counts"]

    fig = make_subplots(rows=2, cols=2, 
                        subplot_titles=["5,806 total titles", "1,535 total titles", "2,396 total titles", "9,871 total titles"])

    fig.add_trace(go.Bar(x=netflix_types, y=netflix_counts, 
                         name="Netflix", marker_color="darksalmon", 
                         text=netflix_counts, textposition="auto"),
                        row=1, col=1)

    fig.add_trace(go.Bar(x=disney_types, y=disney_counts, 
                         name="Disney+", marker_color="mediumorchid", 
                         text=disney_counts, textposition="auto"), 
                          row=1, col=2)

    fig.add_trace(go.Bar(x=hulu_types, y=hulu_counts, 
                         name="Hulu", marker_color="goldenrod", 
                         text=hulu_counts, textposition="auto"), 
                          row=2, col=1)

    fig.add_trace(go.Bar(x=prime_types, y=prime_counts, 
                         name="Prime", marker_color="mediumseagreen", 
                         text=prime_counts, textposition="auto"), 
                          row=2, col=2)


    fig.update_layout(height=900, width=900, title_text="Streaming Service Content Counts")
    fig.show("png")
    
def show_avg():
    netflix_scores = netflix_titles["imdb_score"]
    netflix_scores = netflix_scores.dropna()
    avg_netflix = round(netflix_scores.mean(),2)

    disney_scores = disney_titles["imdb_score"]
    avg_disney = round(disney_scores.mean(),2)

    hulu_scores = hulu_titles["imdb_score"]
    hulu_scores = hulu_scores.dropna()
    avg_hulu = round(hulu_scores.mean(),2)

    prime_scores = prime_titles["imdb_score"]
    prime_scores = prime_scores.dropna()
    avg_prime = round(prime_scores.mean(),2)
    
    avg_scores = [["netflix", avg_netflix], ["disney", avg_disney], ["hulu", avg_hulu], ["prime", avg_prime]]
  
    avg_score_df = pd.DataFrame(avg_scores, columns=['service', 'avg_rating'])
    avg_score_df_sorted = avg_score_df.sort_values(by="avg_rating")
    
    x = avg_score_df_sorted["service"]
    y = avg_score_df_sorted["avg_rating"]

    colors = ["mediumseagreen", "darksalmon", "mediumorchid", "goldenrod"]

    fig = go.Figure(data=[go.Bar(
                x=x, y=y,
                text=y,
                textposition='auto',
                marker_color=colors
            )])

    fig.update_layout(title_text='Average IMDB rating by service')
    fig.show("png")
    
    
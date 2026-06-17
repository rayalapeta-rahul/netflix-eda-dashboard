import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
choice=st.sidebar.selectbox(
    "Select Analysis",
    ['Dataset Overview','Missing Values','Movies Vs TV Shows','Country Wise Movie & TV Show']
)
st.title('NETFLIX EDA Dashboard')
df=pd.read_csv('NetFlix.csv')
if choice=='Missing Values':
    st.header('Missing Values')
    missing_values = df.isnull().sum()
    st.write(missing_values)
    st.header('Missing values Visualization')
    st.bar_chart(missing_values)
if choice=='Dataset Overview':
    st.header('Dataset Shape')
    total_rows=df.shape[0]
    total_columns=df.shape[1]
    col1,col2=st.columns(2)
    col1.metric(label='total_rows',value=total_columns)
    col2.metric(label='total_columns',value=total_rows)
    st.header('Dataset Preview')
    st.write(df.head())
    st.header('Data Understanding')
    st.write('Numerical Data')
    st.write(df.describe())
    st.write('Categorical Data')
    st.write(df.describe(include='object'))
if choice=='Movies Vs TV Shows':
    st.header('Movies Vs TV Shows')
    total_movies=df[df['type']=='Movie'].shape[0]
    total_TV_Shows=df[df['type']=='TV Show'].shape[0]
    st.write('total_Movies',total_movies)
    st.write('total_TV_Shows',total_TV_Shows)
    st.header('Movies Vs TV Show -> Visualization')
    categories=['Movie','TV Show']
    counts=[total_movies,total_TV_Shows]
    plt.bar(categories,counts)
    st.pyplot(plt)
if choice=='Country Wise Movie & TV Show':
    st.header('Country Wise Movie & TV Show')
    country_group=df.groupby(['country','type']).size().unstack(fill_value=0)
    country_group['Total']=(country_group['Movie']+country_group['TV Show'])
    country_group=country_group.sort_values(by='Total',ascending=False)
    st.write('Top 10 Countries Based on the count of Movies And TV Shows',country_group.head(10))
    cat=country_group.head(10).index
    val=country_group.head(10)['Total']
    st.header('Visualization Of top 10 Countries')
    plt.xticks(rotation=45)
    plt.bar(cat,val)
    st.pyplot(plt)

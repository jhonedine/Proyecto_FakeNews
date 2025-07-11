
import pandas as pd

def load_fake_news_data():
    df_fake = pd.read_csv("data/Fake.csv")
    df_real = pd.read_csv("data/True.csv")
    df_fake["label"] = 0
    df_real["label"] = 1
    df = pd.concat([df_fake, df_real]).sample(frac=1).reset_index(drop=True)
    return df

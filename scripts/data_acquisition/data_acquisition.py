from google.colab import drive
drive.mount('/content/drive')
fake = ('https://drive.google.com/uc?id=111J3U3feYR0ri6_DlP79CGRL-WsmLiF3')
true = ('https://drive.google.com/uc?id=18-_Mg6osJGrLmW3baJTgW_-LWcPCopCE')
df_fake = pd.read_csv(fake, sep=None, engine='python')
df_true = pd.read_csv(true, sep=None, engine='python')

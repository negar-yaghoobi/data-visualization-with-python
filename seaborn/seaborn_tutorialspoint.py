# import seaborn
import seaborn as sb

# ---------------------------------------------
# Seaborn for plotting and styling
df = sb.load_dataset('tips')
print(df.head())


# --------------------------------------------
# To view all the available data sets in the Seaborn library
print (sb.get_dataset_names())
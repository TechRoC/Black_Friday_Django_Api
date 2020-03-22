from pyforest import *
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from xgboost import XGBRegressor

def preprocessing(train):
    train['Product_ID'] = train['Product_ID'].str.replace('P00', '')
    sc = StandardScaler()
    train['Product_ID'] = sc.fit_transform(train['Product_ID'].values.reshape(-1, 1))
    pkl_filename2 = "allcol.pkl"
    pkl_filename2 = os.path.dirname(__file__) + "/" + pkl_filename2
    with open(pkl_filename2,'rb') as file:
         allcol = pickle.load(file)
    allcol = allcol.drop("Purchase",axis=1)
    cols = ['Gender','Age','City_Category','Stay_In_Current_City_Years']
    df_processed = pd.get_dummies(train, columns=cols)
    newdict = {}
    
    for i in allcol:
        if i in df_processed.columns:
            newdict[i] = df_processed[i].values
        else:
            newdict[i]= 0
    newdf = pd.DataFrame(newdict)

    return  newdf
def pred(ob):
    d1 = ob.to_dict()
    df = pd.DataFrame(d1,index=[0])
    df = preprocessing(df)
    pkl_filename1 = "pickle_model.pkl"
    pkl_filename1 = os.path.dirname(__file__) + "/" + pkl_filename1
    with open(pkl_filename1,'rb') as file:
        pipeline = pickle.load(file)
    predictor = pipeline.predict(df)
    return np.round(predictor)
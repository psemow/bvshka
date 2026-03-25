def piecewise_constant(data, x_col, y_col, bins):
    data['interval'] = pd.cut(data[x_col], bins=bins, right=False)
    means = data.groupby('interval')[y_col].mean()
    preds = data['interval'].map(means)
    return r2_score(data[y_col], preds)

def piecewise_linear(data, x_col, y_col, bins):
    from sklearn.linear_model import LinearRegression
    data['interval'] = pd.cut(data[x_col], bins=bins, right=False)
    models = {}
    for interval, group in data.groupby('interval'):
        X = group[[x_col]].values
        y = group[y_col].values
        if len(X) >= 2:
            model = LinearRegression().fit(X, y)
            models[interval] = model
        else:
            models[interval] = np.mean(y) if len(y) else 0
    preds = []
    for _, row in data.iterrows():
        interval = row['interval']
        m = models[interval]
        if isinstance(m, LinearRegression):
            preds.append(m.predict([[row[x_col]]])[0])
        else:
            preds.append(m)
    return r2_score(data[y_col], preds)

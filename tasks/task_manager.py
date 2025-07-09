import pandas as pd
import matplotlib.pyplot as plt

def five_number_summary(data: list) -> dict:
    """
    Min, Q1, Median, Q3, Max değerlerini içeren sözlük döndür.
    Output örneği: {'min': ..., 'Q1': ..., 'median': ..., 'Q3': ..., 'max': ...}
    """
    data = pd.Series(data)
    result = {'min': data.min(), 
              'Q1': data.quantile(0.25), 
              'median': data.median(), 
              'Q3': data.quantile(0.75), 
              'max': data.max()}
    return result

def detect_outliers(data: list) -> list:
    """
    IQR metoduyla aykırı değerleri tespit et.
    Output: [list of outliers]
    """
    data = pd.Series(data)
    q1 = data.quantile(0.25)
    q3 = data.quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = data[(data < lower_bound) | (data > upper_bound)]
    return outliers.tolist()

def draw_boxplot(data: list) -> None:
    """
    Verinin boxplot'unu çiz.
    Output: matplotlib görseli
    """
    plt.boxplot(data)
    plt.show()

def draw_histogram(data: list, title: str = "Histogram") -> None:
    """
    Histogramı çiz.
    """
    plt.hist(data)
    plt.title(title)
    plt.show()

#Input: [1, 2, 3, 4, 100]
#Output: skewness değeri, > 0 ise sağa çarpık
def calculate_skewness(data: list) -> float:
    """
    Veri setinin skewness (çarpıklık) değerini hesapla.
    """
    return pd.Series(data).skew()

#Input: [1, 2, 3, 4, 100]
#skewness değerini hesaplamalısın. bu değere göre 'left', 'right' veya 'symmetric' değerini döndür
def is_skewed(data: list) -> str:
    """
    Skewness değerine göre 'left', 'right' veya 'symmetric' döndür.
    """
    skewness = pd.Series(data).skew()
    if skewness > 0:
        return 'right'
    elif skewness < 0:
        return 'left'
    else:
        return 'symmetric'

def calculate_covariance(x: list, y: list) -> float:
    """
    İki veri seti arasındaki kovaryansı hesapla.
    """
    return pd.Series(x).cov(pd.Series(y))

def calculate_correlation(x: list, y: list) -> float:
    """
    Pearson correlation coefficient hesapla.
    """
    return pd.Series(x).corr(pd.Series(y))

def is_positive_correlation(x: list, y: list) -> bool:
    """
    Korelasyon pozitif mi kontrol et.
    """
    corr = pd.Series(x).corr(pd.Series(y))
    return corr > 0

def compare_variables(x: list, y: list) -> dict:
    """
    Hem kovaryans hem de korelasyonu döndür.
    Output: {'covariance': ..., 'correlation': ...}
    """
    cov = pd.Series(x).cov(pd.Series(y))
    corr = pd.Series(x).corr(pd.Series(y))
    return {'covariance': cov, 'correlation': corr}
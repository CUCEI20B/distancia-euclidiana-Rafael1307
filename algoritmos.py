def distancia_euclidiana(x_1, y_1, x_2, y_2):
    xt = (x_2-x_1)*(x_2-x_1)
    yt = (y_2-y_1)*(y_2-y_1)
    return math.sqrt(xt + yt)
    